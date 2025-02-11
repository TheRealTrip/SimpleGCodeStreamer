import tkinter as tk
import serial, time, os

device = "/dev/ttyUSB0" # Dynamic, ensure this is up to date, eg - (/dev/tty/USB0 /dev/tty/ACM0)
baudRate = 115200
movePrefix = "G0" 
demoMode = False
absolute_positioning = False


class serialDevice():
    def __init__(self, device, baudRate):
        self.device = device
        self.baudRate = baudRate
        if not demoMode:
            self.sercon = serial.Serial()
            self.sercon.port = device
            self.sercon.baudrate = baudRate
            self.sercon.setDTR(1)
            print(self.sercon)
            self.sercon.open()
            self.sercon.setDTR(0)
            time.sleep(0.5)
            self.sercon.setDTR(1)
        else:
            print("Demo Mode is active, not establishing a connection.")
    def sendSerialCommand(self, command):
        if not demoMode:
            #self.sercon.write(command.encode())
            os.system(f'echo {command} >> {device}')
            #self.fixIt()
            #self.sercon.write(command.encode())
            print(f"Sending {command}")
        else:
            print(f"Sending {command}")

    def move(self, direction):
        if absolute_positioning:
            self.toggle_positioning()
        step = int(stepBox.get("1.0", "end-1c"))
        match direction:
            case 'up':
                self.sendSerialCommand(f"{movePrefix}Y{step}")
            case 'down':
                self.sendSerialCommand(f"{movePrefix}Y{-step}")
            case 'left':
                self.sendSerialCommand(f"{movePrefix}X{step}")
            case 'right':
                self.sendSerialCommand(f"{movePrefix}X{-step}")
    def goTo(self):
        if not absolute_positioning:
            self.toggle_positioning()
        x = int(xCoordBox.get("1.0", "end-1c"))
        y = int(yCoordBox.get("1.0", "end-1c"))
        self.sendSerialCommand(f"G90X{-x}Y{y}")
    def toggle_positioning(self):
        global absolute_positioning
        absolute_positioning = not absolute_positioning
        btn_toggle["text"] = "Absolute" if absolute_positioning else "Relative"
        mode = "G90" if absolute_positioning else "G91"
        self.sendSerialCommand(mode)
        print(f"Positioning mode: {'Absolute' if absolute_positioning else 'Relative'}")
    def goHome(self):
        #self.sendSerialCommand('G0 X0 Y0')
        self.sendSerialCommand('G28')
    def goToPreset(self, preset):
        self.sendSerialCommand(f"G3X{preset.x}Y{preset.y}")

class gCodeCommand():
    def __init__(self, command):
        self.command = command
    def saveToFile(name):
        with open(name, 'w') as file:
            file.write(self.command)
            file.close()

def loadGCodeFromFile(name):
    with open(name, 'r') as file:
        command = file.read()
        file.close()
    return gCodeCommand(command)

class preset():
    def __init__(self, x, y):
        self.x = x
        self.y = y



connection = serialDevice(device, baudRate) # Establish serial connection

root = tk.Tk()
root.title("Laser Controller")
root.geometry("500x500")

# Create buttons and associate them with the move function
btn_up = tk.Button(root, text="Up", command=lambda: connection.move("up") )
btn_down = tk.Button(root, text="Down", command=lambda: connection.move("down") )
btn_left = tk.Button(root, text="Left", command=lambda: connection.move("left") )
btn_right = tk.Button(root, text="Right", command=lambda: connection.move("right") )

# Button to toggle positioning mode
btn_toggle = tk.Button(root, text="Absolute", command=connection.toggle_positioning)

#Getting the step distance for relative motion
stepBox = tk.Text(root, width=4, height=1)
stepBox.insert("1.0", "5")
stepLabel = tk.Label(root, text="Enter step (in mm)")

#Getting coordinates for absolute motion
xCoordBox = tk.Text(root, width=3, height=1)
yCoordBox = tk.Text(root, width=3, height=1)
xCoordLabel = tk.Label(root, text="X-Coord")
yCoordLabel = tk.Label(root, text="Y-Coord")
goToButton = tk.Button(root, text="Go To", command=lambda: connection.goTo())

#Home Button
homeButton = tk.Button(root, text="Home", command=lambda: connection.goHome())


# Arrange the buttons in a grid
btn_up.grid(row=0, column=1, pady=10)
btn_left.grid(row=1, column=0, padx=10)
btn_right.grid(row=1, column=2, padx=10)
btn_down.grid(row=2, column=1, pady=10)
btn_toggle.grid(row=3, column=1, pady=10)
stepBox.grid(row=5, column=1, pady=10)
stepLabel.grid(row=4, column=1, pady=10)
xCoordBox.grid(row=7, column=0, pady=10)
yCoordBox.grid(row=7, column=1, pady=10)
xCoordLabel.grid(row=6, column=0, pady=10)
yCoordLabel.grid(row=6, column=1, pady=10)
goToButton.grid(row=7, column=2, pady=10)
homeButton.grid(row=1, column=1, pady=10)
# Start the main event loop
root.mainloop()
