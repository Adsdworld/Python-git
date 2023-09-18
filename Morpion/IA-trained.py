"""
copier le code de l'ai

créer une AI
fcontionne sur un entrainement qui stocke les coups gagnants ou le dernier test null si aucun coup gagnat n'existe

doit intégrer un système de rotation pour que l'IA n'ai que 18 possibilités à tester

pour le centre :
    l'orientation dépends du O du joueur
pour un côté ou un coin l'orientation depend du X de l'ia

L'ia doit choisir aléatoirement selon 3 coups, on définit l'orientation, puis on examine les autres possibilités en les prenants dans l'ordre
la première possibilité gagnate rencontrée est directement stocké dans le dico
si aucune possibilité gagnante n'est rencontré avant la fin, on stocke la dernière possibilité null (attention la dernière possibilité n'est pas forcément la null)

on ajoute la clé lorsque la partie est terminé; si on obtient "gagnante137"=2 on va récupérer le dernier caractère du nom de la clé avec , on ajoute toutes les clés gagnantes dans le dico, il se peut que le joueur bloque une possibilité, donc il faut avoir toutes les possibilités

Format d'une possibilité gagnante : "gagnante137"=2

la clé gagnante devra apparaitre plusieurs fois
Exmple:
"gagnante1"=3
"gagnante13"=7
"gagnante13"=9


nouveau format du dict
t=[..."G137"=2]
ça implique que quand on choisit une position on doit retenir dans une variable nos positions précédantes, pour pouvoir rechercher dans le dico le postentiel coup gagant à condition que la position soit libre
"""

"""cré une ia mémoire

montrer l'avancé des coups sur une seule ligne

réviser et comprendres les récompenses"""

import random
from time import sleep
import os

msg_game_launch=":D Faisons un Morpion! :D"
msg_game_agent="Voici le choix de L'IA"
msg_game_input="Choisissez un nombre de 1 à 9"
msg_game_input_error="Vous devez choisir un nombre de 1 à 9"
msg_game_invalid_input="Cette position est déjà occupé"
msg_except_error="Une erreur est survenue"
msg_game_is_not_winable=":/ La partie n'est pas gagnable :/"
msg_game_win="Félicitations, le gagnant est"
msg_game_null="Match null ! Bravo"
var_time_to_sleep_after_agent_choice=1


class Agent:
    def __init__(self, d={}): #
        self.d = d  # définir le dictionnaire dans l'Agent

    def get_state(self, board): #
        return str(board)

    def get_legal_moves(self, board): # retourne une liste de positions libre ex: [2, 3, 6, 9]
        return [i+1 for i, x in enumerate(board) if x == " "]        

    def learn(self, state, action, reward, next_state): #
        if action < 0 or action > 8:
            return
        if next_state not in self.q:
            self.q[next_state] = [0] * 9
        td_target = reward + self.gamma * max(self.q[next_state])
        td_error = td_target - self.q[state][action]
        self.q[state][action] += self.alpha * td_error
    
    def win_position(self, board): # vérifier si une position sur le morpion est gagnante
        for i in self.get_legal_moves(board):
            j=board[i-1]
            board[i-1] = 'X'
            if check_win(board) == 'X':
                return i
            board[i-1]=j
        return None
    def necessary_position(self, board): # vérifier si une position sur le morpion est nécessaire
        for i in self.get_legal_moves(board):
            j=board[i-1]
            board[i-1] = 'O'
            if check_win(board) == 'O':
                return i
            board[i-1]=j
        return None
        
def win(board, player): # vérifier si un player à gagné
    if check_win(board) == player:
            print(msg_game_win+" {}".format(player))
            return False
    return True
    
def match_null(board): # vérifie si la partie est nulle
    if " " in board:
        return True
    else:
        print(msg_game_null)
        return False

def print_board(board):
    print("-------------\n| " + board[0] + " | " + board[1] + " | " + board[2] + " |\n-------------\n| " + board[3] + " | " + board[4] + " | " + board[5] + " |\n-------------\n| " + board[6] + " | " + board[7] + " | " + board[8] + " |\n-------------")

