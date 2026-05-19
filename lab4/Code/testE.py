import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("data.csv", delimiter=";", comments="#")


def analyse(table):

    f_max = np.max(np.abs(table[:, 1]))
    g_max = np.max(np.abs(table[:, 2]))
    h_max = np.max(np.abs(table[:, 3]))
    print("f:",f_max, "\ng:",g_max,"\nh:", h_max)

    return(f_max, g_max, h_max)



def plot(table, figname):

    x = table[:, 0]
    fx = table[:, 1]
    gx = table[:, 2]

    plt.plot(x, fx, label="f(x)")
    plt.plot(x, gx, label="g(x)")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    plt.savefig(figname)

    return()





# Output / call fkt
analyse(data)
plot(data, "figname.png")







