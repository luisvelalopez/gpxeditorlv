# gpxeditorlv

Toma como base una ruta guardada con el reloj Garmin Forerunner 45 y calcula los tiempos que en teoría habría guardado el reloj recorriendo la misma ruta caminando.

El algoritmo asume que todos los puntos se guardan con un tiempo de muestreo constante.

El tiempo de muestreo es calculado con la fórmula:

* dt = (tiempo inicial - tiempo final) / número de puntos de la ruta original

## Parámetros de entrada

* Hora inicial del recorrido
* Hora final del recorrido
* Archivo gpx de la ruta original

## Parámetros de salida

* Archivo gpx con la ruta generada usando las coordenadas del recorrido original y los tiempos calculados por el algoritmo

