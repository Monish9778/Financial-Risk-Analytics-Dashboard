from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data_preprocessing import load_and_preprocess
import pickle

X, y = load_and_preprocess()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

with open("risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print(f"Model trained successfully | Accuracy: {accuracy:.2f}")
