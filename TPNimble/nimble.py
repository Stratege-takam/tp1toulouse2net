import sys;

#importation de la bibliothèque pour générer un nombre aléatoire
from random import randint




#board: liste contenant les pionts du plateau
#n = len(board)
#p = max de piont pouvant contenir une case à l'initialisation
#i et j = deux entiers quelconques permettant de parcourir notre board



#initialise le plateau ou encore le board
def newBoard(n,p):
    #initialisation du  board
    board = []
    #incrementer i de 0 à n-1 pour remplir le  bord
    for i in range(0,n):
        #ajouter le nombre généré au board :  le nombre génére  randint(0,p) est  un nombre de pion compris entre 0 et p
        board.append(randint(0,p))
    #retourner la liste de board
    return  board


#procedure pour afficher le plateau dans la  display(board, n):
def display(board, n):
    #incrémenter la boucle allant de 0 à n,pour chaque valeur de i afficher le board d'indice i puis |
    for i in range(0,n):
        print("{} |".format(board[i]),end="\t")
    #ajout d'un retour chariot
    print("\n")
    #afficher la ligne du dessous
    for i in range(0,n):
        #l'affichage d'un nombre et | se fait sur quatre ticonsole
        print("----",end="")
    print("\n")
    # afficher les indices plus 1 du board
    for i in range(0, n):
        # le numero de la case
        j = i + 1
        print("{}".format(j), end="\t")
    print("\n")

#determiner si le pion est déplacable
def possibleSquare(board,n,i):
    #on adapte le choix de l'utilisateur à  l'indice normal du board
    i = i -1
    #une case contient un pion déplacable si elle a au moins un pion et ce n'est pas la première case et que l'indice demande existe
    if i<=0 or i>=n or  board[i]==0:
        return False
    return True
#demande le numéro de la case source qui contient le pion à déplacer si possibleSquare retourne faux on redemande à l'utilisateur d'entrer une nouvelle case
def selectSquare(board,n):
    #décision
    decision= False
    #permet de récuperer le numéro de la case
    i = 0
    #tant que décision = false alors il n'est pas possible de récuperer le pion alors on éffectue les mème opérations
    while decision == False:
        #récuperer la case entré par l'utilisateur
        i= eval(input("choice a square : "))
        #récuperer la décision : si c'est possible de récuperer le pion ou pas
        decision= possibleSquare(board,n,i)
    return i

#vérifier si la case sollicitée peut contenir un pion déplacable
def possibleDestination(board,n,i,j):
    #on affecte les valeurs i et j aux indices du tableaux
    i= i-1
    j = j-1
    #il faut que la case d'indice j existe c'est à dire doit ètre > à 0 et < n et j doit ètre < à i et j ne doit pas etre > à la taille du board qui est n
    if j>=i or j<0 or j>=n:
        return False
    return True

#demande le numéro de la case de destination et retourne le numéro de cette si possible destination vaut true
def selectDestination(board,n,i):
    #décision
    decision= False
    #permet de récuperer le numéro de la case
    j = 0
    #tant que décision = false alors il n'est pas possible de récuperer le pion alors on éffectue les mème opérations
    while decision == False:
        #récuperer la case entré par l'utilisateur
        j= eval(input("choice a destination : "))
        #récuperer la décision : si c'est possible de récuperer le pion ou pas
        decision= possibleDestination(board,n,i,j)
    return j
#deplace le pion de la case i vers la case j
def move(board,n,i,j):
    i = i-1
    j = j-1
    #on enlève un pion à la source
    board[i]=board[i]-1
    #on ajoute un pion à la destination
    board[j]=board[j]+1

#renvoi true si le jeu est terminé c'est à dire plus aucun pion déplacable
def lose(board,n):
    #si la taille du board est au moins supérieur à 1
    if n >1:
        #pour chaque case du board
        for i in range(1,n):
            #on vérifie si la case contient au moins un pion
            if board[i]>0:
                #si condition valide on retourne false pour signifier que le jeu n'est pas encore terminé et on pourra encore jouer
                return False
     #Si n vaut 1 il n'ya plus rien à faire ou encore toutes les cases du board contiennent zéro
    return True

#affiche le joueur courrant en se basant sur isPlayer 1
def displayGoodplayer(isPlayer1):
    #si c'est le tour du joueur 1 elle affiche Player 1
    if isPlayer1:
        print("Player 1")
    else:
        print("Player 2")


#afficher le joueur perdant en se basant sur isPlayer 1
def displayLoserplayer(isPlayer1):
    #si c'est le tour du joueur 1 alors il a perdu
    if isPlayer1:
        print("Player 1 losed !")
    else:
        print("Player 2 losed ")

#combiner toutes les fonctions pour faire le jeu
def nimble(n,p):
    #si c'est le tour du joueur 1 alors isplayer 1 = True
    isplayer1=True
    # récuperer la liste de board
    board = newBoard(n, p)

    #récuperer l'état du jeu c'est à dire possible de jouer pour False ou non pour True
    islosed=lose(board,n)

    #tester si le jeu n'est pas encore perdu
    while islosed==False:
        #afficher le board
        display(board,n)
        #on affiche le bon joueur
        displayGoodplayer(isplayer1)
        #demander la source : c'est la case d'ou on souhaite prendre le pion
        i = selectSquare(board,n)
        #on demande la destination du pion et on récupère sa valeur
        j = selectDestination(board,n,i)
        #on effectue le déplacement
        move(board,n,i,j)
        #récuperer l'état du jeu
        islosed=lose(board,n)
        #changer le joueur
        if isplayer1:
            isplayer1=False
        else:
            isplayer1=True

    # afficher le board
    display(board, n)
    #afficher
    displayLoserplayer(isplayer1)


#creer une fonction main pour compiler le programma
def main():
    n = 6
    p = 3
    #i = 4
    #j = 2
    #récuperer la liste de board
    #board= newBoard(n,p)
    #afficher le plateau
    #display(board,n)
    #print(possibleSquare(board,n,i))
    #print("la case entrée est : {}".format(selectSquare(board,n)))
    #print(possibleDestination(board,n,i,j))
    #print("la case entrée est : {}".format(selectDestination(board,n,i)))

    #demarrer le jeu
    nimble(n,p)

#choisir la fonction qui doit ètre exécutée
if __name__ == '__main__':main()
