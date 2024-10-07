import math

#三子棋子  minmax算法 加速版本 但第一次运算还是有点慢


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # 检查所有可能的胜利情况：行、列和对角线
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # 第一行
        [board[1][0], board[1][1], board[1][2]],  # 第二行
        [board[2][0], board[2][1], board[2][2]],  # 第三行
        [board[0][0], board[1][0], board[2][0]],  # 第一列
        [board[0][1], board[1][1], board[2][1]],  # 第二列
        [board[0][2], board[1][2], board[2][2]],  # 第三列
        [board[0][0], board[1][1], board[2][2]],  # 主对角线
        [board[0][2], board[1][1], board[2][0]]   # 副对角线
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "X"):
        return -1
    if check_winner(board, "O"):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


class Player:

    # X 代表human  默认x先行
    # O 代表AI     
    def __init__(self,current_player=0) -> None:
        # 棋盘初始化
        self.board= [[" " for _ in range(3)] for _ in range(3)]
        # 老棋盘
        self.oldboard= self.board
        # 游戏对象
        self.players = ["X", "O"]
        self.current_player = 0
        self.is_one_first_in = True
        self.is_two_first_in = True
        self.is_3_first_in = True
        self.is_four_first_in = True
        self.is_five_first_in = True
        self.source_chizi_id = 1
        self.target_id = 5
    
    # 清盘
    def cleanBoard(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.oldboard = self.board
    
    # 切换玩家
    def changePlayer(self):
        self.current_player = 1-self.current_player
        print(self.current_player)
    
    def isCheat(self,oldboard,curboard):
        dif = 1
        ids = []
        for i in range(3):
            for j in range(3):
                # 原来的棋盘上有，现在的棋盘不一致 原始点
                if (oldboard[i][j] == "O" and oldboard[i][j]!=curboard[i][j]):
                    ids.append(i * 3 + j + 1)
                    dif += 1
                # 现在的棋盘上有，原有的棋盘没有，终点，
                if(oldboard[i][j]!=curboard[i][j] and curboard[i][j]=="O"):
                    ids.append(i * 3 + j + 1)
                    dif += 1
                if dif>2:
                    break
        return ids
    



