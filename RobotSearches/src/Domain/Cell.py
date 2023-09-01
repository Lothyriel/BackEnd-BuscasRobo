from enum import Enum


class Cell(Enum):  #  enum para classificar cada celula da matriz e cada nodo do grafo
    WALL = 1
    SHELF = 2
    HALL = 3
    INITIAL_POS = 4
    DELIVER_POS = 5
