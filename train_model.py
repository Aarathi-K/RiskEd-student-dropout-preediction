import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "student_dropout_dataset.csv")

df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip().str.lower()

X = df[['attendance','avg_marks','fee_delay_count','backlogs','extracurricular_score']]
y = df['dropout']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

pickle.dump(model, open("dropout_model.pkl", "wb"))

print("Model training done")