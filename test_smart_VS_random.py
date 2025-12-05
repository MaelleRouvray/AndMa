# test avec un agent random VS un agent smart
import random_agent as rd_ag
import smart_agent as sm_ag

from pettingzoo.classic import connect_four_v3

def multi_play(num_games): 
    """
        Renvoie les statistiques sur les parties jouées

    Parameters:
        num_games : nombre de parties à jouer

    Returns:
        vic_player0 : nombre de victoires du joueur0
        vic_player1 : nombre de victoires du joueur1
        list_coups : liste contenant le nombre de coups joués pour chaque partie
        egalite : nombre de matchs nuls
        
    """
    vic_player0 = 0
    vic_player1 = 0
    egalite = 0
    list_coups = []
    board_echec = []
    global_stats = {"win":0, "block":0,"centre":0, "random":0}

    ind=[]###

    for i in range(num_games):
        nb_coups = 0

        env = connect_four_v3.env(render_mode=None) # ou render_mode="rdb_array" ou bien None
        env.reset(seed=42)

        player0 = rd_ag.RandomAgent(env,"player_0")
        player1 = sm_ag.SmartAgent(env,"player_1")

        agents = {"player_0": player0,"player_1": player1}

        for agent in env.agent_iter():
            observation, reward, termination, truncation, info = env.last()
            board = observation["observation"]

            if termination or truncation:
                action = None
                if reward == 1:
                    print(f"{agent} wins!")
                    print("###########################")
                    print(i+1)
                    if agent == "player_0" : 
                        vic_player0 +=1
                        ind.append(i) ###
                        board_echec.append(board[:,:,0].copy())
                        board_echec.append(board[:,:,1].copy())
                    else :
                        vic_player1 +=1

                    
                elif reward == 0:
                    print("It's a draw!")
                    egalite += 1
            else:
                # Take a random valid action
                action_mask = observation["action_mask"]
                if agent == "player_0":
                    action = agents[agent].choose_action_manual(observation, reward, termination, truncation, info, action_mask)
                if agent == "player_1":
                    action = agents[agent].choose_action(observation, reward, termination, truncation, info, action_mask)
                print(f"{agent} plays column {action}")
                nb_coups += 1

            env.step(action)
        for k in global_stats :
            global_stats[k] += player1.stats[k]
            

        #input("Press Enter to close...")
        env.close()
        # le test s'effectue bien sans problèmes , une partie se terrmine en peu de coups (environ 10 coups par joueur)
        list_coups.append(nb_coups)
    print(f"nb victoires player0 : {vic_player0}, nb victoires player1 : {vic_player1},nb de coups par partie : {list_coups} , nb de matchs nuls : {egalite}, ind={ind}")
    print("Efficacité de la stratégie : ", global_stats)
    return vic_player0, vic_player1, list_coups, egalite, board_echec

#print(multi_play(100))
vic_player0, vic_player1, list_coups, egalite, board_echec = multi_play(100)

new_board_echec = []
for i in range (len(board_echec)):
    if i%2 == 1 :  # impair
        board_echec[i][board_echec[i] == 1] = 2
        new_board_echec.append(board_echec[i-1]+board_echec[i])
print(new_board_echec)
#print(board_echec)