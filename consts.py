#定義判斷5子相連的方式
from enum import Enum

N = 15

class ChessboardState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2
