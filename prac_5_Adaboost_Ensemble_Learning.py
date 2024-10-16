sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create the AdaBoost classifier
abc = AdaBoostClassifier(algorithm='SAMME', n_estimators=50, learning_rate=1)
print(abc)

# Fit the model
model = abc.fit(X_train, y_train)
print(model)

# Make predictions
y_pred = model.predict(X_test)

# Print predictions and accuracy
print(model)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


prac_5
