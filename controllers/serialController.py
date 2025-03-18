import serial, os


class serialDevice():
    def __init__(self, config):
        self.config = config
        self.device = config['device']
        self.baudRate = config['baudRate']
        self.demoMode = config['demoMode']
        self.movePrefix = config['movePrefix']
        self.inverseX = config['inverseX']
        self.inverseY = config['inverseY']
        self.usePySerial = config['usePySerial']
        self.offsetX = config['offsetX']
        self.offsetY = config['offsetY']
        self.ui = None
        self.usableX = config['usableX']
        self.usableY = config['usableY']
        if not self.demoMode:
            self.sercon = serial.Serial()
            self.sercon.port = self.device
            self.sercon.baudrate = self.baudRate
            self.sercon.open()
        else:
            print("Demo Mode is active, not establishing a connection.")
    def sendSerialCommand(self, command):
        if not self.demoMode:
            if not self.usePySerial:
                os.system(f'echo {command} >> {self.device}')
                print(f"Sending {command}")
            else:
                command = ('\r' + command + '\r').encode()
                self.sercon.write(command)
        else:
            print(f"Sending {command}")
    def move(self, direction, step):
        self.ui.setPositioning('relative')
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
        self.ui.setPositioning('absolute')
        x = x + int(self.offsetX)
        y = y + int(self.offsetY)
        if self.inverseX:
            x = -x
        if self.inverseY:
            y = -y
        self.sendSerialCommand(f"G90X{x}Y{y}")
    def goHome(self):
        self.sendSerialCommand('G28')
    def scanArea(self):
        xSteps = int(int(self.usableX) / 10)
        ySteps = int(int(self.usableY) / 10)
        print(xSteps, ySteps)
        for ystep in range(0,ySteps):
            for xstep in range(0,xSteps):
                if (ystep % 2) > 0:
                    self.move('left', 10)
                else:
                    self.move('right', 10)
            self.move('up', 10)
        self.goHome()
