from sys import _current_frames
from maix import camera, display, image, time, app, uart
from ScreenMenu import ScreenMenu
from CheckBoard import CheckBoardAlg
from ticai import print_board, best_move, check_winner, check_draw, Player
from UartControl import UartControl

menu = ScreenMenu()
cam = camera.Camera(320, 320, fps=60)
disp = display.Display()
checkBoard = CheckBoardAlg()
# 创建串口对象
uartcontrol = UartControl()

# 创建玩家，玩家默认是人
player = Player()

# 根据棋子ID和目标棋盘ID，获取启动坐标和停止坐标
# 注意 id 是从 1~9
# index 是从0~8
def getMovePos(source_qizi_id, target_qizi_id):
    # 从黑棋坐标中获得棋子坐标
    if source_qizi_id <= 5:
        source_qizi_index = source_qizi_id - 1
        qizi_black = checkBoard.qizi_blacks[source_qizi_index]
        qizi_x = int(qizi_black[0] )
        qizi_y = int(qizi_black[1] )
    # 从白棋中获取棋子坐标
    else:
        source_qizi_index = source_qizi_id - 6
        qizi_white = checkBoard.qizi_white[source_qizi_index]
        qizi_x = int(qizi_white[0] )
        qizi_y = int(qizi_white[1] )
    # 从棋盘坐标中获得5号棋盘坐标
    target_qizi_index = target_qizi_id - 1
    target_put = checkBoard.rect[target_qizi_index]
    target_x = int(target_put[0] )
    target_y = int(target_put[1] )
    return (qizi_x, qizi_y, target_x, target_y)

def getMovePosGlobal(source_qizi_id, target_qizi_id):
    # 从黑棋坐标中获得棋子坐标
    if source_qizi_id <= 5:
        source_qizi_index = source_qizi_id - 1
        qizi_black = checkBoard.global_qizi_blacks[source_qizi_index]
        qizi_x = int(qizi_black[0] )
        qizi_y = int(qizi_black[1] )
    # 从白棋中获取棋子坐标
    else:
        source_qizi_index = source_qizi_id - 6
        qizi_white = checkBoard.global_qizi_whites[source_qizi_index]
        qizi_x = int(qizi_white[0] )
        qizi_y = int(qizi_white[1] )
    # 从棋盘坐标中获得5号棋盘坐标
    target_qizi_index = target_qizi_id - 1
    target_put = checkBoard.rect[target_qizi_index]
    target_x = int(target_put[0] )
    target_y = int(target_put[1] )
    return (qizi_x, qizi_y, target_x, target_y)

# 拿任意一颗棋子放到指定位置  1-5
# 题目1
def do_one():
    if menu.mode_s == 2:
        if player.is_one_first_in ==True:
            player.source_chizi_id = 1
            checkBoard.global_qizi_blacks = checkBoard.qizi_blacks
            checkBoard.global_qizi_whites = checkBoard.qizi_whites
            player.is_one_first_in = False
        
        if player.source_chizi_id > 5:
            player.source_chizi_id = 1
            menu.mode = 0
            return
        print(f"chess id:{player.source_chizi_id}")
        movePos = getMovePosGlobal(player.source_chizi_id, 5)
        # 描述一下从那个开始到哪里
        print(movePos)
        # 运动 发串口指令
        uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3])
        # 延迟后显示完成 可能不需要
        # 下次启动必须按一下start
        # time.sleep(10)
        # uartcontrol.cmd_str(0,0,0,0)
        # print("do again")
        menu.mode_s = 1
        player.source_chizi_id = player.source_chizi_id + 1


# 题目2
def do_two():
    if menu.mode_s == 2:
        # 获得界面中原始坐标信息和目标坐标信息
        player.source_chizi_id = menu.source_qizi_id
        player.target_id = menu.target_qizi_id
        if player.is_two_first_in == True:
            checkBoard.global_qizi_blacks = checkBoard.qizi_blacks
            checkBoard.global_qizi_whites = checkBoard.qizi_whites
            player.is_two_first_in = False
            # to init
        movePos = getMovePosGlobal(player.source_chizi_id, player.target_id)
        print(f"chess id:{player.source_chizi_id} {player.target_id}")        
        # 描述一下从那个开始到哪里
        print(movePos)
        # 运动 发串口指令
        uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3])
        menu.mode_s = 1


