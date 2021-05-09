import numpy as np
import pandas as pd

def gradient_descent1(x,y,it,lr):
    m_curr=b_curr=0
    iterations=it
    n = len(x)
    learning_rate=lr


    for i in range(iterations):
        #linear function eqn
        y_predicted=m_curr*x+b_curr

        # cost function
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])

        # partial derivatives
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum((y-y_predicted))

        # learning rates
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        # cost_curr=cost

        print("m {} , b {} , cost {}, iteration {}".format(m_curr,b_curr,cost,i))

    return m_curr,b_curr


x=np.array([1,2,3,4,5])
y =np.array([5,7,9,11,13])
it=1500
lr=0.08

coeff,intercept=gradient_descent1(x,y,it,lr)
print("Using grad descent - Coeff/slope {} , intercept {}".format(coeff,intercept))
