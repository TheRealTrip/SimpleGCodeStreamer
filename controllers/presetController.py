import os
if not os.path.exists('presets'): # Ensure presets folder exists
   os.makedirs('presets')


class preset():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    def goToPreset(self, connection):
        connection.goTo(self.x, self.y)
    def saveToFile(self, name):
        with open(name, 'w') as file:
            file.write(f"{self.x}\n{self.y}")
            file.close()


def presetFromFile(name, laser):
    with open(f"./presets/{laser}/{name}", 'r') as file:
        lines = file.readlines()
        x = int(lines[0])
        y = int(lines[1])
        file.close()
    return preset(x, y, name)


def findPresets(laser):
    # Searching for presets and storing in memory
    presets = []
    for file in os.listdir(f'./presets/{laser}'):
        Preset = presetFromFile(os.fsdecode(file), laser)
        presets.append(Preset)
    return presets



