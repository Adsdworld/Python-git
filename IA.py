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
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=1.0): #
        self.epsilon = epsilon  # 
        self.alpha = alpha  # 
        self.gamma = gamma  # 
        self.q = {}  # 

    def get_state(self, board): #
        return str(board)

    def get_legal_moves(self, board): # retourne une liste de positions libre ex: [2, 3, 6, 9]
        return [i+1 for i, x in enumerate(board) if x == " "]
    
    def choose_action(self, board): # regarde si il y a une implication sinon 
        win_or_necessary_position= self.win_or_necessary_position(board)
        if None != win_or_necessary_position:
            return win_or_necessary_position
        if random.uniform(0, 1) < self.epsilon:
            random_max_indices = random.choice(self.get_legal_moves(board))
        else:
            state = self.get_state(board)
            if state not in self.q:
                self.q[state] = [0] * 9
            max_value = max(self.q[state])
            max_indices = [i for i, v in enumerate(self.q[state]) if v == max_value]
            random_max_indices = random.choice(max_indices)
        if ("O" != board[random_max_indices-1] and "X" != board[random_max_indices-1]):
            return random_max_indices
        else:
            return self.choose_action(board)

    def learn(self, state, action, reward, next_state): #
        if action < 0 or action > 8:
            return
        if next_state not in self.q:
            self.q[next_state] = [0] * 9
        td_target = reward + self.gamma * max(self.q[next_state])
        td_error = td_target - self.q[state][action]
        self.q[state][action] += self.alpha * td_error
    
    def win_or_necessary_position(self, board): # vérifier si une position sur le morpion est gagnante
        for i in self.get_legal_moves(board):
            j=board[i-1]
            board[i-1] = 'X'
            if check_win(board) == 'X':
                return i
            board[i-1]=j
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

def play_game(agent): # fait jouer l'agent
    board = [" "]*9
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



"""if __name__ == "__main__":
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

"""