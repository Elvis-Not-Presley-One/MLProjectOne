import os
import random

import logs.log_utils as logs
import src.model as model
import src.game_rules as game_rules


def train_model(num_of_games) -> None:
    """
    this function is the logic that trains the model
    :param num_of_games: the number of games to train on
    :return: NONE
    """

    if num_of_games <= 0:
        print("ERROR: num_of_games must be greater than 0")
        return None

    cwd_path = os.getcwd()
    parent = os.path.dirname(cwd_path)
    data_dir = os.path.join(parent, 'csv')

    sum_games_won = 0
    sum_games_lost = 0
    sum_games_draw = 0

    fixed_eval_const = [.25,.24,.35,.78,.125,.89,.678,.34,.66]
    learner = model.Model(0.4)
    opponent = model.Model(0.4, fixed_eval_const, x_player = False)

    for game in range(num_of_games):
        board = game_rules.create_board()
        o_start = random.random() < .5

        if o_start:
            move = opponent.predict_move(board)
            board = game_rules.apply_move(board, move, x_player = False)

        prev_feat = None
        game_not_done = True

        while game_not_done:
            features = learner.get_board_features(board)

            move = learner.predict_move(board)
            new_board = game_rules.apply_move(board, move)

            result = game_rules.win_check(new_board)

            if prev_feat is not None:
                target = learner.v_hat_calc(features)
                learner.lms(prev_feat, target)

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

                total_games_done = sum_games_won + sum_games_lost + sum_games_draw

                percent_wins = (sum_games_won / total_games_done) * 100
                percent_lost = (sum_games_lost / total_games_done) * 100
                percent_draw = (sum_games_draw / total_games_done) * 100

                logs.to_csv(os.path.join(data_dir, 'wins.csv'), [total_games_done, round(percent_wins, 2)])
                logs.to_csv(os.path.join(data_dir, 'losses.csv'), [total_games_done, round(percent_lost, 2)])
                logs.to_csv(os.path.join(data_dir, 'draws.csv'), [total_games_done, round(percent_draw, 2)])

                print(f"Game: {total_games_done} | Model: {terminal} | Wins: {round(percent_wins, 1)}%, "
                      f"Losses: {round(percent_lost, 1)}%, Draws: {round(percent_draw, 1)}%")

                game_not_done = False

            else:

                prev_feat = features

                move = opponent.predict_move(new_board)
                board = game_rules.apply_move(new_board, move, x_player=False)

                result = game_rules.win_check(board)

                if result is not None:
                    terminal = 100 if result == 1 else -100 if result == -1 else 0
                    learner.lms(features, terminal)

                    if terminal == 100:
                        sum_games_won += 1

                    elif terminal == -100:
                        sum_games_lost += 1

                    else:
                        sum_games_draw += 1

                    total_games_done = sum_games_won + sum_games_lost + sum_games_draw

                    percent_wins = (sum_games_won / total_games_done) * 100
                    percent_lost = (sum_games_lost / total_games_done) * 100
                    percent_draw = (sum_games_draw / total_games_done) * 100

                    logs.to_csv(os.path.join(data_dir, 'wins.csv'), [total_games_done, round(percent_wins, 2)])
                    logs.to_csv(os.path.join(data_dir, 'losses.csv'), [total_games_done, round(percent_lost, 2)])
                    logs.to_csv(os.path.join(data_dir, 'draws.csv'), [total_games_done, round(percent_draw, 2)])

                    print(f"Game: {total_games_done} | Model: {terminal} | Wins: {round(percent_wins, 1)}%, "
                          f"Losses: {round(percent_lost, 1)}%, Draws: {round(percent_draw, 1)}%")

                    game_not_done = False

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
    num_games = input("Enter number of games to train on: ")

    print("\n                           Current Progress                                            ")
    print("====================================================================================\n")

    train_model(int(num_games))