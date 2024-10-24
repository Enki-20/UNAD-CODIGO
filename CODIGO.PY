#Importamos librerias necesarias
from pyspark.sql import SparkSession, functions as F
# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('Tarea3').getOrCreate()
# Define la ruta del archivo .csv en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/9sih-mvrc.csv'
# Lee el archivo .csv
df = spark.read.format('csv').option('header','true').option('inferSchema', 'true').load(file_path)
#imprimimos el esquema
df.printSchema()
# Muestra las primeras filas del DataFrame
df.show()
# Estadisticas básicas
df.summary().show()
# Filtrar las multas con valor mayor a 500,000 y seleccionar columnas
print("Multas con valor mayor a 500,000\n")
multas_altas = df.filter(F.col('valor_multa') > 500000).select('valor_multa', 'fecha_multa', 'placa')
multas_altas.show()

# Ordenar las multas por el valor en orden descendente
print("Multas ordenadas de mayor a menor valor\n")
multas_ordenadas = df.sort(F.col('valor_multa').desc())
multas_ordenadas.show()

# Filtrar las multas no pagadas y mostrar la ciudad y placa
print("Multas no pagadas\n")
multas_no_pagadas = df.filter(F.col('pagado_si_no') == 'NO').select('ciudad', 'placa', 'valor_multa')
multas_no_pagadas.show()
