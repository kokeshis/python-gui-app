import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#ffffff"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

a = [
    "tkinter",
    "geometry",
    "widgets",
    "messagebox",
    "configure",
    "label",
    "column",
    "rowspan",
    "grid",
    "init",
]


def button_action1():
    num = entry1.get().strip()
    if num in a:
        label1.config(text="正解！")
        update_random_word()
        entry1.delete(0, "end")
    else:
        label1.config(text="不正解！")


def update_random_word():
    random_word = random.choice(a)
    label1.config(text=random_word)


# 出力ラベルの作成
label1 = tk.Label(window, text="aiueo", bg=bg_color, fg=fg_color)
label1.pack(pady=10)
update_random_word()

# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action1)
button1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
