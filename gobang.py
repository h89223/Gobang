from enum import Enum
from consts import *

class GoBang(object):
    def __init__(self):
        self.__chessMap = [[ChessboardState.EMPTY for j in range(N)] for i in range(N)]
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = ChessboardState.EMPTY

    def get_chessMap(self):
        return self.__chessMap

    def get_chessboard_state(self, i, j):
        return self.__chessMap[i][j]

    def set_chessboard_state(self, i, j, state):
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state

# x = 0 ; y = 1 y軸正方向
# x = 0 ; y =-1 y軸負方向
# x = 1 ; y = 1 45°斜角正方向

   

    def have_five(self, i, j, color):
        #由四個棋盤方向來計數 (橫向 直向 左斜方 右斜方)
        directions = [[(-1, 0), (1, 0)], \
                      [(0, -1), (0, 1)], \
                      [(-1, 1), (1, -1)], \
                      [(-1, -1), (1, 1)]]

        for axis in directions:
            axis_count = 1
            for (xdirection, ydirection) in axis:
                axis_count += self.count_on_direction(i, j, xdirection, ydirection, color)
                if axis_count >= 5:
                    return True

        return False




    def count_on_direction(self, i, j, xdirection, ydirection, color):
        count = 0
        for step in range(1, 5): #除了當前位置 還要再往對應方向看4步來判斷是否達成條件
            if xdirection != 0 and (j + xdirection * step < 0 or j + xdirection * step >= N):
                break
            if ydirection != 0 and (i + ydirection * step < 0 or i + ydirection * step >= N):
                break
            if self.__chessMap[i + ydirection * step][j + xdirection * step] == color:
                count += 1
            else:
                break
        return count


    #最後返回結果
    def get_chess_result(self):
        if self.have_five(self.__currentI, self.__currentJ, self.__currentState):
            return self.__currentState
        else:
            return ChessboardState.EMPTY

        
