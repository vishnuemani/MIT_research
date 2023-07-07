import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "/Users/vemani/Downloads/" + input("filename")

filepath = "/Users/vemani/Downloads/V3_Wavelength_results_full spectrum.csv"

df = pd.read_csv(filepath, header = None)
df.columns = df.loc[4]



df = df[[not(x) for x in pd.to_numeric(df["% sat"],errors = "coerce").isna()]].astype(float)
df = df.reset_index(drop=True)




#absorbances = pd.DataFrame([columns = df.columns)

absorbances = []


for a in range(int(len(df["% sat"])/4)):
    
    absorbances.append(df.loc[4*a+3]-df.loc[4*a])

absorbances = pd.concat(absorbances,axis = 1).transpose()
absorbances["% sat"] = df["% sat"].unique()
##ABOVE PLOTS SATS WITH DIFF IN ABSORBANCES

guesses = []

for a in range(int(len(df["% sat"])/4)):
    
    abs_diff = df[df.columns[4:]].loc[4*a]/3 - df[df.columns[4:]].loc[4*a+3]/3
    cd = df[df.columns[3]][4*a+3] - df[df.columns[3]][4*a]
    co = df[df.columns[2]][4*a+3] - df[df.columns[2]][4*a]
    sat_guess = (abs_diff-cd*150/64500)/((co-cd)*150/64500)
    guesses.append(sat_guess)

guesses = pd.concat(guesses,axis = 1).transpose()
guesses["% sat"] = df["% sat"].unique()
#THIS PLOTS THE SAT GUESSES AT THE DIFFERENT DETECTOR LOCATIONS

absorbances.to_csv("/Users/vemani/Downloads/absorbance_table.csv")
guesses.to_csv("/Users/vemani/Downloads/guesses_table.csv")


vals = []
for a in range(int(len(df["% sat"])/4)):
    
    val = df[df.columns[4:]].loc[4*a]/3
    vals.append(val)
vals = pd.concat(vals,axis = 1).transpose()
vals["% sat"] = df["% sat"].unique()

for col in range(4,len(absorbances.columns)):
    plt.plot(absorbances["% sat"],absorbances[absorbances.columns[col]], label = str(absorbances.columns[col]))
plt.legend()
plt.savefig('graph.png')
#plt.plot(absorbances["% sat"],vals[vals.columns[2]])