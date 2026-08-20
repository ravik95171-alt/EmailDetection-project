import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

dataset=pd.read_csv("regularization_house_price.csv")


## 1 = print(dataset.head(3))




## 2 = kya eske undar linear regretion aplly hoga, check kro
## esake liye correlate chek kro jo highely hona chahiye
##plt.figure(figsize=(10,10))
##sns.heatmap(data=dataset.corr(),annot=True)
##plt.show()



## 3 = for scaling , seprate the independet and dependent variable

x=dataset.iloc[ :,:-1]  ## ye last column ko chhod dega (resion by -1 , yani price vali column)
y=dataset["price"]
##print(x)

sc=StandardScaler()
sc.fit(x)
a=sc.transform(x)
##print(a)
## esi ko dataframe me banane per
x=pd.DataFrame(sc.transform(x),columns=x.columns)
##print(x)


## 4 = for train,test,split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


## call the feature
from sklearn.linear_model import LinearRegression, Lasso , Ridge
lr = LinearRegression()
lr.fit(x_train, y_train)
a=lr.score(x_test,y_test)*100
##print(a)

## 5 = lasso and Ridge ke vallue ke coefficeint ko represent by gragh
##plt.bar(x.columns,lr.coef_)
##plt.title("LinearRegression")
##plt.xlabel("columns")
##plt.ylabel("coef")
##plt.show()


##  6 = Lasso ( it is fetures remove )
la=Lasso(alpha=0.5)
la.fit(x_train ,y_train)
a=la.score(x_test,y_test)*100
##print(a)

## graph for lasso
plt.bar(x.columns,la.coef_)
plt.title("Lasso")
plt.xlabel("columns")
plt.ylabel("coef")
##plt.show()



## Ridge (reduce the coefficeint value)
ri=Ridge(alpha=10)
ri.fit(x_train ,y_train)
b=ri.score(x_test,y_test)*100
print(b)

## graph for Ridge
plt.bar(x.columns,ri.coef_)
plt.title("Ridge")
plt.xlabel("columns")
plt.ylabel("coef")
plt.show()








































x



