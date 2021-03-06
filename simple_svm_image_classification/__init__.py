# -*- coding: utf-8 -*-
"""svm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jMoBnkX7zB6pK1bARpb_iEYd6T4xHsg1
"""

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
import cv2
import itertools
import mahotas
import numpy as np
from sklearn.model_selection import train_test_split
import os


def huFeatureImg(img): #detecting shape in img
  image = cv2.HuMoments(cv2.moments(img)).flatten()
  return image

def haralickFeatureImg(img): #this is for detecting texture in img
  image = mahotas.features.haralick(img).mean(axis = 0)
  return image

def histogramFeatureImg(img): #for extracting colors
  # compute the color histogram
  # img , dimensions, mask, histsize, ranges
  hist  = cv2.calcHist([img], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
  # normalize the histogram
  cv2.normalize(hist, hist)
  # return the histogram
  return hist.flatten()

Data = []
shape = ()
images = []
classes = []
dimension = 0
x = []
y = []
bins = 8
def preprocessDataSet(imgType):
  categories = []
  directory = "D:\python\cnn\Sign-Language-Digits-Dataset\Dataset"
  categories.append(os.listdir(directory))
  categories = list(itertools.chain.from_iterable(categories))
  for category in categories:
      print(category)
      path = os.path.join(directory, category)
      classNumber = categories.index(category)
      for image in os.listdir(path):
          if imgType == "gray":
              srcImg = cv2.imread(os.path.join(path, image))
              img = cv2.cvtColor(srcImg, cv2.COLOR_RGB2GRAY)
              # building feature matrix
              huImg = huFeatureImg(img)
              haralickImg = haralickFeatureImg(img)
              
                # convert the image to HSV color-space
                # hue, saturation, and value
              img = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)
              histImg = histogramFeatureImg(img)
              images.append(np.hstack([histImg, haralickImg, huImg]))
              classes.append(category)
              
          else:
              srcImg = cv2.imread(os.path.join(path, image))
              #huImg = huFeatureImg(img)
              haralickImg = haralickFeatureImg(srcImg)
                # convert the image to HSV color-space
                # hue, saturation, and value
              #img = cv2.imread(os.path.join(path, image))
              img = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)
              histImg = histogramFeatureImg(img)
              kk = np.hstack([histImg, haralickImg])
              images.append(kk)
              classes.append(category)
preprocessDataSet("gray")


#define standard scaler
images = np.array(images).astype(float)
images /= 255.0
ss = StandardScaler()
scaledImages = ss.fit_transform(images)

pca = PCA(n_components=250)
# use fit_transform to run PCA on our standardized matrix
#principle component analyzer
imagePCA = ss.fit_transform(scaledImages)
# look at new shape
# print('PCA matrix shape is: ', imagePCA.shape)

labelEncoder = LabelEncoder()
encodedClasses = labelEncoder.fit_transform(classes)
#scale features between 0-1
#scaler = MinMaxScaler(feature_range=(0, 1))
#rescaled_features = scaler.fit_transform(images)
X_train, X_test, Y_train, Y_test = train_test_split(imagePCA, encodedClasses,test_size=.2)
model = SVC(kernel='linear', gamma='scale')
kFold = KFold(n_splits=4)
accuracies=[]
for trainData, validationData in kFold.split(X_train):
  model.fit(X_train[trainData], Y_train[trainData])
  accuracies.append(model.score(X_train[validationData], Y_train[validationData]))

y_pred = model.predict(X_test)
print("Classification report for classifier \n%s\n"
       % (classification_report(Y_test, y_pred)))
print("Accuracy for classifier \n%s\n"
       % (accuracy_score(Y_test, y_pred)))