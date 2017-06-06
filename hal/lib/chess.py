# -*- coding: utf-8 -*-

import re
import random

import chess
from hal.library import HalLibrary


class ChessLib(HalLibrary):
    """
    Chess library
    """

    name = "Chess"
    keywords = ["chess"]

    board_regex = re.compile(
        "(chess).*", re.IGNORECASE)
    chess_regex = re.compile(
        "(play chess).*(white|black)", re.IGNORECASE)
    move_regex = re.compile(
        "(move)\s(\w+)", re.IGNORECASE)


    def init(self):
        pass

    def get_next_move(self, board):
        moves = [m for m in board.legal_moves]
        move = random.choice(moves)
        return move

    def save_board(self, board):
        try:
            with open("data/board.sav", "w") as f:
                f.write(board.fen())
        except:
            # Fail Silently
            pass

    def load_board(self):
        try:
            data = ""
            with open("data/board.sav", "r") as f:
                data = f.read()
            board = chess.Board(data)
            return board
        except:
            board = chess.Board()
            # self.save_board(board)
            return board

    def process_input(self):
        if self.match_and_reduce(self.board_regex):
            try:
                # Try starting a new chess game
                board = self.load_board()
                self.add_response(str(board))
                self.status = self.SUCCESS
            except:
                # Could Not Start, Fail Silently
                pass

        if self.match_and_reduce(self.chess_regex):
            expression = self.last_matched.groups()[1].lower()
            if expression is not None:
                try:
                    # Try starting a new chess game
                    board = chess.Board()
                    hal_move = ""
                    if expression == "black":
                        move = self.get_next_move(board)
                        hal_move = board.san(move)
                        board.push(move)
                    self.save_board(board)
                    self.add_response(str(board))
                    self.add_response("=" * 20)
                    self.add_response("YOU:")
                    self.add_response("=" * 20)
                    self.add_response("HAL: " + hal_move)
                    self.status = self.SUCCESS
                except Exception as e:
                    print(e)
                    # Could Not Start, Fail Silently
                    pass

        if self.match_and_reduce(self.move_regex):
            expression = self.last_matched.groups()[1]
            if expression is not None:
                try:
                    # Try loading a saved game
                    board = self.load_board()
                    board.push_san(expression)
                    if board.is_stalemate():
                        self.add_response(str(board))
                        self.add_response("=" * 20)
                        self.add_response("STALEMATE")
                    elif board.is_checkmate():
                        self.add_response(str(board))
                        self.add_response("=" * 20)
                        self.add_response("CHECKMATE, YOU WON!")
                    else:
                        move = self.get_next_move(board)
                        hal_move = board.san(move)
                        board.push(move)
                        if board.is_stalemate():
                            self.add_response(str(board))
                            self.add_response("=" * 20)
                            self.add_response("STALEMATE")
                        elif board.is_checkmate():
                            self.add_response(str(board))
                            self.add_response("=" * 20)
                            self.add_response("CHECKMATE, HAL WON!")
                        self.add_response(str(board))
                        self.add_response("=" * 20)
                        self.add_response("YOU: " + expression)
                        self.add_response("=" * 20)
                        self.add_response("HAL: " + hal_move)
                    self.save_board(board)
                    self.status = self.SUCCESS
                except:
                    self.add_response("Illegal Move: " + expression)
                    self.status = self.SUCCESS

    def process(self):
        pass

    @classmethod
    def help(cls):
        return {
            "name": "Chess",
            "description": "Play chess with HAL.",
            "samples": [
                    "play chess",
                    "play chess black",
                    "chess",
                    "move e4",
                    "move Qxf7",
            ]
        }
