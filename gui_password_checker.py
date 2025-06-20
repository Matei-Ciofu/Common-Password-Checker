import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from password_checker import password_strength, load_common_passwords

def analizza_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Attenzione", "Inserisci una password.")
        return

    strength, entropy, feedback = password_strength(password, common_passwords)

    feedback_text = f"Forza della password: {strength}\nEntropia: {entropy} bit\n"
    if feedback:
        feedback_text += "\nSuggerimenti:\n" + "\n".join(f"- {f}" for f in feedback)
    else:
        feedback_text += "\nPassword solida! "
    output_label.config(text=feedback_text)

    if "Debole" in strength:
        progress["value"] = 25
        progress.configure(style="Red.Horizontal.TProgressbar")
    elif "Media" in strength:
        progress["value"] = 60
        progress.configure(style="Yellow.Horizontal.TProgressbar")
    else:
        progress["value"] = 100
        progress.configure(style="Green.Horizontal.TProgressbar")

# Mostra/Nascondi password
def toggle_password_visibility():
    global password_visible
    if password_visible:
        entry.config(show="*")
        toggle_button.config(text="👁 Mostra password")
        password_visible = False
    else:
        entry.config(show="")
        toggle_button.config(text=" Nascondi password")
        password_visible = True

# Setup iniziale
common_passwords = load_common_passwords()
password_visible = False

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x370")
root.resizable(False, False)

style = ttk.Style()
style.theme_use('default')
style.configure("Red.Horizontal.TProgressbar", troughcolor='white', background='red')
style.configure("Yellow.Horizontal.TProgressbar", troughcolor='white', background='orange')
style.configure("Green.Horizontal.TProgressbar", troughcolor='white', background='green')

# UI Layout
title = tk.Label(root, text=" Password Strength Checker", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Helvetica", 12))
entry.pack(pady=5)

toggle_button = tk.Button(root, text="👁 Mostra password", command=toggle_password_visibility, font=("Helvetica", 10))
toggle_button.pack(pady=2)

check_button = tk.Button(root, text="Analizza", command=analizza_password, bg="#007acc", fg="white", font=("Helvetica", 12))
check_button.pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

output_label = tk.Label(root, text="", wraplength=350, justify="left", font=("Helvetica", 11))
output_label.pack(padx=10, pady=10)

root.mainloop()
