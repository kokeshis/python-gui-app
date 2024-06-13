import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#ffffff"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry2.get()
    num3 = int(num1) + int(num2)
    label1.config(text=f"{num1} + {num2}は、 {num3}")  # 画面に出力


def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry2.get()
    num3 = int(num1) - int(num2)
    label1.config(text=f"{num1} - {num2}は、 {num3}")  # 画面に出力


def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry2.get()
    num3 = int(num1) * int(num2)
    label1.config(text=f"{num1} × {num2}は、 {num3}")  # 画面に出力


def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry2.get()
    num3 = int(num1) // int(num2)
    label1.config(text=f"{num1} ÷ {num2}は、 {num3}")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="+", command=button_action1)
button1.pack(pady=10)

button1 = tk.Button(window, text="-", command=button_action2)
button1.pack(pady=10)

button1 = tk.Button(window, text="×", command=button_action3)
button1.pack(pady=10)

button1 = tk.Button(window, text="÷", command=button_action4)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
