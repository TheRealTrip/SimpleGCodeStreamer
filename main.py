from controllers.presetController import findPresets
from controllers.uiController import mainUI
from controllers.serialController import serialDevice
from tomllib import load


#Load config
config = open('./config.toml', 'rb') # Open as binary format for tomllib
config = load(config)

#Start main routines
presets = findPresets(config['laserType'])
connection = serialDevice(config) # Establish serial connection
UI = mainUI(config, presets, connection)



