import gpxpy.gpx
import pandas as pd
from datetime import datetime
import numpy as np

# Leer el archivo gpx:
# Este es el archivo de la ruta original del recorrido que hice con Franzi corriendo.
gpx_file = open('activity_6266217162.gpx', 'r')
gpx = gpxpy.parse(gpx_file)

dict_points = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            trkpoint = {
                "latitude": point.latitude,
                "longitude": point.longitude,
                "elevation": point.elevation,
                "time": point.time
            }
            dict_points.append(trkpoint)

df = pd.DataFrame.from_dict(dict_points)

# Asumiendo que empezamos a caminar el 13.02.13 14:05:00 hora alemana
t_start = datetime(2021, 2, 13, 13, 5, 0, 0)
# Asumiendo que terminamos de caminar el 13.02.13 15:15:00 hora alemana
t_end = datetime(2021, 2, 13, 14, 15, 0, 0)

# Tiempo de duración de la caminata
time_span = t_end - t_start

# Número de puntos guardados en el archivo original
nr_points = len(dict_points)

delta_t = time_span / nr_points

# Calculando los nuevos tiempos. Asumiendo que el tiempo de muestreo es (delta_t)
new_datetimes = []
for i in range(0, nr_points):
    new_datetimes.append(np.datetime64(t_start + i * delta_t))

# Agregando los nuevos tiempos al DataFrame
df['zoufine_time'] = new_datetimes

# Eliminando la columna time, ya que no es necesaria
df = df.drop(columns="time")

# Renombrando la columna zoufine_time en time
df = df.rename(columns={"zoufine_time": "time"})

# Creating a new file:
# --------------------

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Creando los puntos de la nueva ruta
for idx in df.index:
    gpx_segment.points.append(
        gpxpy.gpx.GPXTrackPoint(latitude=df['latitude'][idx], longitude=df['longitude'][idx],
                                elevation=df['elevation'][idx],
                                time=df['time'][idx]))

with open('myfirstroute.gpx', "w") as f:
    f.write(gpx.to_xml())
    print("Archivo gpx generado con éxito.")
