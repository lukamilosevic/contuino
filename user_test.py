from contuino import *

# game(ip)

board = MyBoard()
board.board_port = 'COM3'
board.baud_rate = 460800
board.server_address = '192.168.5.16'
board.server_port = '5000'
board.wifi_ssid = ''
board.wifi_password = ''
board.user_hash = 'testhash'
board.name = 'board name'
board.message = 'board message'

action_analog = GpioAction()
action_analog.event = Events.SHOOT
action_analog.pin = 0
action_analog.analog = True
action_analog.sensor = Sensors.TOUCH
action_analog.sensor_code = "XXXX1234"

action_digital = GpioAction()
action_digital.event = Events.SHOOT
action_digital.pin = 2
action_digital.sensor = Sensors.TOUCH
action_digital.sensor_code = "XXXX1234"

board.add_action(action_analog)
board.add_action(action_digital)

board.flash_micropython()

board.init_contuino()

board.putty_serial_prompt()

#passed