import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名簿作成")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#ffffff"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

names = []


def name():  # 関数の定義 ※ボタンが押されたときの動き
    names.append(
        entry1.get()
    )  # 名前入力フィールドから名前を取得してnamesのリストに追加
    name_out = ""  # 追加した名前を表示する用の文字列を初期化
    for (
        i
    ) in names:  # forを使用してリストの各名前の後ろに改行コードを入れてname_outに結合
        name_out += f"{i}\n"
        label2.config(text=f"{name_out}\n")  # 結果をラベルに設定して表示させる


# 入力フィールドの作成
label1 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label1.pack()

entry1 = tk.Entry(window, bg=bg_color, fg=fg_color)  # 名前入力欄
entry1.pack()

# ボタンの作成
button1 = tk.Button(
    window, text="追加", command=name
)  # 名前をnamesのリストに追加するボタン
button1.pack(pady=10)

# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
