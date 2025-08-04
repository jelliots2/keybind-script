import keyboard

print("Press a key (press 'ctrl + 1' to exit)...")

while True:
  event = keyboard.read_event()
  if event.event_type == keyboard.KEY_DOWN:
    print(f"You pressed: {event.name}")
    if event.name == "1" and keyboard.is_pressed("ctrl"):
      print("Exiting program.")
      break