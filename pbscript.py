import ctypes
import keyboard
import time

VK_MEDIA_PLAY_PAUSE = 0xB3
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002

last_trigger_time = 0
cooldown_seconds = 0.3

def send_media_key(vk_code):
  global last_trigger_time
  current_time = time.time()
  
  if current_time - last_trigger_time < cooldown_seconds:
    return # too soon since last trigger
  
  last_trigger_time = current_time
  
  ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_EXTENDEDKEY, 0)
  time.sleep(0.05)
  ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
  
keyboard.add_hotkey('pause', lambda: send_media_key(VK_MEDIA_PLAY_PAUSE))

keyboard.wait()