import serial
from functools import partial
from mainUI import grabPositionState

class serialDevice():
    def __init__(self, device, baudRate, demoMode, movePrefix):
        self.device = device
        self.baudRate = baudRate
        self.demoMode = demoMode
        self.movePrefix = movePrefix
        self.ui = None
        if not self.demoMode:
            self.sercon = serial.Serial() # I don't actually use this connection to send data as it dosen't work? I use os.system instead. I don't know if it's still necessary to let the control computer I want to write to it.
            self.sercon.port = device
            self.sercon.baudrate = baudRate
        else:
            print("Demo Mode is active, not establishing a connection.")
    def sendSerialCommand(self, command):
        if not self.demoMode:
            os.system(f'echo {command} >> {device}')
            print(f"Sending {command}")
        else:
            print(f"Sending {command}")

    def move(self, direction, step):
        if grabPositionState():
            self.ui.togglePositioning()
        match direction:
            case 'up':
                self.sendSerialCommand(f"{self.movePrefix}Y{step}")
            case 'down':
                self.sendSerialCommand(f"{self.movePrefix}Y{-step}")
            case 'left':
                self.sendSerialCommand(f"{self.movePrefix}X{step}")
            case 'right':
                self.sendSerialCommand(f"{self.movePrefix}X{-step}")
    def goTo(self, x, y):
        if not grabPositionState():
            self.ui.togglePositioning()
        self.sendSerialCommand(f"G90X{-x}Y{y}")
    def goHome(self):
        self.sendSerialCommand('G28')
