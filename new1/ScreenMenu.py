from maix import image, touchscreen

ts = touchscreen.TouchScreen()

last_pressed = False

def is_in_button(x, y, btn_pos):
    return x > btn_pos[0] and x < btn_pos[0] + btn_pos[2] and y > btn_pos[1] and y < btn_pos[1] + btn_pos[3]

def key_clicked(btn_rects):
    global last_pressed
    x, y, pressed = ts.read()
    if pressed:
        for i, btn in enumerate(btn_rects):
            if is_in_button(x, y, btn):
                if not last_pressed:
                    last_pressed = True
                    return True, i, btn
    else:
        last_pressed = False
    return False, 0, []

class ScreenMenu:

    def __init__(self) -> None:
        self.mode = 0    # 处于什么模式
        self.mode_s = 1  # 开始或停止
        self.source_qizi_id = 1  #原始棋子
        self.target_qizi_id = 1  #目标棋子
        self.finish_do = 1  # 表示下完棋了


    # 根据触摸屏绘制点，并显示点的坐标
    def showpos(self,img: image.Image):
        x, y, pressed = ts.read()
        img.draw_string(10, 40, f"x:{x} y:{y}", image.Color.from_rgb(255, 0, 0),scale=1.5)
        img.draw_circle(x,y,2,image.COLOR_GREEN,2)
        return img

    def check_mode_all(self, img : image.Image, disp_w, disp_h):
        img = self.check_mode_switch(img,disp_w, disp_h)
        img = self.check_modes_switch(img,disp_w, disp_h)
        img = self.check_sourceqizi_switch(img,disp_w, disp_h)
        img = self.check_targetqizi_switch(img,disp_w, disp_h)
        img = self.check_do_switch(img,disp_w, disp_h)
        return img

    def check_mode_switch(self, img : image.Image, disp_w, disp_h):
        btns = [0,0,100,40] 
        btn_rects_disp = [image.resize_map_pos(img.width(), img.height(), disp_w, disp_h, image.Fit.FIT_CONTAIN, btns[0], btns[1], btns[2], btns[3])]
        clicked, idx, rect = key_clicked(btn_rects_disp)
        if clicked:
            self.mode += 1
            if self.mode > 5:
                self.mode = 0
        img.draw_string(2, 10, f"Mode:{self.mode}", color=image.COLOR_GREEN, scale=1.5)
        img.draw_rect(btns[0], btns[1], btns[2],btns[3], image.COLOR_GREEN, 2)
        return img

    def check_do_switch(self, img : image.Image, disp_w, disp_h):
        btns = [100,0,100,40] 
        btn_rects_disp = [image.resize_map_pos(img.width(), img.height(), disp_w, disp_h, image.Fit.FIT_CONTAIN, btns[0], btns[1], btns[2], btns[3])]
        clicked, idx, rect = key_clicked(btn_rects_disp)
        if clicked:
            self.finish_do += 1
            if self.finish_do > 2:
                self.finish_do = 1
        if self.finish_do==1:
            img.draw_string(102, 10, f"do", color=image.COLOR_GREEN, scale=1.5)
        elif self.finish_do==2:
            img.draw_string(102, 10, f"waiting", color=image.COLOR_GREEN, scale=1.5)
        img.draw_rect(btns[0], btns[1], btns[2],btns[3], image.COLOR_GREEN, 2)
        return img

    def check_modes_switch(self, img : image.Image, disp_w, disp_h):
        btns = [200,0,100,40] 
        btn_rects_disp = [image.resize_map_pos(img.width(), img.height(), disp_w, disp_h, image.Fit.FIT_CONTAIN, btns[0], btns[1], btns[2], btns[3])]
        clicked, idx, rect = key_clicked(btn_rects_disp)
        if clicked:
            self.mode_s += 1
            if self.mode_s > 2:
                self.mode_s = 1
        if self.mode_s==1:
            img.draw_string(202, 10, f"Stop", color=image.COLOR_GREEN, scale=1.5)
        elif self.mode_s==2:
            img.draw_string(202, 10, f"Start", color=image.COLOR_GREEN, scale=1.5)
        img.draw_rect(btns[0], btns[1], btns[2],btns[3], image.COLOR_GREEN, 2)
        return img

    def check_sourceqizi_switch(self, img : image.Image, disp_w, disp_h):
        btns = [0,45,100,40] 
        btn_rects_disp = [image.resize_map_pos(img.width(), img.height(), disp_w, disp_h, image.Fit.FIT_CONTAIN, btns[0], btns[1], btns[2], btns[3])]
        clicked, idx, rect = key_clicked(btn_rects_disp)
        if clicked:
            self.source_qizi_id+= 1
            if self.source_qizi_id > 10:
                self.source_qizi_id = 1
        img.draw_string(2, 55, f"F:{self.source_qizi_id}", color=image.COLOR_RED, scale=1.5)
        img.draw_rect(btns[0], btns[1], btns[2],btns[3], image.COLOR_RED, 2)
        return img

    def check_targetqizi_switch(self, img : image.Image, disp_w, disp_h):
        btns = [200,45,100,40] 
        btn_rects_disp = [image.resize_map_pos(img.width(), img.height(), disp_w, disp_h, image.Fit.FIT_CONTAIN, btns[0], btns[1], btns[2], btns[3])]
        clicked, idx, rect = key_clicked(btn_rects_disp)
        if clicked:
            self.target_qizi_id+= 1
            if self.target_qizi_id > 9:
                self.target_qizi_id = 1
        img.draw_string(202, 55, f"T:{self.target_qizi_id}", color=image.COLOR_GREEN, scale=1.5)
        img.draw_rect(btns[0], btns[1], btns[2],btns[3], image.COLOR_GREEN, 2)
        return img
    