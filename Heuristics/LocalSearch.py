
########### NQUEEN PROBLEM: LOCAL SEARCH 
### F.Mazza M63001338

import random
import math
import time

#### Come è fatta la soluzione?
# La soluzione più semplice, non è quella di forma matriciale, bensì una sol
# che ha la forma di un vettore lungo N, dove in ogni locazione, è 
# rappresentante di una riga, ed il numero conservato rappresenta
# la posizione occupata dalla regina in quella riga.

# Esempio: {si va da 0 a N-1}
# [0,2,6,1,...,-]   Nella riga 0 --> regina in posizione 0
#                   Nella riga 1 --> regina in posizione 2
#                   Nella riga 2 --> regina in posizione 6 etc...

def localSearch(N):
    max_iter = 150000
    current_state = generateRandomState(N)			# Prima sol: --> Casuale
    current_cost = Conflicts(current_state)		# Calcolo costo iniziale

    for i in range(max_iter):
        
        print("Inizio prossima iterazione con soluzione corrente:")
        print(current_state, current_cost)

        pos1 = random.randint(0,len(current_state)-1)

        # MOSSA: prendo una riga a caso (pos1), le soluzioni dell'intorno sono quelle ottenute
        # scambiano pos1 con ognuna delle altre righe disponibili.

        for j in range(len(current_state)):
            next_state = generateNextState(current_state,pos1,j)	   # Ottieni il nuovo stato
            #next_state = generateNextStateSwap(current_state)	
            next_cost = Conflicts(next_state)					       # Calcola il suo valore di costo
            print("Provo:","Swap",pos1,j,next_state,next_cost)
            
            if (next_cost < current_cost):
                current_state = next_state
                current_cost = next_cost

            if (current_cost == 0):
                return current_state
                

    return current_state


# Funzione di costo della soluzione: ogni volta che una coppia di regine è in posizione
# di attacco, il costo aumenta di 1 (numero di conflitti). Quando il costo della soluzione candidata è zero,
# allora la soluzione è ammissibile.

def Conflicts(Sol):
    cost = 0
    for pos in range(0, len(Sol)):
        for next_pos in range(pos+1, len(Sol)):

            # Conflitto 1: Se sono sulla stessa colonna --> conflitto
            # Conflitto 2: Se due regine sono disposte a distanza di x righe le une dalle altre
            #              ma distano anche x colonne ---> conflitto

            # Esempio: [-,5,-,7,-,-] 
            # regina 1: riga 1, col 5
            # regina 2: riga 3, col 7 
            # da cui: (7-5) = 2
            #         (3-1) = 2

            # --|--|--|--|--|--|--|--|
            # --|--|--|--|--|xx|--|--|
            # --|--|--|--|--|--|--|--|
            # --|--|--|--|--|--|--|xx|
            # --|--|--|--|--|--|--|--|
            # --|--|--|--|--|--|--|--|
            # --|--|--|--|--|--|--|--|
            # --|--|--|--|--|--|--|--|


            if (Sol[pos] == Sol[next_pos]) or abs(pos - next_pos) == abs(Sol[pos] - Sol[next_pos]):
                cost = cost + 1
                
    return cost


# Genera una candidata soluzione casuale (stato iniziale)
# assegnando randomicamente a ciascuna riga i numeri da 0 a N-1 (colonne regine)

def generateRandomState(n):
    return list(range(n))		


# Genera una nuova candidata soluzione (nuovo stato), per farlo, prende due valori
# casualmente e li scambia, sperando di abbassare la f. di costo.

def generateNextState(state,pos1,pos2): 
    state = state[:]
    state[pos1], state[pos2] = state[pos2], state[pos1]
    return state

def generateNextStateSwap(state): 
    state = state[:]
    i, j = random.sample(range(len(state)), 2)
    state[i], state[j] = state[j], state[i]
    return state


####### Funzioni per rappresentare la scacchiera in modo plausibile... ########

def create_grid(GRID_SIZE):
    tab = []
    for i in range(GRID_SIZE):
        tab.append([])
        for j in range(GRID_SIZE):
            tab[i].append("")
    return tab


def print_grid(tab,GRID_SIZE,ris):
    for i in range(GRID_SIZE):
        print("{} ".format(i + 1), end="")
        for j in range(GRID_SIZE):
              
            if j == ris[i]:
              print("\u2655{}".format(tab[i][j]), end="")
            else:
              print("--".format(tab[i][j]), end="")
            if j < GRID_SIZE:
                print("|", end="")

        if i < GRID_SIZE:
            print()


#####################################################################################

def main():

	# PARAMETRI ALG.
	N = 8

	start = time.time()
	ris = localSearch(N)
	GRID_SIZE = N

	# PRINT DEI RISULTATI
	# Ricorda: le regine possono essere piazzate sulle righe/colonne da 0 a N-1

	print("Runtime in second:", time.time() - start)

	print("Soluzione Ottenuta: ")
	print(ris)

	print("Dispsizione scacchiera:")
	print_grid(create_grid(N),GRID_SIZE,ris)


if __name__ == "__main__":
    main()

#####################################################################################