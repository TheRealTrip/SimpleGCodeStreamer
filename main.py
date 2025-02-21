from controllers.presetController import findPresets
from controllers.uiController import mainUI
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
        case 'inverseX':
            inverseX = horribleDict[parameter]
        case 'usePySerial':
            usePySerial = horribleDict[parameter]
        case 'inverseY':
            inverseY = horribleDict[parameter]

file.close()


presets = findPresets()

connection = serialDevice(device, baudRate, demoMode, movePrefix, inverseX, inverseY, usePySerial) # Establish serial connection
UI = mainUI(dimensions, presets, connection)



