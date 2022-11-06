import pandas as pd
import numpy as np
import time

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

import xgboost as xgb
from xgboost import plot_importance

import warnings
warnings.filterwarnings('ignore')


from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import json
import os
import numpy as np

# Read in data
x_train = pd.read_csv('datasets/x_train.csv', header = None).to_numpy()
y_train = np.ravel(pd.read_csv('datasets/y_train.csv', header = None).to_numpy())
x_test = pd.read_csv('datasets/x_test.csv', header = None).to_numpy()
y_test = np.ravel(pd.read_csv('datasets/y_test.csv', header = None).to_numpy())

# Fit a model
logReg = LogisticRegression(class_weight = 'balanced')
model = logReg.fit(x_train, y_train)

acc = model.score(x_test, y_test)
print(acc)
with open("metrics.txt", "w") as outfile:
    outfile.write("Accuracy: " + str(acc) + "\n")

# Plot it
disp = ConfusionMatrixDisplay.from_estimator(
    model, x_test, y_test, normalize="true", cmap=plt.cm.Blues
)
plt.savefig("plot.png")
