# In the Python file, write a PySpark script that loads the TSLA csv files into a single DataFrame and then
# properly sorts the combined data by date because the files contain stock data from each day in unsorted order.

# Your goal is to return a sorted list of days that had a volume greater than 50 million. 
# The output should just be a normal Python list, for example:
# ['2019-11-21', '2019-12-16', ...]


from pyspark.sql import SparkSession
  
spark = SparkSession.builder.appName("ChallengeSolution").getOrCreate()

df_1 = spark.read.csv("data/TSLA-1.csv", header=True, inferSchema=True)
df_2 = spark.read.csv("data/TSLA-2.csv", header=True, inferSchema=True)

lista = []
for df in (df_1, df_2):
  filtro = df.filter(df["Volume"] > 50000000)
  tmp = [ k["Date"] for k in filtro.select("Date").collect() ]
  lista.extend( tmp )

ok = sorted( [k.isoformat() for k in lista ] )
print(ok)
