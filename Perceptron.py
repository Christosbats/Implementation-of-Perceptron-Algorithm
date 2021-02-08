import numpy as np
from matplotlib import pyplot as plt
import random

#2-Input AND, OR gate Perceptron

Inputs = [[0,0],[0,1],[1,0],[1,1]]
while True:
    print("In which gate do you want to run the perceptron? Choose between AND and OR")
    userInput = input()
    if (userInput == "AND" or userInput == "and"):
        Outputs = [0,0,0,1]
        break
    elif(userInput == "OR" or userInput == "or"):
        Outputs = [0,1,1,1]
        break
    else:
        print("NOT VALID GATE")



Weight1 = random.random()                             
Weight2 = random.random()
learningRate = 0.1
epoch = 30
bias = random.random()


def fx(a1,a2,w1,w2,b):
    sum = a1*w1 + a2*w2 + b
    if(sum<=0): #threshold = 0
        return 0
    else:
        return 1

def dW(lr,target,eksiswsh,a):
    return lr*(target - eksiswsh)*a

def newWeight(w1,dW):
    return w1 + dW

def updateBias(bias,lr,expected,prediction):
    return bias + lr*(expected-prediction)

for j in range(epoch):
    for i in range(4):
        y = fx(Inputs[i][0],Inputs[i][1],Weight1,Weight2,bias)
        DW1 = dW(learningRate,Outputs[i],y,Inputs[i][0])
        DW2 = dW(learningRate,Outputs[i],y,Inputs[i][1])
        Weight1 = newWeight(Weight1,DW1)
        Weight2 = newWeight(Weight2,DW2)
        bias = updateBias(bias,learningRate,Outputs[i],y)
        plt.scatter(Inputs[i][0],Inputs[i][1],color="r")

print("Weight1:",Weight1)
print("Weight2:",Weight2)
print("Bias:",bias)

print("Give values to the two inputs (0 or 1)")


input1 = float(input())
input2 = float(input())
y = fx(input1,input2,Weight1,Weight2,bias)
print(y)

#MATHS
"""
w1 * x1 + w2 * x2 + b, x1=x and x2 = y
Then we have w1x + w2y + b which is similar to Ax + By - C = 0

x = -(b - w2y) / w1
if y == 0
x = -(b - w2 * 0) / w1 <=> x = -b / w1

y = -(b - w1x) / w2
if x == 0
y = -(b - w1 * 0) / w2 <=> y = -b / w2

point_1 = (0, -b / w2) 
point_2 = (-b / w1, 0)

slope = (y2 - y1) / (x2 - x1)
intercept = y

func = slope*x + intercept
"""

xfunc = -bias/Weight1 
yfunc = -bias/Weight2

point1 = [0,yfunc]
point2 = [xfunc,0]

slope = -(bias/Weight2)/(bias/Weight1)
intercept = -bias/Weight2

if (userInput == "AND" or userInput == "and"):
    plt.title("AND Gate")
else:
    plt.title("OR Gate")

plt.plot(point1,point2)
plt.show()