def check_winnable(board): # vérifier si une partie est gagnable
    for i in range(0, 9, 3): # vérifier les lignes
        if board[i:i+3] == ["X", "X", " "] or board[i:i+3] == ["O", "O", " "]:
            return True
        if board[i:i+3] == ["X", " ", "X"] or board[i:i+3] == ["O", " ", "O"]:
            return True
        if board[i:i+3] == [" ", "X", "X"] or board[i:i+3] == [" ", "O", "O"]:
            return True
    
    for i in range(3): # vérifier les colonnes
        if [board[i], board[i+3], board[i+6]] == ["X", "X", " "] or [board[i], board[i+3], board[i+6]] == ["O", "O", " "]:
            return True
        if [board[i], board[i+3], board[i+6]] == ["X", " ", "X"] or [board[i], board[i+3], board[i+6]] == ["O", " ", "O"]:
            return True
        if [board[i], board[i+3], board[i+6]] == [" ", "X", "X"] or [board[i], board[i+3], board[i+6]] == [" ", "O", "O"]:
            return True
    
    # Vérifier les diagonales
    if [board[0], board[4], board[8]] == ["X", "X", " "] or [board[0], board[4], board[8]] == ["O", "O", " "]:
        return True
    if [board[0], board[4], board[8]] == ["X", " ", "X"] or [board[0], board[4], board[8]] == ["O", " ", "O"]:
        return True
    if [board[0], board[4], board[8]] == [" ", "X", "X"] or [board[0], board[4], board[8]] == [" ", "O", "O"]:
        return True
    if [board[2], board[4], board[6]] == ["X", "X", " "] or [board[2], board[4], board[6]] == ["O", "O", " "]:
        return True
    if [board[2], board[4], board[6]] == ["X", " ", "X"] or [board[2], board[4], board[6]] == ["O", " ", "O"]:
        return True
    if [board[2], board[4], board[6]] == [" ", "X", "X"] or [board[2], board[4], board[6]] == [" ", "O", "O"]:
        return True
    print(msg_game_is_not_winable)
    return False

def check_win(board): # vérifie si quelqu'un à gagné
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    return "N"

def position_input(): # choix du player humain
    while True:
        try:
            n = int(input("Choose your move (1-9): ")) - 1
            if -1<n<9:
                return n 
        except:
            print(msg_except_error)
        print(msg_game_input_error)

def play_against_human2(agent, player): # jouer contre l'IA
    print(msg_game_launch)
    board = [" "] * 9
    play=True
    print_board(board)
    if player == "X": # L'IA commence
        while play:
            # L'IA joue
            agent_move = agent.choose_action(board)
            board[agent_move-1] = 'X'
            print(msg_game_agent)
            print_board(board)
            if False == win(board, "X") or False == match_null(board):
                play = False

            if play==True:
                # L'humain joue
                human_move = position_input()
                if board[human_move] != " ":
                    print(msg_game_invalid_input)
                    continue
                board[human_move] = 'O'
                print_board(board)
                if False == win(board, "O") or False == match_null(board):
                    play = False
                sleep(var_time_to_sleep_after_agent_choice)
    else: # L'humain commence
        while play:
            # L'humain joue
            human_move = position_input()
            if board[human_move] != " ":
                print(msg_game_invalid_input)
                continue
            board[human_move] = 'O'
            print_board(board)
            if False == win(board, "O") or False == match_null(board):
                play = False
            sleep(var_time_to_sleep_after_agent_choice)

            if play==True:
                # L'IA joue
                agent_move = agent.choose_action(board)
                board[agent_move-1] = 'X'
                print(msg_game_agent)
                print_board(board)
                if False == win(board, "X") or False == match_null(board):
                    play = False


