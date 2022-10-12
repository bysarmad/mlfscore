# Load packages
import numpy as np 
import pandas as pd 
from sklearn.metrics import f1_score
from IPython.core.display import HTML
from IPython.core.interactiveshell import InteractiveShell
#%config InlineBackend.figure_format = 'retina'

# Load data from the csv file
df = pd.read_csv("F1-score_data.csv")
df.head()
print(df.head())

THRESHOLD = 0.65                 # Choose your threshold for which you want to calculate the F-score

# Convert the probability predicted by the model to an actual binary prediction
def convert_to_pred(x):
    if x < THRESHOLD:            # If under threshold,
        return 0                   # map to 0.
    else:                        # Else,
        return 1                   # map to 1.

df['PREDICTION'] = df['PROBABILITY'].apply(lambda x: convert_to_pred(x))

df.head()
print(df.head())

f1_score(df['ACTUAL LABEL'], df['PREDICTION'])
print(f1_score(df['ACTUAL LABEL'], df['PREDICTION']))