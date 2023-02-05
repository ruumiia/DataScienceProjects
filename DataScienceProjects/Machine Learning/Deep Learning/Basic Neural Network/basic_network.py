
import numpy as np # import numpy library

def relu(input): # rectified linear unit
    return np.maximum(input, 0)

def sigmoid(input): # sigmoid function
    return 1/(1+np.exp(-input))

def nnmodel(value1, value2, value3): # neural network model

    # input layer
    input = [value1, value2, value3]
    wnode0 = [0.12, 0.10, 0.22]
    bnode0 = 0.27
    wnode1 = [1, 1, -1]
    bnode1 = 1

    # processing hidden layer 1
    anode0 = relu(np.dot(input, wnode0) + bnode0)
    anode1 = relu(np.dot(input, wnode1) + bnode1)

    # hidden layer 1 inputs
    input2 = [anode0, anode1]
    wnode2 = [0.55, 0.66]
    bnode2 = 0.27
    wnode3 = [0.77, 0.55]
    bnode3 = 1

    # processing hidden layer 2
    anode2 = relu(np.dot(input2, wnode2) + bnode2)
    anode3 = relu(np.dot(input2, wnode3) + bnode3)

    # hidden layer 2 inputs
    input3 = [anode2, anode3]
    wnode4 = [1, 0.50]
    bnode4 = 0.27
    wnode5 = [0.25, 0.50]
    bnode5 = 1

    # processing hidden layer 3
    anode4 = relu(np.dot(input3, wnode4) + bnode4)
    anode5 = relu(np.dot(input3, wnode5) + bnode5)

    # hidden layer 3 inputs
    output = [anode4, anode5]
    woutput = [0.25, 0.75]
    boutput = 0.27

    # processing output layer
    aoutput = sigmoid(np.dot(output, woutput) + boutput)

    # return output layer value
    return aoutput

def printallpred (input_val): # print all predictions

    final = np.zeros(len(input_val)) # initialize array

    if len(input_val.shape) > 1: # check if array dimension is more than 1

        for i in range(len(input_val)): # loop through array to perform multiple predictions with nnmodel
            final[i] = nnmodel(input_val[i][0],input_val[i][1],input_val[i][2])  

        for i in range(len(input_val)): # loop through array to print all predictions
            print ("\ninput:", input_val[i], "output:", final[i])

    else: # perform prediction with 1 dimensional array with nnmodel
        final = nnmodel(input_val[0],input_val[1],input_val[2]) # perform prediction
        print ("\ninput:", input_val, "output:", final) # print prediction


input_val = np.array([[1,2,3],[2,3,4],[4,5,6]]) # input array
printallpred(input_val) # print all predictions
