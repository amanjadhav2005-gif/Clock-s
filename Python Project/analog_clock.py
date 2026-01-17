import tkinter as tk
import time
import math

window = tk.Tk()
window.title("Analog Clock (Image)")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# load image (PNG only)
clock_img = tk.PhotoImage(file="clock.png")
canvas.create_image(200, 200, image=clock_img)

center_x = 200
center_y = 200

def draw_hand(length, angle, width, color):
    x = center_x + length * math.sin(angle)
    y = center_y - length * math.cos(angle)
    return canvas.create_line(
        center_x, center_y, x, y,
        width=width, fill=color, tags="hands"
    )

def update_clock():
    canvas.delete("hands")

    now = time.localtime()
    sec = now.tm_sec
    min = now.tm_min
    hour = now.tm_hour % 12

    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(min * 6)
    hour_angle = math.radians(hour * 30 + min * 0.5)

    draw_hand(140, sec_angle, 2, "red")
    draw_hand(120, min_angle, 4, "black")
    draw_hand(90, hour_angle, 6, "black")

    canvas.after(1000, update_clock)

update_clock()
window.mainloop()
