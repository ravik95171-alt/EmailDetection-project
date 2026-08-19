##import pandas as pd
##import matplotlib.pyplot as plt
##
##
#### dataset load
##dataset = pd.read_csv("Emails_data.csv")
##print(dataset.head(5))
##
##
####Label convert (spam=1, ham=0)
##dataset['label'] = dataset['label'].map({'spam':1, 'ham':0})
##print(dataset['label'])
##
##
#### message(text) ko → Numeric  me convert kar dega
##from sklearn.feature_extraction.text import CountVectorizer
##cv = CountVectorizer()
##x=cv.fit_transform(dataset['message']).toarray()
##y=dataset['label']
##print(x)
##print(y)
##
##
#### for graph plot
##plt.scatter(x[:,0],dataset["label"])
##plt.xlabel("Word Frequency")
##plt.ylabel("label(0==ham,1==spam)")
##plt.show()
##
##
##
#### Train-Test Split
##from sklearn.model_selection import train_test_split
##x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
##
##
#### Model train
##from sklearn.naive_bayes import MultinomialNB
##model = MultinomialNB()
##model.fit(x_train, y_train)
##
#### Prediction
##y_pred = model.predict(x_test)
##print(y_pred)
##
####  Accuracy check
##from sklearn.metrics import accuracy_score
##print("Accuracy:", accuracy_score(y_test, y_pred))
##
### User input test
##while True:
##    msg = input("\nEnter email text (or type exit): ")
##    if msg.lower() == "exit":
##        break
##    
##    msg_data = cv.transform([msg])
##    result = model.predict(msg_data)
##
##    if result[0] == 1:
##        print(" Spam Email")
##    else:
##        print(" Not Spam")


import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.show()






































