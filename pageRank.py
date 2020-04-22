import numpy as np
import json


def printPageRank(pageRank, iteration):
    print("iteration "+str(iteration)+":\t", end='')
    for x in range(pageRank.shape[1]):  # num of column of matrix
        print("page" + str(x + 1), end=': ')
        print("{:.3f}".format(pageRank[0, x]), end='\t')  # round down to 3 decimal place
    print()


def calPageRank(PR, G, d, n, norm):
    H = G                           # convert G to H
    for row in range(len(H)):
        total = sum(H[row])
        if total != 0:
            for column in range(len(H[0])):
                H[row][column] /= total

    pageRank = np.matrix(PR)
    printPageRank(pageRank, 0)
    for i in range(1, n+1):
        pageRank = (1 - d) + d * pageRank.dot(H)
        if norm == 1 or (norm == 2 and i == n):
            L1Norm = np.sum(pageRank)
            pageRank = pageRank / L1Norm
        printPageRank(pageRank, i)


with open('input.json') as file:
    data = json.load(file)

PR = data["PR"]
G = data["G"]

calPageRank(PR, G, 0.15, 3, 0)
