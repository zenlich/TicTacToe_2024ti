
# 串口控制命令
# 按学生协议做
# qizi x pos qizi y pos
# qipan x pos qipan y pos
# 0x2C 0x12 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x5B
from maix import uart

device = "/dev/ttyS0"
serial0 = uart.UART(device, 115200)

HEAD_FIRST   = "2C"
HEAD_SECOND  = "12"
HEAD_LAST    = "5B"


x_ratio = 0.54
x_dis = 0
y_ratio = 0.54
y_dis = 0


class UartControl():

    def __init__(self) -> None:
        pass
    '''
    def cmd(self,qizhipos_x,qizhipos_y,qipanpos_x,qipanpos_y):
        qizi_x = '{:04x}'.format(int(qizhipos_x))
        qizi_y = '{:04x}'.format(int(qizhipos_y))
        qipan_x = '{:04x}'.format(int(qipanpos_x))
        qipan_y = '{:04x}'.format(int(qipanpos_y))
        cmd_dat = f"{HEAD_FIRST}{HEAD_SECOND}{qizi_x}{qizi_y}{qipan_x}{qipan_y}{HEAD_LAST}"        
        serial0.write(bytes.fromhex(cmd_dat))
    '''
    def cmd_str(self,qizhipos_x,qizhipos_y,qipanpos_x,qipanpos_y):
        FH = bytearray([0x2C,int(qizhipos_x),int(qizhipos_y),int(qipanpos_x),int(qipanpos_y),0x5B])
        print(FH)
        serial0.write_str(FH)