# 標準モジュール
import sys
from tkinter import *
from tkinter import ttk

sys.dont_write_bytecode = True

# 外部モジュール


# 自作モジュール


# システム設定
APP_NAME = 'BrowserPilot'


class TkinterOBJ():
    def __init__(self):
        self.root = Tk()

        # Windowの設定
        # 画面タイトル変更
        self.root.title(APP_NAME)
        # 初期画面サイズ(widthxheight)
        self.root.geometry("640x360")
        # 最小画面サイズ(width, height)
        self.root.minsize(640, 360)

    def create_frame(self):
        frame = Frame(self.root)
        frame.pack(expand=True, fill=BOTH)
        # frame.columnconfigure(0, weight=1) # 0列目を横方向に引き伸ばす

        # ヘッダーの設定
        self.header_frame = ttk.Frame(frame)
        self.header_frame.pack(anchor=W)

        # メインフレームの設定
        self.main_frame = ttk.Frame(frame)
        self.main_frame.pack()

    def setup_header(self):
        # ヘッダーのWidgets
        file_btn = ttk.Button(self.header_frame, text='ファイル')
        file_btn.pack(side='left')
        setting_btn = ttk.Button(self.header_frame, text='設定')
        setting_btn.pack(side='left')

    def setup_main_frame(self):
        # メインフレームのWidgets
        label1 = Label(self.main_frame, text="aaaaaaaa")
        label1.pack()

    def main(self):
        self.create_frame()
        self.setup_header()
        self.setup_main_frame()
        # UIの起動
        self.root.mainloop()


if __name__ == '__main__':
    tkinter_obj = TkinterOBJ()
    tkinter_obj.main()
