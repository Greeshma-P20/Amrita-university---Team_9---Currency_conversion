import pandas as pd

import glob

import os, sys

path = "C:/Users/grees/OneDrive/Desktop/NTRS_APAC/Data_set" # enter the path of folder of all csv files for filling missing data

  
# csv files in the path
files = glob.glob(path + "/*.csv")
for fname in files:
        print(fname)
        df = pd.read_csv(fname)
        print(df)
        for column in df:
            df[column] = df[column].fillna(method='ffill')

        for column in df:
            if column == 'Date':
                continue
            else:
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)
        print(df)
        df.to_csv(fname, index=False)
