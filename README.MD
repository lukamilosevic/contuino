Contuino project: make arduino controlled games	
========================

---------------
Usage:
```
from contuino import *

board = MyBoard()
board.board_port = 'COM3'
board.baud_rate = 115200
board.server_address = 'x.x.x.x'
board.server_port = ''
board.wifi_ssid = ''
board.wifi_password = ''
board.username = 'testhash'
board.name = 'board name'
board.message = 'board message'

# assign action SHOOT to gpio pin 2
action_digital = GpioAction()
action_digital.event = Events.SHOOT
action_digital.pin = 2
action_digital.sensor = Sensors.TOUCH
action_digital.sensor_code = "XXXX1234"
board.add_action(action_digital)

# assign action SHOOT to analog pin 0
action_analog = GpioAction()
action_analog.event = Events.SHOOT
action_analog.pin = 0
action_analog.analog = True
action_analog.sensor = Sensors.TOUCH
action_analog.sensor_code = "XXXX1234"
board.add_action(action_analog)

# flash micropython
board.flash_micropython()

# deploy and initialize contuino script
board.init_contuino()

# start serial prompt
board.putty_serial_prompt()
```

---------------

features:

flashing micropython  
generating the boot.py script for a board running micropython  
deploying the boot script to the board running micropython  
reading analog and digital sensor input  
sending data to server  
opening putty serial prompt  

---------------

todo:


