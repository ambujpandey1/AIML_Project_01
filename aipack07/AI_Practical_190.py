# Step 1: Import libraries
import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Step 2: Read dataset
df = pd.read_csv("sportsDataset.csv")
print("Dataset:\n", df)

# Step 3: Encode categorical data into numbers
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_play = LabelEncoder()

df['Outlook'] = le_outlook.fit_transform(df['Outlook'])
df['Temperature'] = le_temp.fit_transform(df['Temperature'])
df['Humidity'] = le_humidity.fit_transform(df['Humidity'])
df['Wind'] = le_wind.fit_transform(df['Wind'])
df['Play'] = le_play.fit_transform(df['Play'])

# Step 4: Define features and target
X = df[['Outlook','Temperature','Humidity','Wind']]
y = df['Play']

# Step 5: Train Random Forest
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Step 6: Predict for a new sample
# Example: Outlook=Sunny, Temp=Cool, Humidity=High, Wind=Strong
# sample = [[le_outlook.transform(['Sunny'])[0],
#            le_temp.transform(['Cool'])[0],
#            le_humidity.transform(['High'])[0],
#            le_wind.transform(['Strong'])[0]]]

sample = [[le_outlook.transform(['Overcast'])[0],
           le_temp.transform(['Mild'])[0],
           le_humidity.transform(['High'])[0],
           le_wind.transform(['Strong'])[0]]]

prediction = model.predict(sample)

# Step 7: Print details
print("\nPrediction for (Overcast, Mild, High, Strong):", le_play.inverse_transform(prediction)[0])