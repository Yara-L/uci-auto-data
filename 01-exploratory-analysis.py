# import ml libraries 
import numpy as np
import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt

### IMPORT: ------------------------------------
data_path = 'csv/00-cleaned-up-data.csv'
df = pd.read_csv(data_path)

### CORRELATION STUDY: -------------------------------

## overall correlation:
print('correlation table -----------------------')
print(df.corr())

## continuous predictor correlation: -----------
print('individual correlations -----------------------')
# engine-size:price
print(df[["engine-size", "price"]].corr())
plt.figure(1)
sns.regplot(x="engine-size", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-engine-size.png')

# horesepower:price
print(df[["horsepower", "price"]].corr())
plt.figure(2)
sns.regplot(x="horsepower", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-horsepower.png')

# highway-mpg:price
print(df[["highway-mpg", "price"]].corr())
plt.figure(3)
sns.regplot(x="highway-mpg", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-highway-mpg.png')

# curb-weight:price
print(df[["curb-weight", "price"]].corr())
plt.figure(3)
sns.regplot(x="curb-weight", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-curb-weight.png')

# normalized-losses:price
print(df[["normalized-losses", "price"]].corr())
plt.figure(4)
sns.regplot(x="normalized-losses", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-normalized-losses.png')

# symboling:price
print(df[["symboling", "price"]].corr())
plt.figure(5)
sns.regplot(x="symboling", y="price", data=df)
plt.savefig('plots/01-a-reg-plot-symboling.png')


## categorical correlation: -------------------
print('value-counts table -----------------------')
# body-style:price
plt.figure(6)
print(df["body-style"].value_counts())
sns.boxplot(x="body-style", y="price", data=df)
plt.savefig('plots/01-b-box-plot-body-style.png')

# aspiration:price
plt.figure(7)
print(df["aspiration"].value_counts())
sns.boxplot(x="aspiration", y="price", data=df)
plt.savefig('plots/01-b-box-plot-aspiration.png')

# fuel-system:price
plt.figure(8)
print(df["fuel-system"].value_counts())
sns.boxplot(x="fuel-system", y="price", data=df)
plt.savefig('plots/01-b-box-plot-fuel-system.png')

# drive-wheels:price
plt.figure(9)
print(df["drive-wheels"].value_counts())
sns.boxplot(x="drive-wheels", y="price", data=df)
plt.savefig('plots/01-b-box-plot-drive-wheels.png')

# make:price
plt.figure(9)
print(df["make"].value_counts())
sns.boxplot(x="make", y="price", data=df)
plt.savefig('plots/01-b-box-plot-make.png')

# plt.show()