def train_agent(agent): # fait jouer l'agent
    for i in range(3):
        if i == 0:
            board = [" "]*9
            board[5-1] = "X" # L'Agent joue
            adversaire_moves1=Agent().get_legal_moves
            for j in adversaire_moves1:
                    board[j-1] = "O" # L'adversaire joue parmis la liste des positions possibles
                    # on verifie si une position est gagnate
                    # sinon :
                        # on vérifie si une position est nécessaire
                        # sinon on prends une position possibles une fois que l'adversaire à joué
                    win_position = Agent().win_position(board)
                    if None != win_position:
                        board[win_position-1] = "X" 
                        # crer une fonction qui ajoute au dico i, j, win_position
                    else:
                        necessary_position = Agent().necessary_position(board)
                        if None != necessary_position:
                            board[necessary_position-1] = "X" 
                        else:
                            agent_moves2=Agent().get_legal_moves(board)
                            for p in agent_moves2:
                                board[p-1] = "X" 

                                adversaire_moves2=Agent().get_legal_moves
                                for l in adversaire_moves2:
                                        board[l-1] = "O" # L'adversaire joue parmis la liste des positions possibles
                                        # on verifie si une position est gagnate
                                        # sinon :
                                            # on vérifie si une position est nécessaire
                                            # sinon on prends une position possibles une fois que l'adversaire à joué
                                        win_position = Agent().win_position(board)
                                        if None != win_position:
                                            board[win_position-1] = "X" 
                                            # crer une fonction qui ajoute au dico i, j, win_position
                                        else:
                                            necessary_position = Agent().necessary_position(board)
                                            if None != necessary_position:
                                                board[necessary_position-1] = "X" 
                                            else:
                                                agent_moves3=Agent().get_legal_moves(board)
                                                for q in agent_moves3:
                                                    board[q-1] = "X" 

                                                    adversaire_moves3=Agent().get_legal_moves
                                                    for m in adversaire_moves3:
                                                            board[m-1] = "O" # L'adversaire joue parmis la liste des positions possibles
                                                            # on verifie si une position est gagnate
                                                            # sinon :
                                                                # on vérifie si une position est nécessaire
                                                                # sinon on prends une position possibles une fois que l'adversaire à joué
                                                            win_position = Agent().win_position(board)
                                                            if None != win_position:
                                                                board[win_position-1] = "X" 
                                                                # crer une fonction qui ajoute au dico i, j, win_position
                                                            else:
                                                                necessary_position = Agent().necessary_position(board)
                                                                if None != necessary_position:
                                                                    board[necessary_position-1] = "X" 
                                                                else:
                                                                    agent_moves4=Agent().get_legal_moves(board)
                                                                    for r in agent_moves4:
                                                                        board[r-1] = "X" 

                                                                        adversaire_moves4=Agent().get_legal_moves
                                                                        for o in adversaire_moves4:
                                                                                board[o-1] = "O" # L'adversaire joue parmis la liste des positions possibles
                                                                                # on verifie si une position est gagnate
                                                                                # sinon :
                                                                                    # on vérifie si une position est nécessaire
                                                                                    # sinon on prends une position possibles une fois que l'adversaire à joué
                                                                                win_position = Agent().win_position(board)
                                                                                if None != win_position:
                                                                                    board[win_position-1] = "X" 
                                                                                    # crer une fonction qui ajoute au dico i, j, win_position
                                                                                else:
                                                                                    necessary_position = Agent().necessary_position(board)
                                                                                    if None != necessary_position:
                                                                                        board[necessary_position-1] = "X" 
                                                                                    else:
                                                                                        agent_moves5=Agent().get_legal_moves(board)
                                                                                        for s in agent_moves5:
                                                                                            board[s-1] = "X" 
                                                                                            




        elif (i == 1):
            board = [" "]*9
            board[6-1] = "X"
        elif (i == 2):
            board = [" "]*9
            board[3-1] = "X"
        else:
            print("i != 0, 1, 2")
    while True:
        # L'IA joue
        action = agent.choose_action(board)
        board[action-1] = "X"
        reward = 1
        winner = check_win(board)
        if winner == "X":
            reward = 5
        elif winner == "O":
            reward = -100
        elif winner == "tie":
            reward = 3
        agent.learn(str(board), action, reward, str(board))
        if winner:
            break

        # Random joue
        legal_moves = agent.get_legal_moves(board)
        if not legal_moves:
            break
        action = random.choice(legal_moves)
        board[action-1] = "O"
        winner = check_win(board)
        if winner == "O":
            reward = -100
        elif winner == "X":
            reward = 5
        elif winner == "tie":
            reward = 3
        agent.learn(str(board), action, reward, str(board))
        if winner:
            break
    return winner

def print_q_dict(q_dict):
    for key, value in q_dict.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    # clear the console screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("***")
    print("Loading.")
    training=10000
    for i in range(training):
        play_game(Agent())
        if (i==(training/2)):
            print("Loading..")
    print("Loading...")
    while True:
        if 0==random.randint(0,1):
            player="O"
        else:
            player="X"
        player="X"
        print("***")
        print("Nouvelle Partie")
        play_against_human2(Agent(), player)
        print("Partie terminé")

