import pandas as pd
import matplotlib.pyplot as plt
import warnings
from IPython.display import display

warnings.filterwarnings('ignore')

path = "../titanic-data/train.csv"
dataset = pd.read_csv(path)

survived_subset = dataset[dataset['Survived']==1]
dead_subset = dataset[dataset['Survived']==0]

print("\nFirst few passengers who survived:\n")
print(survived_subset.head())

print("\nFirst few passengers who didn't survive:\n")
print(dead_subset.head())

survived = survived_subset['Sex].value_counts()
dead = dead_subset['Sex'].value_counts()

df = pd.DataFrame([survived,dead])
df.index = ['Survived','Died']
#df.plot(kind='bar',stacked=True, figsize=(5,3), title="Survived/Died by Class")

#Class1_survived= 1.0*df.iloc[0,0]/df.iloc[:,0].sum()*100
#Class2_survived = 1.0*df.iloc[0,1]/df.iloc[:,1].sum()*100
#Class3_survived = 1.0*df.iloc[0,2]/df.iloc[:,2].sum()*100

#print("\nPercentage of Class 1 that survived: {}%".format(round(Class1_survived)))
#print("Percentage of Class 2 that survived: {}%".format(round(Class2_survived)))
#print("Percentage of Class 3 that survived: {}%".format(round(Class3_survived)))

#print("\nTable displaying survival by class:\n")
#display(df)

