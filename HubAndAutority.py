import json
import numpy as np


def calHubAndAuthority(Parent, iteration, Hub, Aut):
    autVector = np.matrix(Aut)
    hubVector = np.matrix(Hub)
    ParentM = np.matrix(Parent)
    ChildM = np.matrix(Parent).transpose()
    for i in range(iteration):
        tempHub = ParentM.dot(autVector)
        tempAut = ChildM.dot(hubVector)
        autVector = tempAut
        hubVector = tempHub
        print()
        print("iteration:" + str(i+1))
        print("Hub vector")
        print(hubVector)
        print("Authority vector")
        print(autVector)


with open('input.json') as file:
    data = json.load(file)

G = data["G"]
Hub = data["Hub"]
Aut = data["Aut"]

calHubAndAuthority(G, 2, Hub, Aut)
