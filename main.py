from controllers.presetController import findPresets
from controllers.uiController import mainUI
from controllers.serialController import serialDevice


boolDict = { # python i don't like you
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
            demoMode = boolDict[parameter]
        case 'windowDimensions':
            dimensions = str(parameter)
        case 'inverseX':
            inverseX = boolDict[parameter]
        case 'usePySerial':
            usePySerial = boolDict[parameter]
        case 'inverseY':
            inverseY = boolDict[parameter]

file.close()


presets = findPresets()

connection = serialDevice(device, baudRate, demoMode, movePrefix, inverseX, inverseY, usePySerial) # Establish serial connection
UI = mainUI(dimensions, presets, connection)



