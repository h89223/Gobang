# GoBang
請再 render.py 中把
        self.__ui_chessboard = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\chessboard.jpg').convert()
        self.__ui_piece_black = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\piece_black.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load(r'C:\Users\G_ss\Desktop\UI\piece_white.png').convert_alpha()
改為 
        self.__ui_chessboard = pygame.image.load(IMAGE_PATH + 'chessboard.jpg').convert()
        self.__ui_piece_black = pygame.image.load(IMAGE_PATH + 'piece_black.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load(IMAGE_PATH + 'piece_white.png').convert_alpha()
或
        self.__ui_chessboard = pygame.image.load('chessboard.jpg').convert()
        self.__ui_piece_black = pygame.image.load('piece_black.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load('piece_white.png').convert_alpha()