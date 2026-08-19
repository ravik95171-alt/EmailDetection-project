import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Dataset load karo
data = pd.read_csv("spam_dataset_100_rows.csv")

# 2. Label convert karo (spam=1, ham=0)
data['label'] = data['label'].map({'spam':1, 'ham':0})

# 3. Text → Numeric
cv = CountVectorizer()
X = cv.fit_transform(data['text'])

y = data['label']

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 5. Model trai karo
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Prediction
y_pred = model.predict(X_test)

# 7. Accuracy check
print("Accuracy:", accuracy_score(y_test, y_pred))

# 8. User input test
while True:
    msg = input("\nEnter email text (or type exit): ")
    if msg.lower() == "exit":
        break
    
    msg_data = cv.transform([msg])
    result = model.predict(msg_data)

    if result[0] == 1:
        print(" Spam Email")
    else:
        print(" Not Spam")
