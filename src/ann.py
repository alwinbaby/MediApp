from timeit import default_timer

import pandas
from sklearn import preprocessing
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


class ArtificialNeuralNetwork:
    @staticmethod
    def data_sweep():
        # Assigning column names to the dataset
        names = ["itching", "skin_rash", "chills", "vomiting", "fatigue", "prognosis"]
        # reading data to panda dataframe
        data = pandas.read_csv("../csv/Example_ANN_Training_Samples.csv", names=names)
        # assign data from first five columns to X variable
        x = data.iloc[:, 0:5]
        # assign data from first fifth columns to y variable
        y = data.select_dtypes(include=[object])
        le = preprocessing.LabelEncoder()
        y = y.apply(le.fit_transform)
        return x, y

    @staticmethod
    def ann_train_test_split(x, y):
        sweep_x = x
        sweep_y = y
        x_train, x_test, y_train, y_test = train_test_split(
            sweep_x, sweep_y, test_size=0.20
        )
        # Feature Scaling for uniform evaluation
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train = scaler.transform(x_train)
        x_test = scaler.transform(x_test)
        return x_train, x_test, y_train, y_test

    @staticmethod
    def ann_training(x_train, x_test, y_train, y_test):
        model_start_time = default_timer()
        mlp = MLPClassifier(hidden_layer_sizes=(5, 5, 5), max_iter=1000)
        mlp.fit(x_train, y_train)
        predictions = mlp.predict(x_test)
        clf = SVC(random_state=0)
        clf.fit(x_train, y_train)
        model_end_time = default_timer()
        print(
            f"Model finished construction in {model_end_time - model_start_time} seconds"
        )
        plot_confusion_matrix(clf, x_test, y_test)
        print("The ANN reported:")
        print(confusion_matrix(y_test, predictions))
        print(classification_report(y_test, predictions))
