import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

le = preprocessing.LabelEncoder()


def readData(file):
    dataSet = pd.read_csv(file, names=['political party', 'issue1', 'issue2', 'issue3', 'issue4', 'issue5', 'issue6',
                                              'issue7', 'issue8', 'issue9', 'issue10', 'issue11', 'issue12', 'issue13', 'issue14',
                                              'issue15', 'issue16'])
    return dataSet


def labelData(dataset):
    for column in dataset.columns:
        if dataset[column].dtype == type(object):
            dataset[column] = le.fit_transform(dataset[column])
    return dataset


def handleMissingData(dataSet):
    for i in dataSet.columns[1:]:
        noOcurrences = dataSet[i].value_counts()['n']
        yesOcurrences = dataSet[i].value_counts()['y']
        if yesOcurrences >= noOcurrences:
            dataSet[i].replace(to_replace="?", value="y", inplace=True)
        else:
            dataSet[i].replace(to_replace="?", value="n", inplace=True)
    return dataSet


def splitData(percent, dataSet): #0.25
    targetVariable = dataSet.iloc[:, 0]  # y
    parameters = dataSet.iloc[:, 1:]  # x
    parametersTrain, parametersTest, targetVariableTrain, targetVariableTest = train_test_split(parameters,
                                                                                                targetVariable,
                                                                                                train_size=percent)
    return parametersTrain, parametersTest, targetVariableTrain, targetVariableTest


def classification(parametersTrain, targetVariableTrain, randomSeed=0):

    print("seed: ", randomSeed)
    classifyData = DecisionTreeClassifier(criterion="entropy", splitter="random", random_state=randomSeed)
    classifyData.fit(parametersTrain, targetVariableTrain)
    return classifyData


def predictOutput(classifyData, parametersTest, targetVariableTest):
    targetPredict = classifyData.predict(parametersTest)
    tree = classifyData.tree_
    size = tree.node_count
    accuracy = accuracy_score(targetVariableTest,targetPredict)
    print("tree size : ", size)
    print("accuracy: " , accuracy)
    return accuracy, size


def run(df):
    meanAccuracies = []
    meanSizes = []
    percentList = [30, 40, 50, 60, 70]
    for j in percentList:
        accuracies = []
        sizes = []
        print("percent: ", j)
        for i in range(5):
            parametersTrain, parametersTest, targetVariableTrain, targetVariableTest = splitData(j, df)
            dataClassification = classification(parametersTrain, targetVariableTrain, random.randint(1, 100))
            accuracy, size = predictOutput(dataClassification, parametersTest, targetVariableTest)
            accuracies.append(accuracy)
            sizes.append(size)
            print("--------------------------------------------------------")
        meanSize = np.mean(sizes)
        meanSizes.append(meanSize)
        meanAccuracy = np.mean(accuracies)
        meanAccuracies.append(meanAccuracy)
        print("Accuracy: ")
        print("mean: ", meanAccuracy, " ", "max: ", np.amax(accuracies), " ", "min: ", np.amin(accuracies))
        print("Size: ")
        print("mean: ", meanSize, " ", "max: ", np.amax(sizes), " ", "min: ", np.amin(sizes))
        print("**************************************************************")
    plt.plot(percentList, meanAccuracies, "b+")
    plt.locator_params(axis='x', nbins=len(percentList))
    plt.show()
    plt.plot(percentList, meanSizes, "g.")
    plt.locator_params(axis='x', nbins=len(percentList))
    plt.show()


if __name__ == '__main__':
    df = readData('votes.txt')
    df = handleMissingData(df)
    df = labelData(df)
    run(df)
