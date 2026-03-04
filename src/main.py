import os
import random

import logs.log_utils as logs
import src.model as model
import src.game_rules as game_rules
import graphs.graphs as graph


def train_model(num_of_games) -> None:
    """
    this function is the logic that trains the model
    :param num_of_games: the number of games to train on
    :return: NONE
    """

    # if the user inputs the neg or 0 games we dont break the program
    if num_of_games <= 0:
        print("ERROR: num_of_games must be greater than 0")
        return None

    # get the directory of the project in any os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir_csv = os.path.join(base_dir, 'csv')

    sum_games_won = 0
    sum_games_lost = 0
    sum_games_draw = 0

    # create both models
    fixed_eval_const = [.25,.24,.35,.78,.125,.89,.678,.34,.66]
    learner = model.Model(0.4)
    opponent = model.Model(0.4, fixed_eval_const, x_player = False)


    #game loop
    for game in range(num_of_games):
        board = game_rules.create_board()
        o_start = random.random() < .5

        # if o starts they need to move first
        # usually in tic tac toe x always goes first but for the simulation we can change that rule so the
        # model can train on first move or second move
        if o_start:
            move = opponent.predict_move(board)
            board = game_rules.apply_move(board, move, x_player = False)

        prev_feat = None
        game_not_done = True

        # current game loop
        while game_not_done:
            # given the current board find the best move and apply it
            features = learner.get_board_features(board)

            move = learner.predict_move(board)
            new_board = game_rules.apply_move(board, move)

            result = game_rules.win_check(new_board)

            # update the weights after every move
            if prev_feat is not None:
                target = learner.v_hat_calc(features)
                learner.lms(prev_feat, target)

            # if the board is terminal, update the weights and save the weights
            if result is not None:
                terminal = 100 if result == 1 else -100 if result == -1 else 0
                learner.lms(features, terminal)
                learner.save_model()

                if terminal == 100:
                    sum_games_won += 1

                elif terminal == -100:
                    sum_games_lost += 1

                else:
                    sum_games_draw += 1

                #get the percentages from the game and send them to the correct csv
                total_games_done = sum_games_won + sum_games_lost + sum_games_draw

                percent_wins = (sum_games_won / total_games_done) * 100
                percent_lost = (sum_games_lost / total_games_done) * 100
                percent_draw = (sum_games_draw / total_games_done) * 100

                logs.to_csv(os.path.join(data_dir_csv, 'wins.csv'), [total_games_done, round(percent_wins, 2)])
                logs.to_csv(os.path.join(data_dir_csv, 'losses.csv'), [total_games_done, round(percent_lost, 2)])
                logs.to_csv(os.path.join(data_dir_csv, 'draws.csv'), [total_games_done, round(percent_draw, 2)])

                # print out each game so you can see the progress
                print(f"Game: {total_games_done} | Model: {terminal} | Wins: {round(percent_wins, 1)}%, "
                      f"Losses: {round(percent_lost, 1)}%, Draws: {round(percent_draw, 1)}%")

                game_not_done = False
            # if the game is not over and its o turn
            else:

                #find the best move but dont update the weights since its a fixed weights
                prev_feat = features

                move = opponent.predict_move(new_board)
                board = game_rules.apply_move(new_board, move, x_player=False)

                result = game_rules.win_check(board)

                # if the board is terminal add to the sum
                if result is not None:
                    terminal = 100 if result == 1 else -100 if result == -1 else 0
                    learner.lms(features, terminal)

                    if terminal == 100:
                        sum_games_won += 1

                    elif terminal == -100:
                        sum_games_lost += 1

                    else:
                        sum_games_draw += 1

                    # calc the percent of the game
                    total_games_done = sum_games_won + sum_games_lost + sum_games_draw

                    percent_wins = (sum_games_won / total_games_done) * 100
                    percent_lost = (sum_games_lost / total_games_done) * 100
                    percent_draw = (sum_games_draw / total_games_done) * 100

                    # send off to a csv to save the info to create a graph later
                    logs.to_csv(os.path.join(data_dir_csv, 'wins.csv'), [total_games_done, round(percent_wins, 2)])
                    logs.to_csv(os.path.join(data_dir_csv, 'losses.csv'), [total_games_done, round(percent_lost, 2)])
                    logs.to_csv(os.path.join(data_dir_csv, 'draws.csv'), [total_games_done, round(percent_draw, 2)])

                    # print out each game to see whats going on
                    print(f"Game: {total_games_done} | Model: {terminal} | Wins: {round(percent_wins, 1)}%, "
                          f"Losses: {round(percent_lost, 1)}%, Draws: {round(percent_draw, 1)}%")

                    game_not_done = False

    # get the final total percentages and print them out
    total_games_done = sum_games_won + sum_games_lost + sum_games_draw

    percent_wins = (sum_games_won / total_games_done) * 100
    percent_lost = (sum_games_lost / total_games_done) * 100
    percent_draw = (sum_games_draw / total_games_done) * 100

    print("\n====================================================================================" * 5)
    print("\n                                summary                                            ")
    print("===================================================================================")
    print(f"Percent of Games Won: {round(percent_wins, 1)}% | Number of Games Won: {sum_games_won}")
    print(f"Percent of Games Lost: {round(percent_lost, 1)}% | Number of Games Lost: {sum_games_lost}")
    print(f"Percent of Games Draw: {round(percent_draw, 1)}% | Number of Games Drew: {sum_games_draw}")
    print("===================================================================================")

    return None

if __name__ == "__main__":
    # get the correct directories for any os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir_graph = os.path.join(base_dir, 'graphs')
    data_dir_csv = os.path.join(base_dir, 'csv')


    num_games = input("Enter number of games to train on: ")

    print("\n                           Current Progress                                            ")
    print("====================================================================================\n")

    train_model(int(num_games))

    print("\n====================================================================================\n")
    create_graph = input("\nWould you like to create graph? (y/n): ")
    print("\n====================================================================================\n")

    # if the user wants graphs then create the graphs
    if create_graph == "y":

        # wins graph
        graph.create_graph(os.path.join(data_dir_csv,'wins.csv'),
                           os.path.join(data_dir_graph, 'figures'),
                           "Percent of Games Won Vs. Number of Games",
                           "Percent of Games Won")

        # lost Graph
        graph.create_graph(os.path.join(data_dir_csv, 'losses.csv'),
                           os.path.join(data_dir_graph, 'figures'),
                           "Percent of Games Lost Vs. Number of Games",
                           "Percent of Games Lost")

        # drawn graph
        graph.create_graph(os.path.join(data_dir_csv, 'draws.csv'),
                           os.path.join(data_dir_graph, 'figures'),
                           "Percent of Games Drawn Vs. Number of Games",
                           "Percent of Games Drawn")

        print("Graphs created in figures")

