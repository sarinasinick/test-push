# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
sample_data_prepared = dataiku.Dataset("sample_data_prepared")
sample_data_prepared_df = dkuspark.get_dataframe(sqlContext, sample_data_prepared)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
testorc_df = sample_data_prepared_df # For this sample code, simply copy input to output

# Write recipe outputs
testorc = dataiku.Dataset("testorc")
dkuspark.write_with_schema(testorc, testorc_df)
