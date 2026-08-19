import pandas as pd
import matplotlib as plt
import seaborn as sns

dataset = pd.read_csv("spam_dataset_100_rows.csv")
##print(dataset.head(3))

##check the null value
print(dataset.isnull().sum())

## check the dublicate value
