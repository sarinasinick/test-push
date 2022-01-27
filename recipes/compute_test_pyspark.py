# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
adult__1_ = dataiku.Dataset("adult__1_")
adult__1__df = dkuspark.get_dataframe(sqlContext, adult__1_)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
test_pyspark_df = adult__1__df # For this sample code, simply copy input to output

# Write recipe outputs
test_pyspark = dataiku.Dataset("test_pyspark")
dkuspark.write_with_schema(test_pyspark, test_pyspark_df)
