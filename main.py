from controllers.presetController import findPresets
from mainUI import mainUI
from controllers.serialController import serialDevice


horribleDict = { # python i don't like you
    "True": True,
    "False": False
}


file = open('./config.txt', 'r')
lines = file.readlines()
for line in lines:
    parameterName = line.split(':')[0]
    parameter = line.split(':')[1].strip(' ').strip('\n')
    match parameterName:
        case 'device':
            device = parameter
        case 'baudRate':
            baudRate = int(parameter)
        case 'movePrefix':
            movePrefix = parameter
        case 'demoMode':
            demoMode = horribleDict[parameter]
        case 'windowDimensions':
            dimensions = str(parameter)
file.close()
UI = None
connection = serialDevice(device, baudRate, demoMode, movePrefix, UI) # Establish serial connection
presets = findPresets()
UI = mainUI(dimensions, presets, connection)



