# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
adult_1_prepared_a = dataiku.Dataset("adult_1_prepared_a")
adult_1_prepared_a_df = adult_1_prepared_a.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

myython_df = adult_1_prepared_a_df # For this sample code, simply copy input to output
asdfas

# Write recipe outputs
myython = dataiku.Dataset("myython")
myython.write_with_schema(myython_df)
