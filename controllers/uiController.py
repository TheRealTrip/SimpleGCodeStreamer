import tkinter as tk
absolute_positioning = False

def grabPositionState():
    return absolute_positioning

class mainUI():
    def __init__(self, dimensions, presets, connection):
        self.root = tk.Tk()
        self.root.title("Laser Controller")
        self.root.geometry(dimensions)
        self.connection = connection
        connection.ui = self

        # Create buttons and associate them with the move function
        btn_up = tk.Button(self.root, text="Up", command=lambda: self.connection.move("up", step))
        btn_down = tk.Button(self.root, text="Down", command=lambda: self.connection.move("down", step) )
        btn_left = tk.Button(self.root, text="Left", command=lambda: self.connection.move("left", step) )
        btn_right = tk.Button(self.root, text="Right", command=lambda: self.connection.move("right", step) )


        #Getting the step distance for relative motion
        stepBox = tk.Text(self.root, width=4, height=1)
        stepBox.insert("1.0", "5")
        stepLabel = tk.Label(self.root, text="Enter step (in mm)")

        #Getting coordinates for absolute motion
        xCoordBox = tk.Text(self.root, width=3, height=1)
        yCoordBox = tk.Text(self.root, width=3, height=1)
        xCoordLabel = tk.Label(self.root, text="X-Coord")
        yCoordLabel = tk.Label(self.root, text="Y-Coord")
        goToButton = tk.Button(self.root, text="Go To", command=lambda: self.connection.goTo(int(xCoordBox.get("1.0", "end-1c")), y = int(yCoordBox.get("1.0", "end-1c"))))

        #Home Button
        homeButton = tk.Button(self.root, text="Home", command=lambda: self.connection.goHome())


        # Arrange the buttons in a grid
        btn_up.grid(row=0, column=1, pady=10)
        btn_left.grid(row=1, column=0, padx=10)
        btn_right.grid(row=1, column=2, padx=10)
        btn_down.grid(row=2, column=1, pady=10)
        homeButton.grid(row=1, column=1, pady=10)


        # Button to toggle positioning mode
        self.positonToggle = tk.Button(self.root, text="Absolute", command=lambda: self.togglePositioning())
        self.positonToggle.grid(row=3, column=1, pady=10)

        stepBox.grid(row=5, column=1, pady=10)
        stepLabel.grid(row=4, column=1, pady=10)

        xCoordBox.grid(row=7, column=0, pady=10)
        yCoordBox.grid(row=7, column=1, pady=10)
        xCoordLabel.grid(row=6, column=0, pady=10)
        yCoordLabel.grid(row=6, column=1, pady=10)

        goToButton.grid(row=7, column=2, pady=10)


        step = int(stepBox.get("1.0", "end-1c"))

        for i, preset in enumerate(presets):
            button = tk.Button(self.root, text=preset.name, command=lambda p=preset: p.goToPreset(connection))
            button.grid(row=i, column=10, pady=5)


        # Start the main event loop
        self.root.mainloop()
    def togglePositioning(self):
        global absolute_positioning
        absolute_positioning = not absolute_positioning
        self.positonToggle["text"] = "Absolute" if absolute_positioning else "Relative"
        mode = "G90" if absolute_positioning else "G91"
        self.connection.sendSerialCommand(mode)
        print(f"Positioning mode: {'Absolute' if absolute_positioning else 'Relative'}")
