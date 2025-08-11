
# MEDIA KEYBIND

A simple media keybind script I am creating for use with keyboards that lack proper media keys. If you use AutoHotKey to bind buttons, this may be a good alternative for you. In my case, I use AutoHotKey to bind the PB button on my 60% keyboard to be a media key that can play/pause videos, music etc. Since I tend to watch YouTube videos or listen to music while I'm playing video games, I've run into an issue. Most anti-cheats these days will prevent certain games from launching if AutoHotKey is running. In my case, I cannot play Battlefield or The Finals if I'm running AutoHotKey. Sometimes I want to play games casually and enjoy background music or watch videos on the side. To solve this issue, I am creating this simple Python script to test with these games and attempt to have my media key binding without interfering with anti-cheat in games. 


## Authors

- Me [@jelliots2](https://github.com/jelliots2)


## Features

- Binds PB button to act as a Media Play Pause key in Windows.
- You can edit this to bind whatever keys for whatever actions, just change the key code in the script.

## Easy Install
The exe is in the Dist folder. Pretty sure you can just download and run it. It will show up in your application tray. 
To make it run on startup, Win + R (Run), type "shell:startup" and past the exe, or a shortcut to the exe in that folder.

## Instructions
For if you want to download the whole application (ie if you want to change or test it)
pip install the dependencies: keyboard, pystray, ctypes, time, threading, pyinstaller.
Create EXE using pyinstaller, or download the exe from here.

## DISCLAIMER
This, like most of my projects, is open source. You can download it and use it as you like. All I ask is that you DO NOT modify this script to behave as a macro for cheating in games. Obviously, if you wanted to do that you'd have figured it out already. 
