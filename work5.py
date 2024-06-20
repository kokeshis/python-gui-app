import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#ffffff"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():
    num = str((entry1.get()))
    if num == "aiueo":
        label1.config(text="正解！")
    else:
        label1.config(text="不正解！")


# 出力ラベルの作成
label1 = tk.Label(window, text="aiueo", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# 入力フィールドの作成
entry1 = tk.Entry(text="aiueo", bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action1)
button1.pack(pady=10)

# button1 = tk.Button(window, text="-", command=button_action2)
# button1.pack(pady=10)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
