import pandas as pd

import warnings
warnings.filterwarnings('ignore')

path = "../titanic-data/train.csv"
dataset = pd.read_csv(path)

print("Our data set is a Pandas dataframe object:\n")
print("type = {}\n".format(type(dataset)))

print("First few entries of our training data set:\n")
print(dataset.head())
