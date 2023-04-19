# This is a Rob ticket program for MaoYan

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from datetime import datetime

import pyautogui
import pytesseract

START_TIME = datetime(2023, 3, 5, 11, 00, 00)
LEVEL_STR = r'./maoyan_elements/test_price.png'
N_TICKET = "2"
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract-OCR\tesseract'


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


def getBuyingNowArea(left, top, width, height):
    # 在窗口中截取一张屏幕截图
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save(r'./maoyan_screenshot/Start_Booking.png')
    # 立即购票
    pos = pyautogui.locateOnScreen(r'./maoyan_elements/buying.png')
    # 返回该区域的中心的x,y坐标
    center = pyautogui.center(pos)
    print(f"Click Booking: {center}")
    pyautogui.moveTo(center.x, center.y)
    pyautogui.click()


def getTicketBuyPipeline(left, top, width, height):
    # 在窗口中截取一张屏幕截图
    screenshot1 = pyautogui.screenshot(region=(left, top, width, height))
    screenshot1.save(r'./maoyan_screenshot/Choose_Price.png')
    # 选择价格
    pos1 = pyautogui.locateOnScreen(LEVEL_STR)
    if pos1 is None:
        return False
    # 返回该区域的中心的x,y坐标
    price = pyautogui.center(pos1)
    print(f"Click Price : {price}")
    pyautogui.moveTo(price.x, price.y)
    pyautogui.click()
    time.sleep(0.25)

    i = 0
    pyautogui.screenshot(region=(left, top, width, height))
    notice = pyautogui.locateOnScreen(r'./maoyan_elements/notice.png')
    while notice is not None and i < 100:
        note = pyautogui.center(notice)
        print(f"Click Alert : {note}")
        pyautogui.moveTo(note.x, note.y)
        pyautogui.click()

        pyautogui.moveTo(price.x, price.y)
        pyautogui.click()
        time.sleep(0.25)
        screenshottemp = pyautogui.screenshot(region=(left, top, width, height))
        screenshottemp.save(r'./maoyan_screenshot/Notice.png')
        notice = pyautogui.locateOnScreen(r'./maoyan_elements/notice.png')
        i += 1
    if i == 100:
        return False
        # pyautogui.moveTo(x=left + width // 2 + 5, y=top + height // 2 + 17, duration=0.15)
        # pyautogui.click()

    # 选择票数
    pyautogui.screenshot(region=(left, top, width, height))
    pos2 = pyautogui.locateOnScreen(r'./maoyan_elements/plus1.png')
    if pos2 is None:
        return False
    num = pyautogui.center(pos2)
    print(f"Click Num : {num}")
    pyautogui.moveTo(num.x, num.y)
    pyautogui.click()

    # 确定订单
    pos3 = pyautogui.locateOnScreen(r'./maoyan_elements/submit.png')
    if pos3 is None:
        return False
    sub = pyautogui.center(pos3)
    print(f"Click Submit : {sub}")
    pyautogui.moveTo(sub.x, sub.y)
    pyautogui.click()
    time.sleep(0.75)  # 等待页面跳转

    # 增加购票人
    screenshot2 = pyautogui.screenshot(region=(left, top, width, height))
    screenshot2.save(r'./maoyan_screenshot/Pay_Order.png')
    # 选择购票人
    buyer = pyautogui.locateOnScreen(r'./maoyan_elements/buyers.png')
    if buyer is not None:
        people = pyautogui.center(buyer)
        print(f"Click people : {people}")
        pyautogui.moveTo(people.x, people.y)
        pyautogui.click()

    # 支付订单
    pos4 = pyautogui.locateOnScreen(r'./maoyan_elements/pay.png')
    if pos4 is None:
        return False
    center = pyautogui.center(pos4)
    print(f"Click pay : {center}")
    pyautogui.moveTo(center.x, center.y)
    pyautogui.click()

    screenshot3 = pyautogui.screenshot(region=(left, top, width, height))
    screenshot3.save(r'./maoyan_screenshot/Pay_Statue.png')
    status = pyautogui.locateOnScreen(r'./maoyan_elements/chatpay.png')
    if status is None:
        pyautogui.moveTo(x=left + width // 2, y=top + height // 2)
        pyautogui.click()
    else:
        return True


if __name__ == '__main__':
    # 倒计时3秒钟，手动将鼠标放在打开的小程序上
    print('Start...')
    time.sleep(5)
    LEFT, TOP, WIDTH, HEIGHT = getWindowsInfo()
    getBuyingNowArea(left=LEFT, top=TOP, width=WIDTH, height=HEIGHT)
    time.sleep(0.75)
    n = 0
    flag = False
    try:
        while n < 30 and flag is False:

            flag = getTicketBuyPipeline(left=LEFT, top=TOP, width=WIDTH, height=HEIGHT)
            n += 1
    except Exception as e:
        print('End.....\n', e)
