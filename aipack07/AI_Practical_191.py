# Step 1: Import libraries
import warnings
warnings.filterwarnings(action="ignore")
from sklearn import svm

# Step 2: Create a very small dummy dataset
# X = features, y = labels
# Let's say we classify points into 2 groups (0 and 1)
X = [[1, 2], [2, 3], [3, 3], [8, 8], [9, 10], [10, 8]]
y = [0, 0, 0, 1, 1, 1]  # first 3 are class 0, last 3 are class 1

# Step 3: Create and train the SVM model
model = svm.SVC(kernel='linear')  # using a simple linear kernel
model.fit(X, y)

# Step 4: Make a prediction
sample = [[4, 4]]   # test point
prediction = model.predict(sample)

print("Prediction for [4,4]:", prediction[0])