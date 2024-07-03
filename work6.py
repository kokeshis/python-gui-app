import tkinter as tk
import tkinter.messagebox as messagebox
import random

window = tk.Tk()
window.title("GUI App")
window.geometry("300x300")
bg_color = "#333333"
fg_color = "#ffffff"
window.configure(bg=bg_color)

# ゲームの初期状態を設定する二次元リスト
initial_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 現在のゲームの状態を管理する二次元リスト
game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 勝利条件をチェックする関数
def check_winner():
    # 横のチェック
    for row in game_board:
        if all([cell == "◯" for cell in row]):
            return "◯"
        elif all([cell == "×" for cell in row]):
            return "×"

    # 縦のチェック
    for col in range(3):
        if all([game_board[row][col] == "◯" for row in range(3)]):
            return "◯"
        elif all([game_board[row][col] == "×" for row in range(3)]):
            return "×"

    # 斜めのチェック
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        if game_board[0][0] == "◯":
            return "◯"
        elif game_board[0][0] == "×":
            return "×"
    elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
        if game_board[0][2] == "◯":
            return "◯"
        elif game_board[0][2] == "×":
            return "×"

    # 引き分けのチェック（すべてのセルが◯か×で埋まっている場合）
    if all(all(cell in ["◯", "×"] for cell in row) for row in game_board):
        return "引き分け"

    return None  # 勝者がいない場合は None を返す


def mark_button(event):
    button = event.widget
    button.config(text="◯", state=tk.DISABLED)
    # ボタンの座標を取得
    x, y = get_button_coordinates(button)
    # プレーヤーの手を盤面に反映
    game_board[x][y] = "◯"
    # 勝者のチェック
    winner = check_winner()
    if winner:
        messagebox.showinfo("勝者", f"{winner} の勝ち！")
        return
    # コンピュータの手を処理
    cpu_click()


def cpu_click():
    # 勝利できる手を探す
    for i in range(3):
        for j in range(3):
            if game_board[i][j] not in ["◯", "×"]:
                # その手を打った場合に勝てるかどうかをチェック
                game_board[i][j] = "×"
                if check_winner() == "×":
                    game_board[i][j] = "×"
                    buttons[i * 3 + j].config(text="×", state=tk.DISABLED)
                    messagebox.showinfo("勝者", "× の勝ち！")
                    return
                else:
                    game_board[i][j] = i * 3 + j + 1

    # 相手が勝利できる手を防ぐ
    for i in range(3):
        for j in range(3):
            if game_board[i][j] not in ["◯", "×"]:
                # 相手がその手を打った場合に勝てるかどうかをチェック
                game_board[i][j] = "◯"
                if check_winner() == "◯":
                    game_board[i][j] = "×"
                    buttons[i * 3 + j].config(text="×", state=tk.DISABLED)
                    return
                else:
                    game_board[i][j] = i * 3 + j + 1

    # ランダムに空のセルを選ぶ
    empty_cells = [
        (i, j) for i in range(3) for j in range(3) if game_board[i][j] not in ["◯", "×"]
    ]
    if empty_cells:
        x, y = random.choice(empty_cells)
        game_board[x][y] = "×"
        buttons[x * 3 + y].config(text="×", state=tk.DISABLED)

    # 勝者のチェック
    winner = check_winner()
    if winner:
        messagebox.showinfo("勝者", f"{winner} の勝ち！")


def get_button_coordinates(button):
    # ボタンの位置を取得する関数
    index = buttons.index(button)
    x = index // 3
    y = index % 3
    return x, y


def reset_game():
    global game_board
    # ゲームの盤面を初期化
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        for j in range(3):
            buttons[i * 3 + j].config(text=initial_board[i][j], state=tk.NORMAL)
    # メッセージボックスを閉じる
    messagebox.showinfo("リセット", "ゲームをリセットしました。")


label1 = tk.Label(window, text="あなたは◯です", bg=bg_color, fg=fg_color)
label1.place(x=690, y=40)

buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text=initial_board[i][j])
        button.place(x=630 + j * 80, y=100 + i * 50)
        button.bind("<Button-1>", mark_button)
        buttons.append(button)

# リセットボタンの作成と配置
reset_button = tk.Button(window, text="リセット", command=reset_game)
reset_button.place(x=150, y=270)

window.mainloop()
