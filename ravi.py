
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## dataset load
dataset = pd.read_csv("Emails_data.csv")
print(dataset.head(5))

## check null value
a=dataset.isnull().sum()
##print(a)

##dataset['label'] = dataset['label'].map({'spam':1, 'ham':0})

## message(text) ko → Numeric  me convert kar dega
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x=cv.fit_transform(dataset['message']).toarray()
y=dataset['label']
##print(x)

## for graph plot
plt.scatter(x[:,0],dataset["label"])
plt.xlabel("Word Frequency")
plt.ylabel("label(0==ham,1==spam)")
plt.show()



