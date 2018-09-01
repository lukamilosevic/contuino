import pip
import sys
from subprocess import call
import os
import time

MP_DIR = os.path.dirname(os.path.realpath(__file__)) + os.sep

MICROPYTHON_BIN = MP_DIR + "esp8266-20180511-v1.9.4.bin"

TEMPLATES_FOLDER = MP_DIR + "templates" + os.sep
MAIN_TEMPLATE = TEMPLATES_FOLDER + "main_template.py"

def flash_micropython(port, baud_rate):
    call([sys.executable, '-m', 'esptool', '--port', port, 'erase_flash'])
    call([sys.executable, '-m', 'esptool', '--port', str(port), '--baud', str(baud_rate),
          'write_flash', '--flash_size=detect', '0', MICROPYTHON_BIN])
    time.sleep(5)


def install_ampy():
    print("Installing adafruit-ampy")
    call([sys.executable, '-m', 'pip', 'install', 'adafruit-ampy'])


def install_esptool():
    print("Installing esptool")
    call([sys.executable, '-m', 'pip', 'install', 'esptool'])


def deploy_main(port):
    # print help
    print("Deploying main script to board on port %s" % str(port))
    call(['ampy', '--port', str(port), 'put', MP_DIR + 'main.py'])


def serial_prompt(port):
    print("Running putty serial prompt")
    call(['putty', '-serial', "COM3"])


def generate_main(board_data):
    print("Generating main.py script for the board")
    with open(MAIN_TEMPLATE, "rt") as fin:
        with open(MP_DIR + "main.py", "wt") as fout:
            for line in fin:
                line = line.replace("%_BOARD_DATA_%", board_data)
                fout.write(line)
