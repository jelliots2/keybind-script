import ctypes
import keyboard
import time
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image

VK_MEDIA_PLAY_PAUSE = 0xB3
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002

last_trigger_time = 0
cooldown_seconds = 0.3
running = True

def send_media_key(vk_code):
  global last_trigger_time
  current_time = time.time()
  
  if current_time - last_trigger_time < cooldown_seconds:
    return # too soon since last trigger
  
  last_trigger_time = current_time
  ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_EXTENDEDKEY, 0)
  time.sleep(0.05)
  ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
  
def keyboard_listener():  
  keyboard.on_press_key('pause', lambda _: send_media_key(VK_MEDIA_PLAY_PAUSE))
  keyboard.wait()

def on_exit(icon, _):
  icon.stop()
  keyboard.unhook_all()
  global running
  running = False

def setup_tray():
  image = Image.open("C:/Users/jelli/scripts/playpauseicon.png")
  menu = Menu(MenuItem('Exit', on_exit))
  tray_icon = Icon("PlayPause", image, "Play Pause Keybind", menu)
  tray_icon.run()
  
threading.Thread(target=keyboard_listener, daemon=True).start()

setup_tray()