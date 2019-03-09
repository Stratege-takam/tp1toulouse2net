


import sys;

#importation de la bibliothèque pour générer un nombre aléatoire
from random import randint




#board: liste contenant les pionts du plateau
#n = len(board)
#p = max de piont pouvant contenir une case à l'initialisation
#i et j = deux entiers quelconques permettant de parcourir notre board
#player = 'o' pour le joueur de pion noir et 'x' pour le joueur de pion blanc

#initialiser le tableau
def newBoard(n):
    board=[[0]* n for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            #si on est à la colonne 1 ou on est à la dernière ligne , la case de board sera "x" sauf la dernière colonne de la dernière ligne ou encore la dernière cellule
            if j == 0 or i == (n-1) and j < n-1:
                board[i][j] = 'x'
            #si on est à la 1ère ligne ou la dernière colonne alors la case de board sera "o"
            elif i == 0 or j == (n-1):
                board[i][j] = 'o'
            #dans le cas contraire la case de board sera "."
            else:
                board[i][j]='.'
    return board

#afficher board
def display(board,n):
    #parcourir les lignes du board
    for i in range (0,n):
        #parcourir les colonnes
        for j in range(0,n):
            #pour chaque valeure afficher le board [i] [j] et ajouter une tabulation
            print("{}".format(board[i][j]), end="\t")
        #ajouter un saut de ligne pour la prochaine ligne
        print("")


# qui retourne True si i et j sont les coordonnées d’un pion que le joueur player peut déplacer, et False sinon.
#pour qu'un pion soit deplacable il faut que la case de prêt soit au moins libre cette case peut être à gauche du pion ou à droite sur l'axe
#horizontal ou à en haut ou en bas sur laxe vertical une case est libre si elle contien '.'
#il faut aussi que le pion courant soit pour le joeur
def possiblePawn(board, n, player, i, j):

    i = i - 1
    j = j - 1
    #si le numero du pion n'est pas dans l'interval du jeu ou encore le pion n'appartient pas au joueur alors on renvoi false
    if i < 0 or i >= n or j < 0 or j >= n or not (board[i][j] in player):
        #print(board[i][j] in player)
        #print("bad 1 player={}, n={},  board[{}][{}]={}".format(player, n, i, j, board[i][j]))
        return False
    # tester le deplacement sur l'axe vertical
    #si  c'est possible de deplacer le poin vers le haut
    if (i-1) >= 0 and (board[i-1][j] in '.'):
        return True
    #si c'est possible de déplacer le pion vers le bas
    if (i+1) < n and (board[i+1][j] in '.'):
        return True
    # tester le deplacement sur l'axe horizontal
    # si  c'est possible de deplacer le poin vers la gauche
    if (j - 1) >= 0 and (board[i][j - 1] in '.'):
        return True
    # si c'est possible de déplacer le pion vers la droite
    if (j + 1) < n and (board[i][j + 1] in '.'):
        return True
    #print("bad 2 {}".format(player))
    #si aucun cas n'est vérifié on doit retourner false
    return False

#saisir les coordonnées aussi longtemps que ce ne soit pas valide on
# lui demande de resaisir à nouveau
def selectPawn(board,n,player):
    #on attribut les faussas valeurs a i et a j
    j = -1
    i = -1
    # si les conditions du jeu ne sont respectés
    while possiblePawn(board, n, player, i, j) is False:
        i = eval(input("Select a pawn, row : "))
        j = eval(input("Select a pawn, column : "))

    #si tout est ok alors on retourne un tuple de coordonnée i,j
    return (i, j)

# où l’on suppose ici que i et j sont les coordonnées d’un pion pouvant
#  se déplacer. Cette fonction retourne True si k et l sont les coordonnées
# d’une case vers laquelle le pion
# de coordonnées i et j peut se déplacer, et False sinon.
def possibleDestination(board,n,i,j,k,l):
    i = i - 1
    j = j - 1
    k = k - 1
    l = l - 1
    #si on veux realiser un deplacement sur l'axe vertical, il faut que si k est
    # inferieur à i alors on verifie qu'il n'y a aucun pion entre i et k ensuite
    # que k est plus grand que ou egale 0
    if i > k >= 0 and j is l:
        if k is (i-1):
            if not (board[k][j] in '.'):
                return False
            return True
        for p in range(k, i):
            if not (board[p][j] in '.'):
                return False
        return True
    # si  k est superieur à i, on verifie qu'entre i et k il n'y a aucun pion
    # ensuite que k est plus petit que n
    elif n > k > i and j is l:
        if k is (i + 1):
            if not (board[k][j] in '.'):
                return False
            return True
        for p in range((i+1), k):
            if not (board[p][j] in '.'):
                return False
        return True
        # si on veut realiser un deplacement sur l'axe horisontal, il faut que si l est
        # inferieur à j alors on verifie qu'il n'y a aucun pion entre j et l ensuite
        # que k est plus grand que ou egale 0
    if j > l >= 0 and k is i:
        if l is (j - 1):
            if not (board[i][l] in '.'):
                return False
            return True
        for p in range(l, j):
            if not (board[i][p] in '.'):
                return False
        return True
        # si  l est superieur à j, on verifie qu'entre j et l il n'y a aucun pion
        # ensuite que l est plus petit que n
    elif n > l > j and k is i:
        if l is (j + 1):
            if not (board[i][l] in '.'):
                return False
            return True
        for p in range((j + 1), l):
            if not (board[i][p] in '.'):
                return False
        return True
    #dans le cas contraire on retourne false
    return False

#saisi les coordonnées aussi longtemps que les règles du jeu ne sont pas respectés
def selectDestination(board,n,i,j):
    k = -1
    l = -1

    #tant que condition n'est pas respecté
    while possibleDestination(board,n,i,j,k,l) is False:
        k = eval(input("Select a destination, row"))
        l = eval(input("Select a destination, column"))
    return (k, l)


#realise le deplacement
def move(board,n,player,i,j,k,l):
    i = i - 1
    j = j - 1
    k = k - 1
    l = l - 1
    # on enlève un pion à la source
    board[i][j] = '.'
    # on ajoute un pion à la destination
    board[k][l] = player

# qui retourne False si le joueur player peut déplacer l’un de ses pions et True sinon.
def lose(board,n,player):

    #print("player is : {}".format(player))
    #on parcourt notre board, on verifie s'il y'a au moins 1 pion pour joueur palyer
    for i in range(0, n):
        for j in range(0, n):
            #s'il y a un pion et que le pion est déplacable alors il peut continuer a jouer on retourne false
            #print("({},{}) = {} can play : {}".format(i, j, board[i][j], possiblePawn(board, n, player, (i + 1), (j + 1))))
            if (board[i][j] in player) and possiblePawn(board, n, player, (i + 1), (j + 1)) is True:
                return False
    #si le joueur player n'a plus de pion on retourne true
    return True



#rechercher la position du pion du joueur courant
#on suppose que i la ligne et j la colonne
def getpostionX(board,n,player,i,j,right):
    i = i - 1
    j = j - 1
    #si le deplacement se fait vers la droite
    if right is True:
        # s'il n'y a qu'une case entre le premier et son second pion
        if (j + 1) >= (n-1):
            # on renvoi -1
            return -1
        # on parocurt l'axe horizontal en allant vers la droite
        for p in range((j+1), n):
            #si on trouve le pion du joueur
            if board[i][p] is player:
                #on renvoi la position de son pion
                return p
        #dans le cas contraire on renvoi -1
        return -1
    #si le parourt se fait vers la droite et qu'il n'y a ni le pion precedent ou encore
    #les deux pions du joueurs sont coete a cote
    if (j-1) <= 0:
        #on renvoi -1
        return -1
    #on parcourt les cases du jeu
    for p in range(0, j):
        #si on trouve le prochaine pion du joueur
        if board[i][p] is player:
            #on renvoi la position
            return p
    #on renvoi -1 si aucun pion
    return -1


# rechercher la position du pion du joueur courant
# on suppose que i la ligne et j la colonne
#meme commentaire que le haut
def getpostionY(board, n, player, i, j, bottom):
    i = i - 1
    j = j - 1
    #si le deplacement se fait vers le bas
    if bottom is True:
        if (i + 1) >= (n - 1):
            return -1
        for p in range((i + 1), n):
            if board[p][j] is player:
                return p
        return -1
    #si le deplacement se fait vers le haut
    if (i - 1) <= 0:
        return -1
    for p in range(0, i):
        if board[p][j] is player:
            return p
    return -1



# remplacer tous les pions intrus qui sont coincés sur l'axe vertical
def ReplaceY(board,n,player,i,j,y,bottom):
    cpt = 0
    i = i - 1
    j = j - 1
    #print("position y : {}".format(y))
    #s'il existe au moins pion ou un vide entre les pions de l'utilisateur
    if y >= 0:
        #si le deplacement se fait vers le bas
        if bottom is True:
            #on parcourt chaque case en allant de la première position du pion appartenant
            #au joueur jusqu'au prochaine pion
           for p in range((i+1),y):
               #si le pion existe
               if not (board[p][j] in '.'):
                   #on incremente le compteur
                   cpt  = cpt + 1
            #si  les pions se trouvent effectivement coincés
           #print("position cpt : {} y - j -1 = {} ".format(y, (y - i - 1)))
           if cpt is (y - i - 1):
               #pour chaque pion,  on fait un remplacement
               for p in range((i + 1), y):
                   board[p][j] = player
                #si on remplace on retourne true
               return True
            #sinon false
           return False
        #on fait la meme operation si le deplament vers le haut
        for p in range((y + 1), i):
            if not (board[p][j] in '.'):
                cpt = cpt + 1
        #print("position cpt : {} y - j -1 = {} ".format(y, (i - y - 1)))
        if cpt is (i - y - 1):
            for p in range((y + 1), i):
                board[p][j] = player
            #SI ON REMPLACE on retourne true
            return True
    #si non false
    return False

# remplacer les pions coincés sur l'axe horizontal (le commentaire est le
#  même que sur laxe vertical)
def ReplaceX(board,n,player,i,j,x,right):
    cpt = 0
    i = i - 1
    j = j - 1
    #print("position x : {}".format(x))
    if x >=0:
        #si le deplacement se fait vers la droite
        if right is True:
           for p in range((j+1), x):
               if not (board[i][p] in '.'):
                   cpt  = cpt + 1
           #print("position cpt : {} x - j -1 = {} ".format(x, (x - j - 1)))
           if cpt is (x - j -1):
               for p in range((j + 1), x):
                   board[i][p] = player
               return True
           return False

        for p in range((x + 1) , j ):
            if not (board[i][p] in '.'):
                cpt = cpt + 1
        #print("position cpt : {} x - j -1 = {} ".format(x, (j - x - 1)))
        if cpt is (j - x - 1):
            for p in range((x + 1), j):
                board[i][p] = player
            return True
    return False


#changer le joueur
def changePlayer(lastPlayer):
    #si le joueur de pion noir
    if lastPlayer is 'o':
        #retourner le joueur de pion blanc
        return 'x'
    #retourner le joueur de pion noir
    return 'o'

#gagner une partie
#pour gagner un tour de jeu, une fois que le joueur a éffectué le deplacement,
#on vérifie qu'il n' y a pas de pion croisé. si c'est le cas, le pion est bouffe
#au final il renvoi le prochaine joueur
def GetParty(board,n,player,i,j,k,l):
    # effectuer le deplacement
    move(board, n, player, i, j, k, l)

    x1  = getpostionX(board, n, player, k, l, True)
    x2  = getpostionX(board, n, player, k, l, False)
    y1 = getpostionY(board, n, player, k, l, True)
    y2 = getpostionY(board, n, player, k, l, False)

    #remplacer  sur l'axe horizintal en allant vers la droite
    ReplaceY(board, n, player, k, l, y1, True)
    # remplacer  sur l'axe horizintal en allant vers la gauche
    ReplaceY(board, n, player, k, l, y2, False)

    # remplacer  sur l'axe vertical en allant vers le bas
    ReplaceX(board, n, player, k, l, x1, True)
    # remplacer  sur l'axe vertical en allant vers le haut
    ReplaceX(board, n, player, k, l, x2, False)

    #retourner le prochaine joueur
    return changePlayer(player)



#déclare le perdant
def DeclareLosing(player):
    if player == 'x':
        print("Player 1 losed")
    else:
        print("Player 2 losed")

#déclare le perdant
def showPlayer(player):
    if player == 'x':
        print("Player 1 :")
    else:
        print("Player 2 :")



#realiser le jeu
def mingMang(n):

    #initialiser le board
    board = newBoard(n)

    # dernière joueur (nous permet de declarer le vinqueur du jeu ou le perdant
    # par defaut on suppose que c'est le blanc qui debute le jeu
    lastPlayer = "x"

    #on recupère l'etat du jeu (si c'est possible de jouer True sinon false)
    cannotplay = lose(board, n, lastPlayer)

   # print("etat du jeu {} ".format(cannotplay))

    # afficher le board
    display(board, n)

    #tant que le jeu est possible
    while cannotplay == False:
        #Afficher le joueur
        showPlayer(lastPlayer)

        #on recupere les coordonnées du pion à deplacer
        i,j = selectPawn(board, n, lastPlayer)

        #on recupere les cordonnées de la destination du pion
        k,l = selectDestination(board, n, i, j)

        #on fait jouer le joueur ( le laisser découvrir une partie
        lastPlayer  = GetParty(board, n, lastPlayer, i, j, k, l)

        # on recupère l'etat du jeu (si c'est possible de jouer True sinon false)
        cannotplay = lose(board, n, lastPlayer)

        # afficher le board
        display(board, n)

    #on affiche le perdant
    DeclareLosing(lastPlayer)


#creer une fonction main pour compiler le programma
def main():
    #on suppose que la longueur du board vaux 8
    n = 4

    # on lance le jeu
    mingMang(n)

    # player = 'x'

    # initialiser le board
    #board = newBoard(n)

    # afficher le board
    #display(board, n)

    # on recupere les coordonnées du pion à deplacer
    #i,j = selectPawn(board, n, player)

    # on recupere les cordonnées de la destination du pion
    #k, l = selectDestination(board, n, i, j)

    # effectuer le deplacement
    #move(board, n,  player, i, j, k, l)


    # afficher le board
    #display(board, n)

    #print("({},{}), ({}, {})".format(i, j, k, l))



#choisir la fonction qui doit ètre exécutée
if __name__ == '__main__':main()