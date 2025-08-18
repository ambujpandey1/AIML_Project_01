#Practical implimentation of LogisticRegression(Based on Sigmoid Function)

# Step 1: Import required libraries
import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Step 2: Create a very simple dataset
data = {
    'Age':          [22,   25,    47,    52,    46,    56,    55,    60,    18,   28],
    'InsuredOrNot': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
}


df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 3: Convert target column (Yes/No) to numbers
label_encoder = LabelEncoder()
df['InsuredOrNot'] = label_encoder.fit_transform(df['InsuredOrNot'])
# Now: No = 0, Yes = 1

print("\nDataset after encoding:")
print(df)

# Step 4: Split into Features (X) and Target (y)
X = df[['Age']]         # Feature column   ==== df[ :, 0:1]
y = df['InsuredOrNot']  # Target column

# Step 5: Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X, y) # It will calculate parameters (= m & c )

# Step 6: Make a prediction
# Example: Predict if a 40-year-old person will be insured
predicted_value = model.predict([[57]])
predicted_label = label_encoder.inverse_transform(predicted_value)

print("\nPrediction for Age = 57 years old:", predicted_label[0])

# Step 7 (Optional): Predict probabilities
probability = model.predict_proba([[57]])  # [probability of No, probability of Yes]
print("Prediction probabilities (No, Yes):", probability[0])