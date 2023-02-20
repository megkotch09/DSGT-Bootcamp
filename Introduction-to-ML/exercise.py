from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


def get_iris_dataset():
    iris = datasets.load_iris()
    X, y = iris.data[:, [0, 1]], iris.target
    df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
    return df

def perform_train_test_split():
    # fetching the data from previous method
    df = get_iris_dataset()

    # fetching X columns (sepal lenght, sepal width) and Y (labels)
    X, y = df.iloc[:, [0, 3]], df.target

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True)

    return X_train, X_test, y_train, y_test

def instantiate_models():
    """
    Fill in the blanks to instantiate the models using scikit learn. Return a tuple in the format:
    (SVM model, Decision Tree model, MLP model, KNN Model)
    
    Fill in the blanks as shown
    """
    #YOUR CODE HERE
    svm = SVC(kernel='linear')
    dt = DecisionTreeClassifier(max_leaf_nodes=5)
    mlp = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, max_iter = 100) #?
    knn = KNeighborsClassifier(n_neighbors=7) #???
    return svm, dt, mlp, knn

def fit_models():
    """
    For each model from the instantiate_model() function, fit the models. 
    
    Fill in the blanks as ashown
    """
    svm, dt, mlp, knn = instantiate_models()
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    svm.fit(X_train, Y_train)
    dt.fit(X_train, Y_train)
    mlp.fit(X_train, Y_train)
    knn.fit(X_train, Y_train)
    return svm, dt, mlp, knn #return fitted models


def accuracy_at_least_90():
    """
    Choose a model from the instantiate_models function. Play around with the hyperparameters (eg: turning the dials and 
    knobs) from the instantiate_models() function and get the accuracy to at least 0.9.
    
    Recommended link to help you: https://scikit-learn.org/stable/supervised_learning.html
    
    The above link contains documentation to the scikit-learn library you are using
    
    Fill in the blanks
    
    Return format is tuple of the form (model, accuracy)
    """
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    
    #svm, dt, mlp, knn = instantiate_models()
    
    #s, d, m, k = fit_models()
    s, d, m, k = fit_models()

    predS = s.predict(X_test)
    predD = d.predict(X_test)
    predM = m.predict(X_test)
    predK = k.predict(X_test)

    accS = accuracy_score(Y_test, predS)
    accD = accuracy_score(Y_test, predD)
    accM = accuracy_score(Y_test, predM)
    accK = accuracy_score(Y_test, predK)

    print(accS, accD, accM, accK)

    model = s
    accuracy = accS
    
    return model, accuracy #Return tuple format (model, accuracy). Look at sklearn.metrics to see how to calculate accuracy
    
    
    