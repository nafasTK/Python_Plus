
import colorsys
import tkinter as tk

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#') 
    
    r = int(hex_color[0:2], 16) 
    g = int(hex_color[2:4], 16) 
    b = int(hex_color[4:6], 16) 
    
    return (r, g, b)


print("🎨 Color Box 🎨")
color1_hex = input("Enter your first color code: ")
color2_hex = input("Enter your second color code: ")

while True:
    try:
        ratio_text = input("How much of your first color do you want?(between 0.0 and 1.0): ")
        mix_ratio = float(ratio_text)
        if 0.0 <= mix_ratio <= 1.0:
            break
        else:
            print("❗ It must be a number between 0.0 and 1.0. Please try again.")
    except ValueError:
        print("❗ Invalid input! Please enter a number.")


r1, g1, b1 = hex_to_rgb(color1_hex)
r2, g2, b2 = hex_to_rgb(color2_hex)


hsv1 = colorsys.rgb_to_hsv(r1 / 255, g1 / 255, b1 / 255)
hsv2 = colorsys.rgb_to_hsv(r2 / 255, g2 / 255, b2 / 255)


mixed_h = mix_ratio * hsv1[0] + (1 - mix_ratio) * hsv2[0]
mixed_s = mix_ratio * hsv1[1] + (1 - mix_ratio) * hsv2[1]
mixed_v = mix_ratio * hsv1[2] + (1 - mix_ratio) * hsv2[2]


mixed_rgb_normalized = colorsys.hsv_to_rgb(mixed_h, mixed_s, mixed_v)

final_r = int(mixed_rgb_normalized[0] * 255)
final_g = int(mixed_rgb_normalized[1] * 255)
final_b = int(mixed_rgb_normalized[2] * 255)

final_r = max(0, min(255, final_r))
final_g = max(0, min(255, final_g))
final_b = max(0, min(255, final_b))

final_rgb_tuple = (final_r, final_g, final_b)


final_hex_color = f"#{final_rgb_tuple[0]:02X}{final_rgb_tuple[1]:02X}{final_rgb_tuple[2]:02X}"


print(f"\nYour new color (in computer language): {final_rgb_tuple}")
print(f"Your new color (like a color code): {final_hex_color}")


painting_window = tk.Tk()
painting_window.title("Here's Your New Color!")
painting_window.geometry("300x150")

color_display_label = tk.Label(painting_window, 
                                 text="Mixed Color", 
                                 bg=final_hex_color, 
                                 font=("Arial", 20), 
                                 fg="white")

color_display_label.pack(expand=True, fill="both")

painting_window.mainloop()
