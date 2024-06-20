import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名簿作成&ランダム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#ffffff"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

names = []


def name():
    name = nameInput.get()  # 入力フィールドから名前を取得
    if name == "":  # 名前が入力されていない場合
        label1.config(text="名前を入力してください。")
    else:  # 名前が入力されていた場合
        names.append(name)  # 名前入力フィールドから名前を取得してnamesのリストに追加
        name_out = ""  # 追加した名前を表示する用の文字列を初期化
        for (
            i
        ) in (
            names
        ):  # forを利用してリストの各名前の後ろに改行コードを入れてname_outに結合
            name_out += f"{i}\n"
        label1.config(text=f"{name_out}\n")  # 結果をラベルに設定して表示させる


def select():
    if len(names) == 0:  # 名前がリストにない場合
        label2.config(text="名前が登録されていません。")
    else:  # 名前がリストにある場合
        # namesの数をrandom.randintの引数に渡して、ランダムに数字を生成
        num = random.randint(0, len(names) - 1)
        label2.config(text=f"{names[num]}")  # ランダムに選ばれた名前を表示


# フィールドの作成
nameInput = tk.Entry(window, bg=fg_color, fg=bg_color)
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
addBtn = tk.Button(window, text="追加", command=name)
randomBtn = tk.Button(window, text="ランダム選択", command=select)

# 出力の作成
nameInput.pack(pady=10)
addBtn.pack(pady=10)
label2.pack()
randomBtn.pack(pady=10)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
