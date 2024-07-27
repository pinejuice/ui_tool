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
    def main(self):
        root = Tk()

        #------ Windowの設定 -------#
        root.title(APP_NAME) #画面タイトル変更
        root.geometry("640x360")    #初期画面サイズ(widthxheight)
        # root.maxsize(1024, 576) #最大画面サイズ(width, height)
        root.minsize(640, 360)  #最小画面サイズ(width, height)

        root.mainloop()


if __name__ == '__main__':
    tkinter_obj = TkinterOBJ()
    tkinter_obj.main()
