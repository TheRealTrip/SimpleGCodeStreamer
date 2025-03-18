import tkinter as tk


class mainUI():
    def __init__(self, config, presets, connection):
        self.config = config
        self.root = tk.Tk()
        self.root.title("Laser Controller")
        self.root.geometry(config['windowDimensions'])
        self.usableX = config['usableX']
        self.usableY = config['usableY']
        self.connection = connection
        connection.ui = self # Fixes circular import

        if self.config['defaultPositioning'] == 'relative':
            self.absolute_positioning = False
        else:
            self.absolute_positioning = True

        # Create buttons and associate them with the move function
        btn_up = tk.Button(self.root, text="Up", command=lambda: self.connection.move("up", int(self.removeNonIntegers(stepBox.get("1.0", "end-1c")))))
        btn_down = tk.Button(self.root, text="Down", command=lambda: self.connection.move("down", int(self.removeNonIntegers(stepBox.get("1.0", "end-1c")))) )
        btn_left = tk.Button(self.root, text="Left", command=lambda: self.connection.move("left", int(self.removeNonIntegers(stepBox.get("1.0", "end-1c")))) )
        btn_right = tk.Button(self.root, text="Right", command=lambda: self.connection.move("right", int(self.removeNonIntegers(stepBox.get("1.0", "end-1c")))) )


        #Getting the step distance for relative motion
        stepBox = tk.Text(self.root, width=4, height=1)
        stepBox.insert("1.0", "5")
        stepLabel = tk.Label(self.root, text="Enter step (in mm)")

        #Getting coordinates for absolute motion
        xCoordBox = tk.Text(self.root, width=3, height=1)
        yCoordBox = tk.Text(self.root, width=3, height=1)
        xCoordLabel = tk.Label(self.root, text="X-Coord")
        yCoordLabel = tk.Label(self.root, text="Y-Coord")
        goToButton = tk.Button(self.root, text="Go To", command=lambda: self.connection.goTo(int(self.removeNonIntegers(xCoordBox.get("1.0", "end-1c"))), y = int(self.removeNonIntegers(yCoordBox.get("1.0", "end-1c")))))

        #Home Button
        homeButton = tk.Button(self.root, text="Home", command=lambda: self.connection.goHome())

        usableSpace = tk.Label(self.root, text=f"Usable space is {self.usableX}x{self.usableY}")

        # Arrange the buttons in a grid
        btn_up.grid(row=0, column=1, pady=10)
        btn_left.grid(row=1, column=0, padx=10)
        btn_right.grid(row=1, column=2, padx=10)
        btn_down.grid(row=2, column=1, pady=10)
        homeButton.grid(row=1, column=1, pady=10)


        # Button to toggle positioning mode
        self.positionToggle = tk.Button(self.root, text="Absolute", command=lambda: self.togglePositioning())
        self.positionToggle.grid(row=3, column=1, pady=10)

        stepBox.grid(row=5, column=1, pady=10)
        stepLabel.grid(row=4, column=1, pady=10)

        xCoordBox.grid(row=8, column=0, pady=10)
        yCoordBox.grid(row=8, column=1, pady=10)
        usableSpace.grid(row=7, column=0, pady=10)
        xCoordLabel.grid(row=6, column=0, pady=10)
        yCoordLabel.grid(row=6, column=1, pady=10)

        goToButton.grid(row=8, column=2, pady=10)

        scanAreaButton = tk.Button(self.root, text="Start Scan", command=lambda: connection.scanArea())
        scanAreaButton.grid(row=0, column=4)


        for i, preset in enumerate(presets): # Adding all the presets to the UI
            button = tk.Button(self.root, text=preset.name, command=lambda p=preset: p.goToPreset(connection))
            button.grid(row=i, column=10, pady=5)


        # Start the main event loop
        self.root.mainloop()
    def setPositioning(self, positioning):
        if positioning == 'relative' and (not self.absolute_positioning):
            return
        if positioning == 'absolute' and self.absolute_positioning:
            return
        self.absolute_positioning = not self.absolute_positioning
        self.positionToggle["text"] = "Absolute" if self.absolute_positioning else "Relative"
        mode = "G90" if self.absolute_positioning else "G91"
        self.connection.sendSerialCommand(mode)
        print(f"Positioning mode: {'Absolute' if self.absolute_positioning else 'Relative'}")
    def togglePositioning(self):
        if self.absolute_positioning:
            self.setPositioning('relative')
        else:
            self.setPositioning('absolute')
    def removeNonIntegers(self, input_string):
        result = ''.join([char for char in input_string if char.isdigit()])
        return result