# 题目3
def do_three():
    if menu.mode_s == 2:
        # 获得界面中原始坐标信息和目标坐标信息
        player.source_chizi_id = menu.source_qizi_id
        player.target_id = menu.target_qizi_id
        if player.is_3_first_in == True:
            checkBoard.global_qizi_blacks = checkBoard.qizi_blacks
            checkBoard.global_qizi_whites = checkBoard.qizi_whites
            player.is_3_first_in = False
            # to init
        movePos = getMovePosGlobal(player.source_chizi_id, player.target_id)
        print(f"chess id:{player.source_chizi_id} {player.target_id}")        
        # 描述一下从那个开始到哪里
        print(movePos)
        # 运动 发串口指令
        uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3])
        menu.mode_s = 1


#
def playAIFirst():
    #print(player.players[player.current_player])
    if player.players[player.current_player] == "O":
        # 不允许下一次进入
        print("AI is making a move...")
        if player.is_four_first_in  == True:
            player.is_four_first_in = False
            # 直接运动一次
            movePos = getMovePosGlobal(1, 1)
            player.source_chizi_id=2
            menu.finish_do = 2
            player.board[0][0] = 'O'
            print(f"chess move:{1} {1}")        
            # 运动 发串口指令
            uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3]) 
        else:  
            #检测是否被挪动过了，如果被挪动，则给出新位置ID
            # 获取棋盘上的状态
            player.board = checkBoard.qiziboard_AI_First()
            # ids = player.isCheat(player.oldboard,player.board)
            # print(ids)
            ids = []
            if len(ids) == 0:
                move = best_move(player.board)
                row, col = move
                # 更新棋盘信息
                menu.finish_do = 2
                # 虽然是X在下，但要放入O
                player.board[row][col] = 'O'
                print(player.board)    
                # 计算出目标棋盘
                player.target_id = row * 3 + (col+1)
                print(f"{player.source_chizi_id} Move to {player.target_id}")  
                movePos = getMovePosGlobal(player.source_chizi_id, player.target_id)
                print(f"chess id:{player.source_chizi_id} {player.target_id}")        
                # 运动 发串口指令
                uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3])        
                # add to do 移动机械臂   黑子      
                # 棋子ID加一
                player.source_chizi_id += 1 
                # 把上一次下过的棋盘，和上一次的位置都记录下来
                player.oldboard = player.board  
            elif len(ids)==2:
                print("I found cheat")
                # 把不一样的那个值那会到player.lastwhiteposID上
                #拿回棋子 退出 并彻底退出 
                # 注意要把ids[1]棋盘上的棋子挪回到ids[0] 中
                # to do list  add uart                
                menu.mode = 1
                return      
    else:
        # 等待人下棋完成
        if menu.finish_do==1:
            # 表示下棋完成
            # 更新棋盘
            player.board = checkBoard.qiziboard_AI_First()
            # 判断棋盘前后两次变换
            print(player.board)     
        else:
            #更新棋盘 相关信息
            #print("waiting player do")
            return
    
    #判定胜利者
    if check_winner(player.board, player.players[player.current_player]):
        print_board(player.board)
        print(f"Player {player.players[player.current_player]} wins!")
        menu.mode_s = 1  
        return
    #判定是否是平局
    if check_draw(player.board):
        print_board(player.board)
        print("The game is a draw!")
        menu.mode_s = 1  
        return
    # 切换下棋的人
    player.changePlayer()

def playHumanFirst():
    if player.players[player.current_player] == "X":
        # 等待人下棋完成
        if menu.finish_do == 1:
            # 表示下棋完成
            # 更新棋盘
            player.board = checkBoard.qiziboard()
            # 判断棋盘前后两次变换
            print(player.board)
        else:
            # 更新棋盘 相关信息
            # print("waiting player do")
            return
    else:
        # 获取一下当前的棋盘
        player.board = checkBoard.qiziboard()
        ids = []
        if len(ids) == 0:
            move = best_move(player.board)
            row, col = move          
        else:
            print("I found cheat")
            # 把不一样的那个值那会到player.lastwhiteposID上
            # 拿回棋子 退出 并彻底退出
            # 注意要把ids[1]中棋子那回到ids[0] 中
            # to do list  add uart
            menu.mode = 1
            return
        # 更新棋盘信息
        #menu.finish_do = 2
        # 虽然是X在下，但要放入O
        player.board[row][col] = "O"
        print(player.board)
        # 计算出目标棋盘
        player.target_id = row * 3 + (col + 1)
        print(f"{player.source_chizi_id} Move to {player.target_id}")
        # add to do 移动机械臂  白子
        player.target_id = row * 3 + (col+1)
        print(f"{player.source_chizi_id} Move to {player.target_id}")  
        movePos = getMovePosGlobal(player.source_chizi_id, player.target_id)
        print(f"chess id:{player.source_chizi_id} {player.target_id}")        
        # 运动 发串口指令
        uartcontrol.cmd_str(movePos[0], movePos[1], movePos[2], movePos[3])        
        # 棋子ID加一
        player.source_chizi_id += 1
        # 把上一次下过的棋盘，和上一次的位置都记录下来
        player.oldboard = player.board
        print("change to waiting")
        menu.finish_do = 2

    # 判定胜利者
    if check_winner(player.board, player.players[player.current_player]):
        print_board(player.board)
        print(f"Player {player.players[player.current_player]} wins!")
        menu.mode_s = 1
        return

    # 判定是否是平局
    if check_draw(player.board):
        print_board(player.board)
        print("The game is a draw!")
        menu.mode_s = 1
        return

    # 切换下棋的人
    player.changePlayer()


