#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/3/2
import time

import pyautogui


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
        # 点击场次
        pyautogui.moveTo(left + 80, top + 220)
        # pyautogui.moveTo(left + 35, top + 334)  # 根据票价确定相对于窗口的坐标
        pyautogui.click()
        time.sleep(0.1)
        # 点击票价
        pyautogui.moveTo(left + 94, top + 450)
        # pyautogui.moveTo(left + 35, top + 376)  # 根据票价确定相对于窗口的坐标
        pyautogui.click()
        # # 点击缺货登记按钮
        pyautogui.moveTo(left + width // 2, top + 421)
        pyautogui.click()
        time.sleep(0.1)
        # 点击增加人数位置
        pyautogui.moveTo(left + 370, top + 680)
        pyautogui.click()
        # 点击提交
        pyautogui.moveTo(left + 370, top + 749)
        pyautogui.click()
        time.sleep(0.5)  # 页面加载
        # 输入购票人
        # pyautogui.moveTo(left + 59, top + 352)
        # pyautogui.click()
        pyautogui.moveTo(left + 59, top + 392)
        pyautogui.click()
        # 立即支付
        pyautogui.moveTo(left + 301, top + 754)
        pyautogui.click()
        count += 1


if __name__ == '__main__':
    print('Start...')
    # 等待5秒钟，确保程序可以启动并获取到鼠标位置
    time.sleep(5)
    LEFT, TOP, WIDTH, HEIGHT = getWindowsInfo()
    # startBooking(left=LEFT, top=TOP)
    fastClickTicket(left=LEFT, top=TOP, width=WIDTH, height=HEIGHT, max_click_epoch=30)
    print('End.....')
