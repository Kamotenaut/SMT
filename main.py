import cv2
import time
import datetime
import pyautogui
import numpy as np
import os, os.path
from PIL import Image
import subprocess
from logzero import logger
import win32ui

############
# Settings #
PAUSE_TIME = 1.5
TIMING_MULT = 1.5
CLOSENESS_THRESHOLD = 0.8
ROLLS_FOLDER = 'rolls'
NAME = 'Remotoz'
############

pyautogui.PAUSE = PAUSE_TIME
pyautogui.FAILSAFE = True

HOME_BUTTON = {'x': 503, 'y': 757}
DX2_ICON = {'x': 337, 'y': 438}
FILE_MANAGER = {'x' : 147, 'y' : 294}
SKIP_BUTTON = {'x': 1200, 'y': 70}
CONFIRM = {'x': 830, 'y': 600}
AGREE = {'x': 335, 'y':755}
ATTACK = {'x': 1125, 'y': 630}
NOX_PATH = "D:\\Program Files\\Nox\\bin\\Nox.exe"

def StartNoxProcess():
    try:
        logger.info("Starting Nox")
        process = subprocess.Popen(NOX_PATH, shell=True, stdout=subprocess.PIPE)
    except:
        logger.error("Nox failed")

def IsNoxRunning():
    try:
        if win32ui.FindWindow(None, "Nox App Player"):
            return True
    except:
        return False

def KillNoxProcess():
    try:
        if IsNoxRunning():
            os.system("taskkill /im Nox.exe /f")
    except:
        logger.error("The program could not be killed")

def wait(given_time):
    time.sleep(TIMING_MULT * given_time)


def touch(x, y):
    pyautogui.click(x=x, y=y)

def close_app():
    touch(**HOME_BUTTON)
    touch(x=502, y=791)  # App Switcher
    pyautogui.moveTo(280, 750)  # Move Cursor Over GO
    pyautogui.dragTo(43, 750,.2,button='left')
    wait(1)
    pyautogui.moveTo(280, 750)  # Move Cursor Over GO
    pyautogui.dragTo(43, 750,.2,button='left')
    touch(**HOME_BUTTON)
    wait(1)


def select_card(card_no):
    locations = {1: 140, 2: 390, 3: 650, 4: 900, 5: 1160}
    touch(x=locations[card_no], y=530)


def image_is_on_screen(template_name):
    template = cv2.imread(os.path.join(
        'screenshots',
        template_name + '.png'),
        cv2.IMREAD_GRAYSCALE)
    image = cv2.cvtColor(
        np.array(pyautogui.screenshot(
            region=(0, 0, 523, 832))),
        cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= CLOSENESS_THRESHOLD)

    # Not sure why this works but okay
    for pt in zip(*loc[::-1]):
        return True

    return False


def click_until(*images):
    pyautogui.PAUSE = 0.2 * PAUSE_TIME
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen("error"):
                touch(242,492)
            elif image_is_on_screen(image):
                pyautogui.PAUSE = PAUSE_TIME
                wait(0.5)
                return pos

        for _ in range(10):
            touch(**LEFT_EDGE)


def wait_until(*images):
    while True:
        for pos, image in enumerate(images):
            if image_is_on_screen("error"):
                touch(242,492)
            elif image_is_on_screen(image):
                wait(0.5)
                return pos
def remove_pref():
    close_app()
    touch(142, 328)
    touch(397, 800)
    pyautogui.typewrite("playerpref", interval=.25)
    touch(238, 139)
    wait_until("playerpref")
    pyautogui.mouseDown(260, 125, button='left', duration=2.3)
    wait(1)
    touch(280, 390)
    touch(280, 390)
    touch(355, 500)
    touch(**HOME_BUTTON)

