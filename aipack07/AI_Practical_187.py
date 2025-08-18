#Practical Implimentation of GaussianNB algorithm
#( Based on concept of Conditional Probability )

# Step 1: Import required libraries
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

# Step 2: Create a very simple weather dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],
    'Play':    ['No',    'No',    'Yes',      'Yes',  'No',   'Yes',  'Yes',      'No',    'Yes',   'Yes']
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 3: Convert categorical values to numbers
# Machine learning models work with numbers, not text
le_outlook = LabelEncoder()
le_play = LabelEncoder()

df['Outlook'] = le_outlook.fit_transform(df['Outlook'])
df['Play'] = le_play.fit_transform(df['Play'])

print("\nDataset after encoding:")
print(df)

# Step 4: Split data into features (X) and target (y)
X = df[['Outlook']]  # Feature column====> df[:, 0:1]
y = df['Play']       # Target column

# Step 5: Create and train the Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X, y)

# Step 6: Make a prediction
# Example: Predict if we should play when Outlook is 'Sunny'
outlook_value = le_outlook.transform(['Sunny'])  # Convert text to number
prediction = model.predict([[outlook_value[0]]])

# Step 7: Convert prediction back to 'Yes' or 'No'
predicted_label = le_play.inverse_transform(prediction)

print("\nPrediction for Outlook = 'Sunny':", predicted_label[0])