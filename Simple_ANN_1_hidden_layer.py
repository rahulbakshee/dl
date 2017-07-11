################################################################################################
# Below code is inspired from http://iamtrask.github.io/2015/07/12/basic-python-network/#
################################################################################################


import numpy as np


#input and output
x = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T


#weights initialisation
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1


for i in range(100000):
    #forward
    l1 = 1/(1 + np.exp(-(np.dot(x,syn0))))
    l2 = 1/(1 + np.exp(-(np.dot(l1, syn1))))
    #print("l1", l1)
    #print("l2", l2)

    #backprop
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T)*(l1*(1-l1))

    #weights update
    syn1 += l1.T.dot(l2_delta)
    syn0 += x.T.dot(l1_delta)
    if i%10000 == 0:
        print("l2 error mean", y-l2)
print("l2",l2)
