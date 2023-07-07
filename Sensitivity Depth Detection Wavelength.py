import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle




filepath = "/Users/vemani/Documents/NEC Sensitivity Studies/Cloud Analysis V4/"
dir_list = os.listdir(filepath)


all_readings = pd.DataFrame()
all_readings_50 = pd.DataFrame()
all_readings_100 = pd.DataFrame()

for item in dir_list:
    if ".csv" in item and (not ("cap" in item)or "baseline" in item):
        print(item)
        fp = filepath + item
        
        label = item#.split("_")[-1]
        
#fp = filepath + input("Train filename: ")

        df = pd.read_csv(fp, header = None)
        df.columns = df.loc[4]
        
        cols = df.columns
        
        df = df[[not(x) for x in pd.to_numeric(df["% wl"],errors = "coerce").isna()]].astype(float)
        df = df.reset_index(drop=True)
        
        df = 10**(df)
        
        dif_50 = df.loc[1,cols[4:]] - df.loc[0,cols[4:]]
        dif_100 = df.loc[3,cols[4:]] - df.loc[2,cols[4:]]
        
        dif = dif_50-dif_100
        
        
        
        all_readings_50[label] = dif_50
        all_readings_100[label] = dif_100
        
        
        
        #all_readings[label] = dif    
        
#SIGNAL -- How much change in sat leads to change in fluence
#NOISE --- How much change in other stuff leads to change in fluence
        
#noise = pd.Series([np.std(row) for index, row in all_readings_50.iterrows()], index = dif_50.keys())
#signal = pd.Series([np.mean(row) for index, row in all_readings.iterrows()], index = dif_50.keys())

noise = pd.Series([])
signal = pd.Series([])

for index in all_readings_50.index:
    
    data_50 = (all_readings_50.loc[index])
    data_100 = (all_readings_100.loc[index])
    
    mean = np.mean(data_50) - np.mean(data_100)
    var = np.sqrt(np.var(data_50) + np.var(data_100)) + np.sqrt(np.mean(data_50)) #Added Poisson shot noise
    
   # print(var)
    
   # key = all_readings_50.index[index]
    
    signal[index] = mean
    
    noise[index] = var
    


snr = signal/noise



