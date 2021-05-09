import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import math

df=pd.read_csv('datasets/test_scores.csv')

def gradient_descent(x,y,it,lr):
    m_curr=b_curr=0
    iterations=it
    n=len(x)
    learning_rate=lr
    cost_previous=0
    

    for i in range(iterations):
        y_predicted=m_curr*x+b_curr

        cost=(1/n)*sum([val **2 for val in (y-y_predicted)])

        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)

        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        # if():


        # print("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost,i))
    
    return m_curr,b_curr




# def predict_using_sklean(x,y):
#     # df = pd.read_csv("datasets/test_scores.csv")
#     r = LinearRegression()
#     r.fit(x,y)
#     return r.coef_, r.intercept_

def predict_using_sklean():
    # df = pd.read_csv("datasets/test_scores.csv")
    r = LinearRegression()
    r.fit(df[['math']],df.cs)
    return r.coef_, r.intercept_


if __name__=="__main__":
    x=np.array(df.math)
    y=np.array(df.cs)
    it=1000000
    lr=0.0002

    # gradient_descent(x,y,it,lr)
    coeff,intercept=gradient_descent(x,y,it,lr)
    print("Using grad descent - Coeff/slope {} , intercept {}".format(coeff,intercept))

    m_sklearn, b_sklearn = predict_using_sklean()
    print("Using sklearn: Coef {} Intercept {}".format(m_sklearn,b_sklearn))
