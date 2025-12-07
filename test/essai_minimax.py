import smart_agent_pour_test as sm_ag
import minimax_agent as mm_ag

from pettingzoo.classic import connect_four_v3



def run_tournament(num_games):
    vic_player0 = 0
    vic_player1 = 0
    egalite = 0
    list_coups = []
    board_echec = []


    for i in range(num_games):
        nb_coups = 0

        env = connect_four_v3.env(render_mode=None) # ou render_mode="rdb_array" ou bien None
        env.reset(seed=42)

        player0 = sm_ag.SmartAgent(env,player_name="player_0")
        player1 = mm_ag.MinimaxAgent(env,player_name="player_")
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

                    else :
                        vic_player1 +=1

                    
                elif reward == 0:
                    print("It's a draw!")
                    egalite += 1
            else:
                # Take a random valid action
                action_mask = observation["action_mask"]
                action = agents[agent].choose_action(board, reward, termination, truncation, info, action_mask)
                print(f"{agent} plays column {action}")
                nb_coups += 1

            env.step(action)
    

        #input("Press Enter to close...")
        env.close()
        list_coups.append(nb_coups)

    print(f"nb victoires player0 : {vic_player0}, nb victoires player1 : {vic_player1},nb de coups par partie : {list_coups} , nb de matchs nuls : {egalite}")
    return vic_player0, vic_player1, list_coups, egalite


print(run_tournament(10))