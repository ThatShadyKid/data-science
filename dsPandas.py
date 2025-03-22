import pandas as pd
import numpy as np

df = pd.read_csv('inventory.txt')

def basics():
    print(df.head()) # tabulates the first 5 rows 
    print(df.describe())

def add_column():
    df['Total Stock Value'] = df['Cost'] * df['Quantity']

basics()
add_column()
print(df.head())