# 装置执黑先行 AI
def do_four():
    # 开始进行计算
    if menu.mode_s == 2:
        # 只要一次
        if player.is_four_first_in == True:
            player.current_player = 1
            player.cleanBoard()
            # 从黑棋开始移动
            checkBoard.global_qizi_blacks = checkBoard.qizi_blacks
            checkBoard.global_qizi_whites = checkBoard.qizi_whites
            player.source_chizi_id = 1
            menu.finish_do = 2
            # 在后面函数中清零
            #player.is_four_first_in = False
            #print("clear once")
        #  下一次棋
        #  注意一下这个棋要反下
        playAIFirst()


def do_five():
    if menu.mode_s == 2:
        if player.is_five_first_in == True:
            player.cleanBoard()
            player.current_player = 0
            # 从白棋开始移动
            checkBoard.global_qizi_blacks = checkBoard.qizi_blacks
            checkBoard.global_qizi_whites = checkBoard.qizi_whites
            player.source_chizi_id = 6
            menu.finish_do = 2
            player.is_five_first_in = False

        playHumanFirst()


def do_zero():
    if menu.mode_s == 2:
        # 发送一次坐标信息
        menu.mode_s = 1
        # 移动棋子的坐标
        # 默认棋子开始的坐标为 0 0
        print(0, 0, checkBoard.rect[0][0], checkBoard.rect[0][1])
        uartcontrol.cmd_str(0, 0, checkBoard.rect[0][0], checkBoard.rect[0][1])
        # 延迟1s 再发送一条
        time.sleep(10)
        print(0, 0, checkBoard.rect[8][0], checkBoard.rect[8][1])
        uartcontrol.cmd_str(0, 0, checkBoard.rect[8][0], checkBoard.rect[8][1])
        time.sleep(10)
        print(0, 0, checkBoard.rect[8][0], checkBoard.rect[8][1])
        # uartcontrol.cmd_str(0, 0, 0, 0)


def main():
    while not app.need_exit():
        img = cam.read()
        # 找到棋盘，找到棋子
        checkBoard.find_qipan(img)
        checkBoard.find_qizi(img)
        img = checkBoard.draw_qipan(img)
        img = checkBoard.draw_qizi(img)
        # 虚拟键盘
        img = menu.check_mode_all(img, disp.width(), disp.height())
        if menu.mode == 0:
            player.is_one_first_in = True
            player.is_3_first_in = True
            player.if_four_first_in = True
            player.is_five_first_in = True
            player.is_two_first_in = True
            do_zero()
        if menu.mode == 1:            
            player.is_two_first_in = True
            player.is_3_first_in = True
            player.if_four_first_in = True
            player.is_five_first_in = True
            do_one()
        elif menu.mode == 2:            
            player.is_one_first_in = True
            player.is_3_first_in = True
            player.if_four_first_in = True
            player.is_five_first_in = True
            do_two()
        elif menu.mode == 3:            
            player.is_one_first_in = True
            player.is_two_first_in = True
            player.if_four_first_in = True
            player.is_five_first_in = True
            do_three()            
        elif menu.mode == 4:
            player.is_one_first_in = True
            player.is_two_first_in = True
            player.is_3_first_in = True
            player.is_five_first_in = True
            do_four()
        elif menu.mode == 5:
            player.is_one_first_in = True
            player.is_two_first_in = True
            player.is_3_first_in = True
            player.is_four_first_in = True
            do_five()
        disp.show(img)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        e = traceback.format_exc()
        print(e)
        img = image.Image(disp.width(), disp.height())
        img.draw_string(
            2, 2, e, image.COLOR_WHITE, font="hershey_complex_small", scale=0.6
        )
        disp.show(img)
        while not app.need_exit():
            time.sleep(0.2)
