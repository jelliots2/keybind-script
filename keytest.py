import keyboard

print("Press a key (press 'ctrl + c' to exit)...")

while True:
  event = keyboard.read_event()
  if event.event_type == keyboard.KEY_DOWN:
    print(f"You pressed: {event.name}")
    if event.name == "c" and keyboard.is_pressed("ctrl"):
      print("Exiting program.")
      break