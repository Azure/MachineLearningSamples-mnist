from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from azureml.core.run import Run

run = Run.get_submitted_run()

mnist = fetch_mldata('MNIST original')

# use the full set with 70k records
#X, y = mnist['data'], mnist['target']

# use the 5,000 random records to reduce training time.
np.random_state = 42
shuffle_index = np.random.permutation(70000)[:5000]
X, y = mnist['data'][shuffle_index], mnist['target'][shuffle_index]

print('X: ', X.shape)
print('y: ', y.shape)
print('labels: ', np.unique(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

lr = LogisticRegression()
print("training a logistic regression model...")
lr.fit(X_train, y_train)
print(lr)

y_hat = lr.predict(X_test)
acc = np.average(np.int32(y_hat == y_test))
run.log('accuracy', acc)

print('Overall accuracy:', acc)


