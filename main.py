# main.py
import pyautogui as pag
import random
import time
import keyboard

def stop_requested():
    return keyboard.is_pressed("esc") or keyboard.is_pressed("space")

def tiny_mouse_movement():
    while True:
        if stop_requested():
            break

        # Move just a few pixels in random direction
        dx = random.uniform(-5, 5)  # X shift: -5 to +5 pixels
        dy = random.uniform(-5, 5)  # Y shift: -5 to +5 pixels

        pag.moveRel(dx, dy, duration=0.2)  # short smooth movement

        # Random short pause before next nudge
        pause_time = random.uniform(2, 5)
        elapsed = 0
        while elapsed < pause_time:
            if stop_requested():
                return
            time.sleep(0.05)
            elapsed += 0.05

if __name__ == "__main__":
    tiny_mouse_movement()
