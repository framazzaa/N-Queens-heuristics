import time
import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB


# Dimensioni scacchiera:
n = 1024

# Creazione modello:
m = gp.Model("NQUEENS")

# Introduciamo le variabili decisionali:
x = m.addMVar((n, n), vtype=GRB.BINARY, name="x")

# Funzione obiettivo: massimizzare il numero delle regine presenti (n):
m.setObjective(x.sum(), GRB.MAXIMIZE)

# Per ogni riga/colonna valgono i seguenti constraints:
for i in range(n):

    # Al massimo una regina per riga:
    m.addConstr(x[i, :].sum() == 1, name="row"+str(i))

    # Al massimo una regina per colonna:
    m.addConstr(x[:, i].sum() == 1, name="col"+str(i))

# Vincolo diag:
# Elenco tutti gli indici da considerare per ogni diag nella somma (vettori I e J)

for k in range(1-n,n-1):
    I = [] 
    J = []
    for i in range(n):
        for j in range(n):
            if (i-j)==k:
                I.append(i)
                J.append(j)
    m.addConstr(x[I,J].sum() <= 1, name="diag"+str(k))
    

# Vincolo adiag:
# Elenco tutti gli indici da considerare per ogni adiag nella somma (vettori I e J)

for k in range(2,2*n):
    I = [] 
    J = []
    for i in range(n):
        for j in range(n):
            if (i+j)==k:
                I.append(i)
                J.append(j)
    m.addConstr(x[I,J].sum() <= 1, name="adiag"+str(k))
    
# Ottimizzazione
m.optimize()

print(x.X)
print('Queens placed: %g' % m.ObjVal)

# Rappresentazione grafica del risultato ottenuto:

GRID_SIZE = n
ris = x.X

def create_grid():
    tab = []
    for i in range(GRID_SIZE):
        tab.append([])
        for j in range(GRID_SIZE):
            tab[i].append("")
    return tab
    
def print_grid(tab):
    for i in range(GRID_SIZE):
        print("{} ".format(i + 1), end="")
        for j in range(GRID_SIZE):
              
            if ris[i][j] == 1:
              print("\u2655{}".format(tab[i][j]), end="")
            else:
              print("--".format(tab[i][j]), end="")
            if j < GRID_SIZE:
                print("|", end="")

        if i < GRID_SIZE:
            print()
        

# Ricorda che le regine possono essere piazzate sulle colonne da 0 a N-1
print("Soluzione Ottenuta: ")
print("Dispsizione scacchiera:")
print_grid(create_grid())
