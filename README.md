# GCode Streamer

## Who is this for?
It is mostly for me but I can't see why it couldn't be adapted to your use-case. 
## Usage

### From Source
Pull the repo down and then run
`python -m pip install -r requirements.txt`

### From Source
Grab a recent release for your OS and run as normal, probably in a CMD window as it can help with troubleshooting.

Then
`cp example_config.toml config.toml`


After filling out the config you have the option to make more presets than already provided, this is trivial and just requires you to follow the format. The file name will be what's displayed in the UI, including the extension.
`
X\nY
`
![Graphic to illustrate the file structure](https://cdn.discordapp.com/attachments/955529298654146601/1356353370364842194/graphics.jpg?ex=67ec4203&is=67eaf083&hm=ddf41adadac4d454c0a56aa99280e27303d2939c4a6bfb62746d403ba15bc5d1&)


Then simply run main.py

# To Do List


- Create a new Laser Object which stores presets for ease of use