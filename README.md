# GCode Streamer

## Who is this for?
It is mostly for me but I can't see why it couldn't be adapted to your use-case. 
## Usage
Pull the repo down and then run
`python -m pip install -r requirements.txt`
Then
`cp example_config.toml config.toml`

After filling out the config you have the option to make more presets than already provided, this is trivial and just requires you to follow the format. The file name will be what's displayed in the UI, including the extension.
`
X\nY
`

Then simply run main.py

# To Do List

- X and Y Offset in config.toml
- Create a new Laser Object which stores presets for ease of use