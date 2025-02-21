import serial, os
from controllers.uiController import grabPositionState


class serialDevice():
    def __init__(self, device, baudRate, demoMode, movePrefix, inverseX, inverseY, usePySerial):
        self.device = device
        self.baudRate = baudRate
        self.demoMode = demoMode
        self.movePrefix = movePrefix
        self.inverseX = inverseX
        self.inverseY = inverseY
        self.usePySerial = usePySerial
        self.ui = None
        if not self.demoMode:
            self.sercon = serial.Serial()
            self.sercon.port = device
            self.sercon.baudrate = baudRate
        else:
            print("Demo Mode is active, not establishing a connection.")
    def sendSerialCommand(self, command):
        if not self.demoMode:
            if not self.usePySerial:
                os.system(f'echo {command} >> {self.device}')
                print(f"Sending {command}")
            else:
                self.sercon.write(command)
        else:
            print(f"Sending {command}")

    def move(self, direction, step):
        if grabPositionState():
            self.ui.togglePositioning()
        if self.inverseX and (direction == "left" or direction == "right"):
            step = -step
        if self.inverseY and (direction == "up" or direction == "down"):
            step = -step
        match direction:
            case 'up':
                    self.sendSerialCommand(f"{self.movePrefix}Y{step}")
            case 'down':
                    self.sendSerialCommand(f"{self.movePrefix}Y{-step}")
            case 'left':
                    self.sendSerialCommand(f"{self.movePrefix}X{-step}")
            case 'right':
                    self.sendSerialCommand(f"{self.movePrefix}X{step}")
    def goTo(self, x, y):
        if not grabPositionState():
            self.ui.togglePositioning()
        if inverseX:
            x = -x
        if inverseY:
            y = -y
        self.sendSerialCommand(f"G90X{x}Y{y}")
    def goHome(self):
        self.sendSerialCommand('G28')
