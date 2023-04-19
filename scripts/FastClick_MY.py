#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/3/2
import time

import pyautogui
import keyword


def getWindowsInfo():
    # 获取当前活动窗口对象
    win = pyautogui.getActiveWindow()
    # 获取当前活动窗口的位置和大小
    win_pos = (win.left, win.top)
    win_size = (win.width, win.height)
    print(f"Activate Windows position: {win_pos}")
    print(f"Activate Windows size: {win_size}")
    # 返回窗口左上角位置，宽度和高度
    return win.left, win.top, win.width, win.height


def startBooking(left, top):
    # 点击开始抢票
    # 根据已经获取的当前活动窗口的位置和大小, 移动鼠标到屏幕右下角，然后执行单击操作
    pyautogui.moveTo(left + 374, top + 746)
    pyautogui.click()
    time.sleep(0.7)


def fastClickTicket(left, top, width, height, max_click_epoch=20):
    # 选择价格，点击人数，立即下单，确认购票人，快速支付
    count = 0
    while count < max_click_epoch:
        # # 点击场次
        # pyautogui.moveTo(left + 94, top + 260)
        # # pyautogui.moveTo(left + 35, top + 334)  # 根据票价确定相对于窗口的坐标
        # pyautogui.click()
        # # time.sleep(0.1)
        # pyautogui.scroll(-50)
        # # 点击票价
        # pyautogui.moveTo(left + 104, top + 472)
        # # pyautogui.moveTo(left + 35, top + 334)  # 根据票价确定相对于窗口的坐标
        # pyautogui.click()
        # time.sleep(0.1)
        # # 点击缺货登记按钮
        pyautogui.moveTo(left + width // 2, top + 410)
        pyautogui.click()
        # time.sleep(0.1)
        # # 点击增加人数位置
        # pyautogui.moveTo(left + 374, top + 708)
        # pyautogui.click()
        # 点击提交
        pyautogui.moveTo(left + 374, top + 749)
        pyautogui.click()
        # time.sleep(0.7)  # 页面加载
        # 输入购票人
        pyautogui.scroll(-10)
        # pyautogui.moveTo(left + 97, top + 322)
        # pyautogui.typewrite('Alvaro')
        # pyautogui.moveTo(left + 208, top + 598)
        # pyautogui.click()
        # 立即支付
        pyautogui.moveTo(left + 374, top + 749)
        pyautogui.click()
        # time.sleep(0.2)
        count += 1


if __name__ == '__main__':
    print('Start...')
    # 等待5秒钟，确保程序可以启动并获取到鼠标位置
    time.sleep(3)
    LEFT, TOP, WIDTH, HEIGHT = getWindowsInfo()
    startBooking(left=LEFT, top=TOP)
    count = 0
    while count < 10:
        # 点击增加人数位置
        pyautogui.moveTo(LEFT + 374, TOP + 708)
        pyautogui.click()
        fastClickTicket(left=LEFT, top=TOP, width=WIDTH, height=HEIGHT, max_click_epoch=10)
        count += 1
    print('End.....')
