from maix import camera, display, image, time, app, touchscreen
import cv2
import numpy as np
import math

# 和棋盘 棋子相关的封装类


class CheckBoardAlg:

    def __init__(self) -> None:
        # 交叉点坐标
        self.cross_points = []
        # 中心点坐标
        self.centers = []
        # 标识棋盘 ID
        self.rect = np.zeros((9, 2), dtype="float32")
        # 是否大于45度
        self.is_over_45 = False
        # 黑白色棋子坐标
        self.qizi_coners = []
        self.qizi_blacks = []
        self.qizi_whites = []
        self.global_qizi_blacks = []
        self.global_qizi_whites = []
        # 在棋盘上白棋和黑棋的数量
        self.blackcounts = 0
        self.whitecounts = 0

    # 画棋
    def draw_qipan(self, img):
        # 四个顶角点
        for cross_point in self.cross_points:
            img.draw_circle(cross_point[0], cross_point[1], 3, image.COLOR_GREEN, -1)
        # 画中心
        for center in self.centers:
            img.draw_circle(center[0], center[1], 2, image.COLOR_GREEN, -1)
        for i in range(9):
            img.draw_string(
                self.rect[i][0],
                self.rect[i][1],
                f"{i + 1}",
                image.COLOR_WHITE,
                scale=2,
                thickness=-1,
            )
        return img

    # 找棋盘
    def find_qipan(self, img):
        # 查找中心算法 1,2
        find_center_method = 1
        # 区域门限
        area_threshold = 80
        # 点门限
        pixels_threshold = 50
        # 门限
        thresholds = [[29, 49, 46, 66, 3, 23]]  # red
        # 软件畸变矫正，速度比较慢，建议直接买无畸变摄像头（Sipeed 官方淘宝点询问）
        # img = img.lens_corr(strength=1.5)
        # 启动 opencv
        img_cv = image.image2cv(img, False, False)
        # 变成灰度图
        gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
        # 高斯模糊去噪声
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # 边缘检测
        edged = cv2.Canny(gray, 50, 150)
        # 膨胀处理
        kernel = np.ones((5, 5), np.uint8)
        dilated = cv2.dilate(edged, kernel, iterations=1)
        # 现实图片
        # disp.show(image.cv2image(dilated, False, False))
        # 查找轮廓
        contours, _ = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        if len(contours) > 0:
            # 筛选出最大的轮廓
            largest_contour = max(contours, key=cv2.contourArea)
            # 近似多边形
            epsilon = 0.02 * cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, epsilon, True)
            # 如果找到的是一个四边形
            if len(approx) == 4:
                # print("rect found")
                corners = approx.reshape((4, 2))
                # 绘制顶点和轮廓
                # for corner in corners:
                #     cv2.circle(img_cv, tuple(corner), 4, (0, 255, 0), -1)

                # 绘制四边路径性
                # cv2.drawContours(img_cv, [approx], -1, (0, 255, 0), 1)
                # 洪泛填充外部，如果棋盘外部的背景和棋盘内部的背景不同才需要这一步
                #img.flood_fill(
                #    corners[0][0] - 5, corners[0][1] - 5, 0.3, 0.3, image.COLOR_BLUE
                #)
                # img.flood_fill(corners[1][0] - 5, corners[1][1] + 5, 0.5, 0.05, image.COLOR_BLUE)
                # img.flood_fill(corners[0][0] + 5, corners[0][1] + 5, 0.5, 0.05, image.COLOR_BLUE)
                # img.flood_fill(corners[0][0] + 5, corners[0][1] - 5, 0.5, 0.05, image.COLOR_BLUE)

                # 按顺序排列角点（左上、右上、右下、左下）
                # rect = np.zeros((4, 2), dtype="float32")
                # s = corners.sum(axis=1)
                # rect[0] = corners[np.argmin(s)]
                # rect[2] = corners[np.argmax(s)]
                # diff = np.diff(corners, axis=1)
                # rect[1] = corners[np.argmin(diff)]
                # rect[3] = corners[np.argmax(diff)]

                # (tl, tr, br, bl) = rect
                # 上面出来的结果已经是 点从左上逆时针，所以跳过找顶点
                tl = corners[0]
                bl = corners[1]
                br = corners[2]
                tr = corners[3]

                # print(corners)

                # 计算像素——物理坐标
                # self.x_ratio = 94 / (tr[0] - tl[0])
                # self.y_ratio = 94 / (bl[1] - tl[1])
                # print(self.x_ratio)
                # print(self.y_ratio)
                # print(corners[0] * self.x_ratio)

                # 计算3x3格子的交叉点 交叉点需要保存
                self.cross_points = []
                for i in range(4):
                    for j in range(4):
                        # 线性插值计算交叉点
                        cross_x = int(
                            (tl[0] * (3 - i) + tr[0] * i) * (3 - j) / 9
                            + (bl[0] * (3 - i) + br[0] * i) * j / 9
                        )
                        cross_y = int(
                            (tl[1] * (3 - i) + tr[1] * i) * (3 - j) / 9
                            + (bl[1] * (3 - i) + br[1] * i) * j / 9
                        )
                        self.cross_points.append((cross_x, cross_y))
                        # cv2.circle(img_cv, (cross_x, cross_y), 3, (0, 255, 0), -1)

                self.centers = []
                # 找格子中心点方法一：直接根据顶点计算
                if find_center_method == 1:
                    for i in range(3):
                        for j in range(3):
                            center_x = int(
                                (
                                    self.cross_points[i * 4 + j][0]
                                    + self.cross_points[i * 4 + j + 1][0]
                                    + self.cross_points[(i + 1) * 4 + j][0]
                                    + self.cross_points[(i + 1) * 4 + j + 1][0]
                                )
                                / 4
                            )
                            center_y = int(
                                (
                                    self.cross_points[i * 4 + j][1]
                                    + self.cross_points[i * 4 + j + 1][1]
                                    + self.cross_points[(i + 1) * 4 + j][1]
                                    + self.cross_points[(i + 1) * 4 + j + 1][1]
                                )
                                / 4
                            )
                            self.centers.append((center_x, center_y))
                            # cv2.circle(img_cv, (center_x, center_y), 2, (0, 255, 0), -1)
                elif find_center_method == 2:
                    # 找格子中心点方法二： 找色块的方式来确定中心点
                    roi = [
                        corners[:, 0].min(),
                        corners[:, 1].min(),
                        corners[:, 0].max() - corners[:, 0].min(),
                        corners[:, 1].max() - corners[:, 1].min(),
                    ]
                    img.draw_rect(roi[0], roi[1], roi[2], roi[3], image.COLOR_WHITE)
                    blobs = img.find_blobs(
                        thresholds,
                        roi=roi,
                        x_stride=2,
                        y_stride=1,
                        area_threshold=area_threshold,
                        pixels_threshold=pixels_threshold,
                    )
                    for b in blobs:
                        self.centers.append((b.cx(), b.cy()))
                        img.draw_circle(b.cx(), b.cy(), 2, image.COLOR_WHITE, -1)
                else:
                    raise Exception("find_center_method value error")

                # 对找到的中心点进行编号, y + x 最大就是右下角，最小就是左上角， y-x 最大就是左下角，y-x 最小就是右上角，其它几个点根据在旁边两个点中间判断
                if len(self.centers) == 9:
                    self.centers = np.array(self.centers)
                    self.rect = np.zeros((9, 2), dtype="float32")
                    s = self.centers.sum(axis=1)
                    idx_0 = np.argmin(s)
                    idx_8 = np.argmax(s)
                    diff = np.diff(self.centers, axis=1)
                    idx_2 = np.argmin(diff)
                    idx_6 = np.argmax(diff)
                    self.rect[0] = self.centers[idx_0]
                    self.rect[2] = self.centers[idx_2]
                    self.rect[6] = self.centers[idx_6]
                    self.rect[8] = self.centers[idx_8]
                    #   其它点
                    calc_center = (
                        self.rect[0] + self.rect[2] + self.rect[6] + self.rect[8]
                    ) / 4
                    mask = np.zeros(self.centers.shape[0], dtype=bool)
                    idxes = [1, 3, 4, 5, 7]
                    mask[idxes] = True
                    others = self.centers[mask]
                    idx_l = others[:, 0].argmin()
                    idx_r = others[:, 0].argmax()
                    idx_t = others[:, 1].argmin()
                    idx_b = others[:, 1].argmax()
                    found = np.array([idx_l, idx_r, idx_t, idx_b])
                    mask = np.isin(range(len(others)), found, invert=False)
                    idx_c = np.where(mask == False)[0]
                    if len(idx_c) == 1:
                        self.rect[1] = others[idx_t]
                        self.rect[3] = others[idx_l]
                        self.rect[4] = others[idx_c]
                        self.rect[5] = others[idx_r]
                        self.rect[7] = others[idx_b]
                        # 写编号
                        # for i in range(9):
                        # img.draw_string(self.rect[i][0], self.rect[i][1], f"{i + 1}", image.COLOR_WHITE, scale=2, thickness=-1)
                    else:
                        # 大于 45度的情况
                        self.is_over_45 = True
                        print("> 45 degree")
        # return img

    # 画棋
    def draw_qizi(self, img):
        i = 1
        for qizi in self.qizi_blacks:
            img.draw_circle(qizi[0], qizi[1], qizi[2], image.COLOR_GREEN, 2)
            # img.draw_string(qizi[0], qizi[1], f"{i}", image.COLOR_GREEN, scale=2, thickness=-1)
            i = i + 1
        i = 5
        for qizi in self.qizi_whites:
            img.draw_circle(qizi[0], qizi[1], qizi[2], image.COLOR_GREEN, 2)
            # img.draw_string(qizi[0], qizi[1], f"{i + 1}", image.COLOR_RED, scale=2, thickness=-1)
            i = i + 1
        return img

    def find_qizi(self, img):
        area_threshold = 300
        pixels_threshold = 300
        black_threshold = 2000
        white_threshold = 2000
        self.qizi_blacks = []
        self.qizi_whites = []
        self.blackcounts = 0
        self.whitecoutns = 0
        thresholds = []
        # [[0, 80, 0, 80, 30, 80]]
        # threshold_red = [40, 60, 33, 53, -10, 10]
        # color define
        threshold_red = [21, 79, 19, 77, -41, 35]
        threshold_black = [0, 48, -42, 31, -32, 10]
        threshold_white = [71, 100, -26, 2, -19, 1]
        thresholds.append(threshold_red)
        thresholds.append(threshold_black)
        thresholds.append(threshold_white)
        # 软件畸变矫正，速度比较慢，建议直接买无畸变摄像头（Sipeed 官方淘宝点询问）
        #img = img.lens_corr(strength=1.5)
        # img.find_circles
        blobs = img.find_blobs(
            thresholds,
            roi=[1, 1, img.width() - 1, img.height() - 1],
            x_stride=2,
            y_stride=1,
            area_threshold=area_threshold,
            pixels_threshold=pixels_threshold,
        )
        for b in blobs:
            corners = b.mini_corners()
            # print(b.code())
            if b.code() == 1:
                # print("find code 1")
                for i in range(4):
                    pass
                    # img.draw_line(corners[i][0], corners[i][1], corners[(i + 1) % 4][0], corners[(i + 1) % 4][1], image.COLOR_YELLOW, 2)
            elif b.code() == 2:
                if (
                    b.area() < black_threshold
                ):  # 过滤掉棋盘，认为area大于800时是棋盘，根据实际值调节
                    enclosing_circle = b.enclosing_circle()
                    self.qizi_blacks.append(
                        [enclosing_circle[0], enclosing_circle[1], enclosing_circle[2]]
                    )
                    # img.draw_circle(enclosing_circle[0], enclosing_circle[1], enclosing_circle[2], image.COLOR_GREEN, 2)
            elif b.code() == 4:
                if b.area() < white_threshold:
                    enclosing_circle = b.enclosing_circle()
                    self.qizi_whites.append(
                        [enclosing_circle[0], enclosing_circle[1], enclosing_circle[2]]
                    )
                    # img.draw_circle(enclosing_circle[0], enclosing_circle[1], enclosing_circle[2], image.COLOR_RED, 2)

    # 根据情况来确定
    # X 黑棋   O 白棋
    def qiziboard(self):
        # 如果黑色棋子 或 白色棋子 大于 5个 算法不启动
        dis_thread = 8
        # print("blacks %s whites %s"%(len(self.qizi_blacks),len(self.qizi_whites)))
        # if len(self.qizi_blacks) > 5 or len(self.qizi_whites) > 5:
        # print("the black is over 5")
        # return
        # 判断棋子的坐标和棋盘的坐标的中心值
        board = [[" " for _ in range(3)] for _ in range(3)]
        self.blackcounts = 0
        for qizi in self.qizi_blacks:
            index = 0
            for r in self.rect:
                dis = math.sqrt((qizi[0] - r[0]) ** 2 + (qizi[1] - r[1]) ** 2)
                if dis < dis_thread:
                    # print("black is in %s"%(index+1))
                    row = index // 3
                    col = index % 3
                    if board[row][col] == " ":
                        board[row][col] = "X"
                    self.blackcounts = self.blackcounts + 1
                index = index + 1

        self.whitecounts = 0
        for qizi in self.qizi_whites:
            index = 0
            for r in self.rect:
                dis = math.sqrt((qizi[0] - r[0]) ** 2 + (qizi[1] - r[1]) ** 2)
                if dis < dis_thread:
                    # print("white is in %s"%(index+1))
                    self.whitecounts = self.whitecounts + 1
                    row = index // 3
                    col = index % 3
                    if board[row][col] == " ":
                        board[row][col] = "O"

                index = index + 1

        return board

    def qiziboard_AI_First(self):
        # 如果黑色棋子 或 白色棋子 大于 5个 算法不启动
        dis_thread = 8
        # print("blacks %s whites %s"%(len(self.qizi_blacks),len(self.qizi_whites)))
        # if len(self.qizi_blacks) > 5 or len(self.qizi_whites) > 5:
        # print("the black is over 5")
        # return
        # 判断棋子的坐标和棋盘的坐标的中心值
        board = [[" " for _ in range(3)] for _ in range(3)]
        self.blackcounts = 0
        for qizi in self.qizi_blacks:
            index = 0
            for r in self.rect:
                dis = math.sqrt((qizi[0] - r[0]) ** 2 + (qizi[1] - r[1]) ** 2)
                if dis < dis_thread:
                    # print("black is in %s"%(index+1))
                    row = index // 3
                    col = index % 3
                    if board[row][col] == " ":
                        board[row][col] = "O"
                    self.blackcounts = self.blackcounts + 1
                index = index + 1

        self.whitecounts = 0
        for qizi in self.qizi_whites:
            index = 0
            for r in self.rect:
                dis = math.sqrt((qizi[0] - r[0]) ** 2 + (qizi[1] - r[1]) ** 2)
                if dis < dis_thread:
                    # print("white is in %s"%(index+1))
                    self.whitecounts = self.whitecounts + 1
                    row = index // 3
                    col = index % 3
                    if board[row][col] == " ":
                        board[row][col] = "X"

                index = index + 1

        return board
