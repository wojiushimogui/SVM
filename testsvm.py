#################################################  
# svm: support vector machine  
# Author :   
# Date   :   
# HomePage :
# Email  :  
#################################################  
  
from numpy import *  
import svm  
  
################## test svm #####################  
## step 1: load data  
print ("step 1: load data...")  
dataSet = []  
labels = []  
fileIn = open('D:/xuepython/svm/testSet.txt')  
for line in fileIn.readlines():  
	lineArr = line.strip().split('\t')  
	dataSet.append([float(lineArr[0]), float(lineArr[1])])  
	labels.append(float(lineArr[2]))  
#将数据转化为矩阵，并将labels转置一下,于是类别标签向量的每行元素都和数据矩阵中的行一一对应。
dataSet = mat(dataSet)  
labels = mat(labels).T 
#选取testSet.txt文件中前80个样本数据为训练样本，后面的数据为测试样本  
train_x = dataSet[0:81, :]  
train_y = labels[0:81, :]  
test_x = dataSet[80:101, :]  
test_y = labels[80:101, :] 

  
## step 2: training...  
print ("step 2: training..." ) 
C = 0.6  
toler = 0.001  
maxIter = 50  
svmClassifier = svm.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))  
  
## step 3: testing  
print ("step 3: testing..." ) 
accuracy = svm.testSVM(svmClassifier, test_x, test_y)  
  
## step 4: show the result  
print ("step 4: show the result...")    
print ('The classify accuracy is: %.3f%%' % (accuracy * 100) ) 
svm.showSVM(svmClassifier)  