if __name__ == '__main__':
    TimeIOError = 0
    if not os.path.exists(ROLLS_FOLDER):
        os.mkdir(ROLLS_FOLDER)
    try:
        while True:

            StartNoxProcess()
            # # First Launch
            # wait_until('dx2_icon')
            # remove_pref()
            # wait_until('dx2_icon')
            # touch(**HOME_BUTTON)
            # touch(**DX2_ICON)  # Game Icon
            #
            # # # Intro
            # click_until('Terms')
            # touch(**AGREE)  # AGREE TOS
            # wait_until('check_setting')
            # touch(**CLOSE_SETTING)
            #
            # # titlescreen
            # wait_until('title_start')
            # touch(246, 605)  # start button
            # wait_until('scene1')
            # # skip
            # touch(447, 750)
            # wait(0.5)
            # touch(447, 750)
            # # charselect
            # wait(0.5)
            # touch(149, 423)
            # wait(0.5)
            # touch(149, 423)
            # # writename
            # pyautogui.typewrite(NAME, interval=0.25)
            # touch(245, 360)
            # touch(245, 500)
            # wait_until('confirm_name')
            # touch(297, 494)
            # #skip
            # wait_until("menu_button_rev")
            # touch(460, 775)
            # wait(2)
            # touch(437, 775)
            # #battlescene
            # #wait_until("tut_battle_1")
            # click_until("tut_battle_1_arrow2")
            # touch(140,620)
            # click_until("tut_battle_1_2")
            # touch(140, 620)
            # #2ndmob
            # click_until("tut_battle_1_arrow4")
            # touch(230,590)
            # click_until("tut_battle_1_2")
            # touch(320,595)
            # # #3rdmob
            # click_until("fairy_ava")
            # touch(230, 590)
            # click_until("dog_ava_smol")
            # touch(320, 595)
            # wait(3)
            # touch(230, 590)
            # click_until("end_combat_1")
            # touch(450, 790)
            # touch(450, 790)
            # touch(450, 790)
            # #movie
            # click_until("skip_1")
            # touch(290,500)
            #
            # click_until("dialogue1")
            # touch(311,360)
            # click_until("arrow1")
            # touch(446,770)
            # #click_until("arrow1_3") #here atm
            # touch(460,791)
            # wait(.5)
            # touch(309,716)
            # click_until("dialogue2")
            # touch(343,353)
            # click_until("arrow2")
            # touch(186,129)
            # click_until("arrow3")
            # touch(252,626)
            # touch(36,787)
            # touch(36, 787)
            # touch(36, 787)
            # touch(36, 787)
            # touch(36, 787)
            # #arrow4
            # click_until("pop1_1")
            # touch(239,720)
            # click_until("arrow5_1")
            # touch(458,781)
            # click_until("menu1")
            # touch(457,776)
            # wait(1)
            # #home
            # touch(232,765)
            # click_until("home1")
            # touch(194,616)
            # touch(107,706)
            # click_until("mail1")
            # touch(193,770)
            # touch(320,499)
            # touch(247,496)
            # touch(457, 776)
            # wait(1)
            # touch(374,760)
            # wait(1)
            # touch(317,375)
            #
            # #prologue
            # wait(2)
            # touch(301,367)
            # wait(1)
            # touch(344,168)
            # wait(1)
            # touch(466,783)
            # touch(444,769)
            # #bat1
            # wait_until("wait_bat2")
            # touch(410,290)
            # wait_until("bat1")
            # touch(241, 550)
            # #menu skip
            # wait_until("menu_button")
            # touch(455,776)
            # touch(440,770)

            # click_until("bat2_arrow1")
            # touch(226,142)
            # click_until("interaction_mid")
            # click_until("mokoi_interaction")
            # touch(95,513)
            # touch(95, 513)
            # click_until("interaction_mid")
            # touch(95, 513)
            # click_until("interaction_mid")
            # click_until("mokoi_interaction")
            # touch(95, 513)
            # touch(95, 513)
            # click_until("bat2_pop1")
            # touch(435,425)
            # touch(435, 425)
            # touch(236,722)
            # click_until("tut_battle_1_4")
            # #battleskip
            # touch(453,136)
            # touch(453,136)
            # #
            # #change_auto
            # touch(466,502)
            # wait_until("auto_talk_menu_button")
            # touch(383,658)
            # touch(187,479)
            # touch(176,744)
            # touch(32,788)
            # touch(306,505)
            # touch(440,75)
            # #
            #
            # click_until("bat2_end")
            # touch(442,790)
            # wait(1)
            # touch(442, 790)
            # touch(442, 790)
            # wait_until("close_button")
            # touch(251,551)
            # touch(442, 790)
            # wait(1)
            # # menu skip
            # wait_until("menu_button_rev")
            # touch(455, 776)
            # wait(1)
            # touch(440, 770)
            # #
            # touch(378,656)
            # touch(378, 656)
            # wait_until("chap1_2")
            # touch(416,292)
            # click_until("bat3_start")
            # touch(237,404)
            # click_until("bat3_start1_play")
            # touch(77,146)
            # click_until("bat3_start2")
            # touch(332,451)
            # wait_until("bat3_start3")
            # touch(247,335)
            # click_until("bat3_start4")
            # touch(238,547)
            # # menu skip
            # wait_until("menu_button_rev")
            # touch(455, 776)
            # touch(440, 770)
            # #
            # click_until("skip_button")
            # touch(444,783)
            # wait_until("skip_button_message")
            # touch(305,503)
            #
            # click_until("neko_ava")
            # # battleskipfull
            # touch(440, 75)
            # touch(453, 136)
            # touch(453, 136)

            # click_until("chap2_2_1")
            # touch(140, 595)

            click_until("mokoi_ava")
            click_until("mokoi_ava")
            #battleskipfull
            touch(440, 75)
            touch(453, 136)
            touch(453, 136)
            #

            #endofbattle2
            click_until("end_combat_1_2")
            touch(460,781)
            click_until("end_combat_1_2")
            touch(460,781)
            click_until("end_combat_1_2_1")
            touch(240,542)
            click_until("close_button")
            touch(233,521)
            #menu
            click_until("end_dialogue_chap1_2")
            touch(443,789)
            #skip
            wait_until("menu_button_rev")
            touch(455, 776)
            touch(440, 770)
            #
            click_until("menu2")
            touch(455,780)
            wait_until("chap1_2_menu_hideout")
            touch(303,716)
            wait_until("chap1_2_church")
            touch(243,767)
            #
            click_until("fusion1")
            touch(129,543)
            wait(.5)
            touch(129,543)
            click_until("fusion2")
            touch(108,485)
            touch(193,474)
            click_until("chap1_2_church_fusion")
            touch(251,389)
            touch(251, 389)
            touch(251, 389)
            touch(251, 389)

            wait(1)
            touch(251,730)
            touch(251, 730)
            touch(251, 730)
            touch(251, 730)
            click_until("fusion3")
            touch(443,427)
            touch(256,718)
            click_until("fusion4")
            touch(238,522)
            click_until("sum1")
            touch(91,219)
            click_until("sum2")
            touch(405,307)
            click_until("sum3")
            touch(422,424)
            touch(248,723)
            click_until("sum4")
            touch(241,514)
            click_until("sum5")
            pyautogui.moveTo(195, 505)  # Move Cursor Over GO
            pyautogui.dragTo(195, 100, 3, button='left')
            wait_until("sum_tix1")
            touch(396,339)
            touch(261,679)
            click_until("pull1")

            folder_name = os.path.join(ROLLS_FOLDER,
                                       datetime.datetime.now().strftime('%y_%m_%d_%H_%M'))
            lock_file = os.path.join(folder_name, '.done')

            if image_is_on_screen('stars5'):
                try:
                    os.mkdir(folder_name)
                    open(lock_file, 'a').close()
                except FileExistsError:
                    pass  # Tbh idk what to do if this happens
                except WindowsError:
                    pass  # Folder already exists

                #screenshot
                pull1 = pyautogui.screenshot(region=(100, 144, 75, 55))
                pull1Img = Image.new('RGB', (75, 55))
                pull1Img.paste(pull1, (0, 0))
                pull1Img.save(os.path.join(folder_name,'rolls.png'))
                #
                touch(447, 787)
                wait_until("sum6")
                touch(396, 339)
                touch(261, 679)
                touch(32, 788)
                touch(32,788)
                touch(237,548)
                click_until("pull1")
                touch(446,773)
                # screenshot
                pull2 = pyautogui.screenshot(region=(100, 144, 75, 55))
                pull2Img = Image.new('RGB', (75, 55))
                pull2Img.paste(pull2, (0, 0))
                pull2Img.save(os.path.join(folder_name, 'rolls2.png'))

                # screenshot account
                click_until("arrow5")
                touch(458, 781)
                click_until("party_button_hand")
                touch(378,669)
                click_until("party1")
                touch(226,171)
                click_until("bat3_start1")
                touch(77, 146)
                click_until("party_2")
                touch(80,155)
                click_until("close_button")
                touch(251, 551)
                touch(456, 777)
                touch(179, 794)
                touch(98, 277)
                touch(380, 231)

                touch()
                i = 0
                while os.path.exists("account%s.png" % i) :
                    i += 1
                acc = pyautogui.screenshot(region=(95, 208, 203, 48))
                accImg = Image.new('RGB', (203, 48))
                accImg.paste(pull1, (0, 0))
                accImg.save(os.path.join(folder_name, 'account%s.png' % i))
                # writepass
                touch(250,345)
                pyautogui.typewrite("fityak37!", interval=0.25)
                touch(270,465)
                touch(270, 465)
                wait(.5)
                touch(244,650)
                touch(507,782)
                close_app()
            else:
                close_app()
            touch(**HOME_BUTTON)

    except IOError as err:
        if not IsNoxRunning():
            logger.error("The program can't detect nox , trying to start...")
            StartNoxProcess()
        else:
            TimeIOError += 1
            if TimeIOError > 70:
                TimeIOError = 0
                logger.info("Waiting for nox: Restarting...")
                KillNoxProcess()
            else:
                logger.error("Waiting for nox: %s/%s" % (TimeIOError, 70))
        time.sleep(4)