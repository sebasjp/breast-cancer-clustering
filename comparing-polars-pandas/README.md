# Comparando Polars y Pandas

El objetivo es comparar la librería [Polars](https://www.pola.rs/) con [Pandas](https://pandas.pydata.org/), en algunos procesos comunes en el procesamiento de datos.

Para esto, se realizó la simulación de diferentes conjuntos de datos, utilizando la librería [scikit-learn](https://scikit-learn.org/stable/). Se simularon 20 conjuntos de datos, desde 500 registros hasta 30MM cada uno con 11 variables, los cuales fueron guardados en formato `parquet`. [Código generador de los datos](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/create_data.py).

Se midió la ejecución de 5 procesos: lectura, calculo de promedios, ordenamiento, groupby y calculo de promedios moviles a partir de groupby. [Código de los procesos](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/process.py).


Para cada proceso, vamos a visualizar dos graficas: la primera hasta 1MM de registros, la segunda desde 5MM hasta 30MM.

## Tiempo de lectura

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_reading_menor5.png?raw=true)

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_reading_mayor5.png?raw=true)

En general, los tiempos de lectura de los archivos `.parquet` es muy similar entre ambas librerías, sin embargo, con `pandas` no fue posible procesar más de 10MM de registros, mientras que con `polars` se pudo procesar hasta 25MM. Claro, esto está ligado a la capacidad del equipo con el que estoy realizando este ejercicio, el cual tiene 7Gb de RAM disponibles.

## Tiempo de calculo de promedios en todas las variables

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_mean_menor5.png?raw=true)

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_mean_mayor5.png?raw=true)


## Tiempo de ordenamiento por id

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_sorting_menor5.png?raw=true)

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_sorting_mayor5.png?raw=true)


## Tiempo de agrupación por id

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_groupby_mean_menor5.png?raw=true)

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_groupby_mean_mayor5.png?raw=true)


## Tiempo de calculo de promedios moviles

Este es la comparación que más me sorprendió, debido a que es uno de los procesos que más utilizó en el día a día para crear variables, y de manera contundente `polars` tiene un rendimiento cerca de 60 veces más rápido que `pandas`, cuando tenemos 10MM de registros.

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_moving_avg_menor5.png?raw=true)

![](https://github.com/sebasjp/data-science-applications/blob/master/comparing-polars-pandas/output/time_moving_avg_mayor5.png?raw=true)


## Conclusión

En general, `polars` tiene un rendimiento impresionantemente bueno en comparación con `pandas`, vale bastante la pena utilizarlo tanto en el desarrollo de proyectos de Data Science, como en la automatización de los mismos, pues debido a como está construida/optimizada esta librería, puede llevar a disminuir costos de manera significativa en los pipelines que tienen un fuerte procesamiento de datos.

## Librerias y versiones utilizadas
```
     total  used   available
Mem: 6,7Gi  2,1Gi   4,2Gi
```

```
python==3.8.10
pandas==1.5.3
polars==0.16.10
pyarrow==11.0.0
scikit-learn==1.2.1
```