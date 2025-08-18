# Step 1: Import required libraries
import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Step 2: Read dataset from CSV file
df = pd.read_csv("LgR_Movies_kNN_classifier.csv")
print("Dataset:\n", df)

# Step 3: Define features (X) and target (y)
X = df[['kicks', 'kisses']]        # independent features
y = df['movietype']                # dependent target

# Step 4: Create and train the KNN model
model = KNeighborsClassifier(n_neighbors=5)  # using k=3 neighbors
model.fit(X, y)

# Step 5: Make prediction for new instance (?,18,90,Unknown)
sample = [[18, 90]]  # kicks=18, kisses=90
prediction = model.predict(sample)

print("\nPrediction for (kicks=18, kisses=90):", prediction[0])