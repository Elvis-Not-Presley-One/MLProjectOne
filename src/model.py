import os
import random
import csv
import copy

import src.game_rules as game_rules

class Model:

    def __init__(self, epsilon, fixed_eval_constants = None, x_player = True):
        """
        This is the constructor of the model

        :param epsilon: the value used in the LMS algorithm
        :param fixed_eval_constants: fixed constants representing fixed weights
        :param x_player: if the model is player x
        """
        self.ep = epsilon
        self.weights = [random.random() for _ in range(9)]
        self.player_x = x_player
        self.eval_constants = fixed_eval_constants


    @staticmethod
    def get_board_features(board) -> list[int]:
        """
        This function gets all the board_features

        :param board: a 3x3 matrix representing the board
        :return: a list of int values representing the board_features
        """

        #x = 1, o = -1
        player = [1,-1]
        corner = [board[0][0], board[0][2], board[2][0], board[2][2]]
        """
        X1: # of X in center 
	    X2: # of O in center 
	    X3: # of O occupied corners 
        X4: # of X occupied corners 
        X5: # of X two in a row with an empty third
        X6: # of O two in a row with empty third
        X7: # of X one in a row with two empty spots
	    X8: # of O one in a row with two empty spots

        """
        board_features = {'x1':0,
                          'x2':0,
                          'x3':0,
                          'x4':0,
                          'x5':0,
                          'x6':0,
                          'x7':0,
                          'x8':0}
        # x1, x2
        if board[1][1] == 1:
            board_features['x1'] = 1
        elif board[1][1] == -1:
            board_features['x2'] = 1

        #x3, x4
        for value in corner:
            if value == -1:
                board_features['x3'] += 1
            if value == 1:
                board_features['x4'] += 1

        # x5, x6, x7, x8
        for row in board:
            if 0 in row:
                if row.count(0) == 1 and 1 in row:
                    board_features['x5'] += 1
                elif row.count(0) == 1 and -1 in row:
                    board_features['x6'] += 1
                elif row.count(0) == 2 and 1 in row:
                    board_features['x7'] += 1
                elif row.count(0) == 2 and -1 in row:
                    board_features['x8'] += 1

        return list(board_features.values())

    def view_weights(self):
        """
        This function prints the weights of the model for debugging
        :return: the list of weights printed
        """
        return print(self.weights)

    def v_hat_calc(self, features) -> float:
        """
        This function calculates the value of v_hat

        :param features: list of int values representing the board_features
        :return: a float value representing the v_hat
        """
        return (self.weights[0] +
                self.weights[1] * features[0] +
                self.weights[2] * features[1] +
                self.weights[3] * features[2] +
                self.weights[4] * features[3] +
                self.weights[5] * features[4] +
                self.weights[6] * features[5] +
                self.weights[7] * features[6] +
                self.weights[8] * features[7])

    @staticmethod
    def fixed_v_hat_calc(fixed_weights, features) -> float:

        return (fixed_weights[0] +
                fixed_weights[1] * features[0] +
                fixed_weights[2] * features[1] +
                fixed_weights[3] * features[2] +
                fixed_weights[4] * features[3] +
                fixed_weights[5] * features[4] +
                fixed_weights[6] * features[5] +
                fixed_weights[7] * features[6] +
                fixed_weights[8] * features[7])

    def predict_move(self, board) -> list[list[int]] | None:
        """
        This function finds the best move given the current board

        :param board: a 3x3 matrix representing the board
        :return: the new board with the best move applied
        """
        legal_moves = game_rules.get_legal_moves(board)

        v_hat_moves = {}

        if not legal_moves:
            return None

        for new_move in legal_moves:
            board_copy = copy.deepcopy(board)
            new_board = game_rules.apply_move(board_copy, new_move)
            features = self.get_board_features(new_board)
            v_hat = self.v_hat_calc(features)
            v_hat_moves[new_move] = v_hat

        best_move = max(v_hat_moves, key=v_hat_moves.get)

        return best_move

    def lms(self, features, target) -> None:
        """
        This function updates the weights of the model

        :param features: the list of int values representing the board_features
        :param target: v_train_b
        :return: NONE
        """
        v_hat = self.v_hat_calc(features)

        error = target - v_hat
        for i in range(len(features)):
            self.weights[i] += features[i] * self.ep * error

    def save_model(self) -> None:
        """
        This function saves the weights of the model
        :return: None
        """

        cwd_path = os.getcwd()
        parent = os.path.dirname(cwd_path)
        data_dir = os.path.join(parent, 'csv')

        try:
            with open(os.path.join(data_dir,'model_weights.csv'), 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(self.weights)
        except IOError:
            print('File not found. Please try again.')

