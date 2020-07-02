# GitActionFileHelper
Just a small little script to replace keywords in a given workflow file. Great for quickly setting up default workflows.

## Prerequisites
- Python runtime available on your environment variables

## Steps to use while modifying code

1. Open a terminal, if inside Eclipse and you have the CodeMix plugin, follow step 2 and 3, otherwise skip to step 4
2. From the `Quick Open`  Command Palette (ctrl/cmd + shift + p) search for:
     `Terminal: Create New Integrated Terminal`
3. From the `Quick Open` options select this project.
4. Once you are inside the Terminal, execute: `python src/hello-world.py`

### Important note
- A recent windows 10 update has made it so by default when you use the `python` command, it redirects you to the Windows Store instead of executing python, even if you have the python exe on your system PATH. To fix this, either remove the WindowsApps folder from your PATH or go to `Apps & Features` of your windows settings, click on `App execution aliases` and disable the `App Installer` with the sub texts of `python.exe` and `python3.exe`

## Steps to use anywhere
1. Download one of the release versions
2. Extract `actionhelper.zip` to whereever you'd like. If you have a folder already on your system path, great, if not, perhaps make a folder `C://actionhelper`
3. Ensure where ever you extracted the zip to is on your system path
4. Open up a command prompt / terminal and run the command `actionhelper -h` to get started