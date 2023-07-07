# Numerical Comparisons



import os
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.signal import butter, lfilter, freqz
import numpy as np




avgs = {}

import tkinter as tk
import tkinter.filedialog as fd

#root = tk.Tk()
#filez = fd.askopenfilenames(parent=root, title='Choose a file')



filez = os.listdir("NEC Project Roche/Benchtop Data/V3 Ref/")

numlist = {} # check that the average over 3 trials worked

for file in filez:

        try:
            raw = pd.read_csv("NEC Project Roche/Benchtop Data/V3 Ref/" + file, sep = "\t", skiprows = range(40))
            
            cleaned_data = raw.drop(raw.index[-1])#.astype(float)
            
            
            
        except:
            print("Bad File, not including", file)
            continue
        
        else:
            
        
            name_list = []
            
            opt_num = int((len(cleaned_data.columns)-2)/3)
            
            for i in range(opt_num):
                
                name_list.append("optode" + str(i+1) + "_"+ "730")
                name_list.append("optode" + str(i+1) + "_"+ "amb")
                name_list.append("optode" + str(i+1) + "_"+ "850")
            
            name_list.insert(0,"time")
            name_list.append("unknown")
            
            
            
            cleaned_data.columns = name_list
            
            cleaned_data = cleaned_data.astype(float)
            
            means = cleaned_data.iloc[:-1].astype(float).mean()
            
            short_name = file.split('_')[0] + file.split('_')[1]
           
           
            print(np.mean(cleaned_data["optode17_730"]))
            #print(np.mean(cleaned_data["optode17_730"]))
            
            
            
            
            
            
            
            try:
                
                current  = avgs[short_name]
                
                new = [current[0] + np.mean(cleaned_data["optode17_730"]), current[1] + np.mean(cleaned_data["optode17_850"])]
                avgs[short_name]  = new
                
                numlist[short_name] += 1
                
            except:
                avgs[short_name] = [np.mean(cleaned_data["optode17_730"]), np.mean(cleaned_data["optode17_850"])]
                
                numlist[short_name] = 1
            
            
            #print(np.mean(cleaned_data["optode1_850"]))        
    
            
        
avgs = 1/3 * pd.DataFrame.from_dict(avgs).T

columns = ["750", "830"]



avgs.columns = columns

plt.bar(avgs.index, avgs["750"])

plt.ylim(min(avgs["750"])-500, max(avgs["750"])+50)


avgs.to_csv("benchtop_reading_avgs.csv")
