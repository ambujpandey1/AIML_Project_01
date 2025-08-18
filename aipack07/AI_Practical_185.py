import warnings
warnings.filterwarnings(action="ignore")

from sklearn.preprocessing import LabelEncoder

# Step 1: Create some sample data
colors = ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green','Red']

# Step 2: Create the LabelEncoder object
encoder = LabelEncoder()

# Step 3: Fit and transform the data
encoded_colors = encoder.fit_transform(colors)

# Step 4: Show results
print("Original data:", colors)
print("Encoded data :", encoded_colors)
# Step 5: Decode numbers back to original labels
decoded_colors = encoder.inverse_transform(encoded_colors)
print("Decoded data :", decoded_colors)