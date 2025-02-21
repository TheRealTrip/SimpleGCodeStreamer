# GCode Streamer

## Who is this for?
It is mostly for me but I can't see why it couldn't be adapted to your use-case. 
One thing to keep in mind is that left and rights are swapped from standard GCode due to my hardware, however I will be adding this to the config soon.
In it's current state it only functions for Linux machines due to how it sends serial commands. However it could easily be adapted for other platforms.

## Usage
Pull the repo down and then run
`python -m pip install -r requirements.txt`
Then
`cp example_config.txt config.txt`

After filling out the config you have the option to make more presets than already provided, this is trivial and just requires you to follow the format. The file name will be what's displayed in the UI, including the extension.
`
X\nY
`

Then simply run main.py