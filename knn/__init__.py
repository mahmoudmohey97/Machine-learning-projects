import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

class node:
    distance = 10000000000000000000
    nearestTuple = []

def readData():
    trainingData = pd.read_csv("TrainData.txt", header=None).values.tolist()
    testData = pd.read_csv("TestData.txt", header=None).values.tolist()
    return trainingData, testData

def nearestKth(tuple, trainingData, kth):
    output = []
    distanceList = euclideanDistance(tuple, trainingData)
    distanceList.sort(key = lambda x : x.distance)
    return distanceList[0:kth]

def euclideanDistance(tuple, trainingData):
    distanceList=[]
    for i in range(len(trainingData)):
        distance = 0
        for j in range(len(tuple) - 1):
            distance += math.pow(math.fabs(float(tuple[j]) - float(trainingData[i][j])), 2)
        n = node()
        n.distance = math.sqrt(distance)
        n.nearestTuple = trainingData[i]
        distanceList.append(n)
    return distanceList

def handleTie(classes, trainData):
    predictedClasses = sorted(classes.items(), key=lambda kv: kv[1], reverse=True)
    tie = True
    if len(predictedClasses) == 1:
        return predictedClasses[0][0]
    if (predictedClasses[0][1] != predictedClasses[1][1]):
        tie = False
        return predictedClasses[0][0]
    if tie == False:
        print("predicted : ", predictedClasses[0][0])
    else:
        tiedClasses = []
        tiedClasses.append(predictedClasses[0][0])
        for i in range(1, len(predictedClasses)):
            if (predictedClasses[i][1] != predictedClasses[i - 1][1]):
                break
            if predictedClasses[i][0] not in tiedClasses:
                tiedClasses.append(predictedClasses[i][0])
        for i in trainData:
            if i[-1] in tiedClasses:
                return i[-1]

def featuresOccurrence(nearElements):
    classes = {}
    for i in nearElements:
        if i.nearestTuple[-1] not in classes:
            classes.update({i.nearestTuple[-1]: 1})
        else:
            classes[i.nearestTuple[-1]] += 1
    return classes

if __name__ == '__main__':
    trainingData, testData = readData()
    kELements = []
    accuracies = []
    g_max = 0
    k_max = 0
    file = open("report.txt", 'a+')
    for k in range(1,10):
        correctCount = 0
        total = 0
        accuracy = 0.0
        print("K = ", k)
        file.write("K = " + str(k) + "\r\n")
        for i in testData:
            nearestRows = nearestKth(i, trainingData, k)
            classes = featuresOccurrence(nearestRows)
            actualclass = i[-1]
            predictedClass = handleTie(classes, trainingData)
            if(actualclass == predictedClass):
                correctCount += 1    
            file.write("Predicted : " + predictedClass+ "  " + "Actual : " + actualclass+ "\r\n")    
            total += 1
        accuracy = correctCount / total
        if accuracy > g_max:
            g_max = accuracy
            k_max = k
        kELements.append(k)
        accuracies.append(accuracy)
        
        file.write("Number of correctly classified instances : " + str(correctCount) + "\r\n")       
        file.write("Total number of instances : " + str(total) + "\r\n")        
        file.write("Accuracy :  " + str(accuracy) + "\r\n")
        file.write("----------------------------------------------------------------------------------" + "\r\n")
    file.close()
    print("k Max =", k_max)
    print("accuracy =", g_max)
    plt.plot(kELements, accuracies, "b.")
    plt.locator_params(axis='x', nbins=len(kELements))
    plt.show()