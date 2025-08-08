import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    n=np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)

    ss_xy = np.sum(x * y) - n * m_x * m_y
    ss_xx = np.sum(x * x) - n * m_x * m_x

    m = ss_xx / ss_xy
    c = m_y - m * m_x
    return (m, c)


def plot_regression_line(x, y, b):
    plt.scatter(x, y, color='r', marker='o', s=30)
    y_pred = b[0] + b[1] * x

    plt.scatter(x, y_pred, color='g', marker='o', s=60)
    plt.plot(x, y_pred, color='b')

    plt.xlabel("--------------X--------------->")
    plt.ylabel("--------------Y--------------->")

    plt.show()


# mannual Code for Linear Regression
def startAIAlgorithm():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])



    m,c=estimate_coef(x,y)
    print("Estimated coefficients:\n")
    print("Slope m= ",m)
    print("y_intercept c=",c)
    print("Model :  y  =",m,"* X + ",c)
    plot_regression_line(x,y,[c,m])



if __name__=="__main__":
    startAIAlgorithm()





# fine tune== Approx value ,assuption
# bias=>+ve,-ve biase=>
