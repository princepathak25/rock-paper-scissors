# 🎮 Rock, Paper, Scissors - GUI Version by Prince 💛
import tkinter as tk
import random

# 🌟 Game logic
def play(user_choice):
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)

    result_text.set(f"🧠 Computer chose: {comp_choice.capitalize()}")

    if user_choice == comp_choice:
        outcome = "🤝 It's a tie!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        outcome = "🎉 You Win!"
    else:
        outcome = "💔 You Lose!"

    result_text.set(f"🧠 Computer chose: {comp_choice.capitalize()}\n{outcome}")

# 🔁 Reset the game
def reset():
    result_text.set("🤖 Make your move!")

# 🖼 GUI Setup
window = tk.Tk()
window.title("🪨📄✂️ Rock Paper Scissors - Prince Edition")
window.config(bg="#1e1e1e")
window.geometry("400x450")

# 🧾 Header
title = tk.Label(window, text="🎮 Rock • Paper • Scissors 🎮", font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#00ffff")
title.pack(pady=20)

# 🔁 Result display
result_text = tk.StringVar()
result_text.set("🤖 Make your move!")
result_label = tk.Label(window, textvariable=result_text, font=("Segoe UI", 14), bg="#2d2d2d", fg="white", width=35, height=3, wraplength=300, relief="ridge", bd=2)
result_label.pack(pady=10)

# 🧱 Buttons
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=10)

choices = [("🪨 Rock", "rock"), ("📄 Paper", "paper"), ("✂️ Scissors", "scissors")]
for emoji_text, value in choices:
    btn = tk.Button(button_frame, text=emoji_text, font=("Segoe UI", 14), width=12, bg="#444", fg="white",
                    activebackground="#888", relief="raised", command=lambda val=value: play(val))
    btn.pack(side='left', padx=10)

# 🔁 Reset Button
tk.Button(window, text="🔁 Play Again", font=("Segoe UI", 12), bg="#00cc66", fg="white",
          command=reset).pack(pady=20)

# 👋 Exit
tk.Button(window, text="🚪 Exit", font=("Segoe UI", 12), bg="#cc0000", fg="white",
          command=window.destroy).pack()

window.mainloop()
