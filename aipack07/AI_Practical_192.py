import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

df=pd.read_csv("customers_LDA2.csv")
print("Datasets:\n",df)

x=df[['Age','Salary']]
y=df['Buy']

lda=LinearDiscriminantAnalysis()
lda.fit(x,y)

sample=[[53,32000]]
prediction=lda.predict(sample)
result=None
if prediction[0]==1:
    result="Buy"
else:
    result="Not Buy"
print("\nprediction for Age=53 ,Salary=32000: ",result)

# Step 2: Separate data for visualization
X = df["Age"]
Y = df["Salary"]
Z = df["Buy"]

# Step 3: Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot Buy=1 in green and Buy=0 in red
ax.scatter(X[Z==1], Y[Z==1], Z[Z==1], c='green', marker='o', label='Buy')
ax.scatter(X[Z==0], Y[Z==0], Z[Z==0], c='red', marker='x', label='Not Buy')

# Step 4: Set labels
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_zlabel("Buy (0=No, 1=Yes)")
ax.set_title("3D Visualization of Customers Dataset")

ax.legend()
plt.show()
