import pygame
from pygame.locals import *
from consts import * #畫布
from gobang import GoBang

#IMAGE_PATH = '/Users/phantom/Projects/AI/gobang/UI/'
IMAGE_PATH = 'UI/'
#定義畫布大小
WIDTH = 540
HEIGHT = 540
MARGIN = 22
GRID = (WIDTH - 2 * MARGIN) / (N - 1)
PIECE = 32

class GameRender(object):
    def __init__(self, gobang):
        # 綁定邏輯類
        self.__gobang = gobang
        # 黑棋開局
        self.__currentPieceState = ChessboardState.BLACK

        # 初始化 pygame
        pygame.init()
        # pygame.display.set_mode((width, height), flags, depth) 
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('五子棋-made by 林逸倫 KHSH')

        # UI 資源 載入棋盤,棋子
        self.__ui_chessboard = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\chessboard.jpg').convert()
        self.__ui_piece_black = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\piece_black.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\piece_white.png').convert_alpha()

    def coordinate_transform_map2pixel(self, i, j):    
        # 從 chessMap 裏的邏輯座標到 UI 上的繪製座標的轉換(因chessMap中座標無法對應圖 所以做個轉換)
        return MARGIN + j * GRID - PIECE / 2, MARGIN + i * GRID - PIECE / 2

    def coordinate_transform_pixel2map(self, x, y):    
        # 從 chessMap 裏的邏輯座標到 UI 上的繪製座標的轉換(因chessMap中座標無法對應圖 所以做個轉換)
        i , j = int(round((y - MARGIN + PIECE / 2) / GRID)), int(round((x - MARGIN + PIECE / 2) / GRID))
        # 有MAGIN, 排除邊緣位置導致 i,j 越界
        if i < 0 or i >= N or j < 0 or j >= N:
            return None, None
        else:
            return i, j

    def draw_chess(self):
        # 繪出棋盤
        self.__screen.blit(self.__ui_chessboard, (0,0))
        # 繪出棋子
        for i in range(0, N):
            for j in range(0, N):
                x,y = self.coordinate_transform_map2pixel(i,j)
                state = self.__gobang.get_chessboard_state(i,j)
                if state == ChessboardState.BLACK:
                    self.__screen.blit(self.__ui_piece_black, (x,y))
                elif state == ChessboardState.WHITE:
                    self.__screen.blit(self.__ui_piece_white, (x,y))
                else: # ChessboardState.EMPTY
                    pass
                
    def draw_mouse(self):
        # 鼠標的座標
        x, y = pygame.mouse.get_pos()
        # 棋子跟隨鼠標移動
        if self.__currentPieceState == ChessboardState.BLACK:
            self.__screen.blit(self.__ui_piece_black, (x - PIECE / 2, y - PIECE / 2))
        else:
            self.__screen.blit(self.__ui_piece_white, (x - PIECE / 2, y - PIECE / 2))
		#勝利與否的繪圖 因避免其他電腦沒安裝相關語言(中文)因而使用 main 來避免錯誤
    def draw_result(self, result):
        pygame.font.get_fonts()
        font = pygame.font.SysFont('main', 50)
        tips = u"Game over:"
        if result == ChessboardState.BLACK :
            tips = tips + u"Black Won!"
        elif result == ChessboardState.WHITE:
            tips = tips + u"White Won!"
        else:
            tips = tips + u"Draw"
        text = font.render(tips, True, (255, 0, 0))
        self.__screen.blit(text, (WIDTH / 2 - 200, HEIGHT / 2 - 50))

    def one_step(self):
        i, j = None, None
        # 鼠標點擊
        mouse_button = pygame.mouse.get_pressed()
        # 左鍵
        if mouse_button[0]:
            x, y = pygame.mouse.get_pos()
            i, j = self.coordinate_transform_pixel2map(x, y)

        if not i is None and not j is None:
            # 格子上已經有棋子
            if self.__gobang.get_chessboard_state(i, j) != ChessboardState.EMPTY:
                return False
            else:
                self.__gobang.set_chessboard_state(i, j, self.__currentPieceState)
                return True

        return False
            
    def change_state(self):
        if self.__currentPieceState == ChessboardState.BLACK:
            self.__currentPieceState = ChessboardState.WHITE
        else:
            self.__currentPieceState = ChessboardState.BLACK
