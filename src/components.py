import logging
import sys
import tkinter as tk

logging.basicConfig(filename='logs/chessProgramErrors.log',
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

class Board:
    def __init__(self):
        self.tiles = [[None for j in range(0,8)] for i in range(0,8)]

    def __repr__(self):
        return f'Tiles:{self.tiles}'

    def getTiles(self):
        return self.tiles

class Piece:
    def __init__(self, type, position, color):
        self.position = position
        self.type = type
        self.color = color
        self.moveList = []
        self.availableTiles = []

    def __repr__(self):
        return f'({self.type},{self.position},{self.color})'


initialGamePieces = [
    Piece('r', [0, 0], 'wh'),
    Piece('n', [0, 1], 'wh'),
    Piece('b', [0, 2], 'wh'),
    Piece('q', [0, 3], 'wh'),
    Piece('k', [0, 4], 'wh'),
    Piece('b', [0, 5], 'wh'),
    Piece('n', [0, 6], 'wh'),
    Piece('r', [0, 7], 'wh'),
    Piece('p', [1, 0], 'wh'),
    Piece('p', [1, 1], 'wh'),
    Piece('p', [1, 2], 'wh'),
    Piece('p', [1, 3], 'wh'),
    Piece('p', [1, 4], 'wh'),
    Piece('p', [1, 5], 'wh'),
    Piece('p', [1, 6], 'wh'),
    Piece('p', [1, 7], 'wh'),

    Piece('p', [6, 0], 'bl'),
    Piece('p', [6, 1], 'bl'),
    Piece('p', [6, 2], 'bl'),
    Piece('p', [6, 3], 'bl'),
    Piece('p', [6, 4], 'bl'),
    Piece('p', [6, 5], 'bl'),
    Piece('p', [6, 6], 'bl'),
    Piece('p', [6, 7], 'bl'),
    Piece('r', [7, 0], 'bl'),
    Piece('n', [7, 1], 'bl'),
    Piece('b', [7, 2], 'bl'),
    Piece('q', [7, 3], 'bl'),
    Piece('k', [7, 4], 'bl'),
    Piece('b', [7, 5], 'bl'),
    Piece('n', [7, 6], 'bl'),
    Piece('r', [7, 7], 'bl')
]

class Move:
    def __init__(self):
        moveDict = {}

class Turn:
    def __init__(self):
        self.count = 0
        self.player = Player()

class Player:
    def __init__(self):
        self.id = 0
        self.color = ''
        self.piecesList = []
        self.turn = Turn()

class Game:
    def __init__(self):
        self.pieceList = []
        self.board = Board()

    def setupBoard(self):
        for piece in initialGamePieces:
            self.board.tiles[piece.position[0]][piece.position[1]] = piece
        return

    def getPieceList(self):
        return self.pieceList

    def getBoard(self):
        return self.board