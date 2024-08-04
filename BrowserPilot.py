# 標準モジュール
import sys
import configparser
from tkinter import *
from tkinter import ttk

sys.dont_write_bytecode = True

# 外部モジュール


# 自作モジュール


# システム設定
APP_NAME = 'BrowserPilot'
BROWSER_LIST = ['Chrome', 'Firefox']


class TkinterOBJ():
    def __init__(self):
        self.load_current_project_info()

        self.root = Tk()
        # Windowの設定
        # 画面タイトル変更
        self.root.title(APP_NAME)
        # 初期画面サイズ(widthxheight)
        self.root.geometry("640x360")
        # 最小画面サイズ(width, height)
        self.root.minsize(640, 360)

    def load_current_project_info(self):
        conf = configparser.ConfigParser()
        conf.read('current_pj.ini', encoding='utf-8')
        # Defaultの読み込み
        self.project_info = {
            'path': conf.get('Default', 'PROJECT_PATH'),
            'name': conf.get('Default', 'PROJECT_NAME'),
            'last_file': conf.get('Default', 'LAST_FILE'),
            'browser': conf.get('Default', 'LAST_BROWSER'),
        }

    def create_frame(self):
        frame = Frame(self.root)
        frame.pack(expand=True, fill=BOTH)

        # ヘッダーの設定
        self.header_frame = ttk.Frame(frame)
        self.header_frame.pack(anchor=W)

        # メインフレームの設定
        self.main_frame = ttk.Frame(frame)
        self.main_frame.pack()

    def setup_header(self):
        # ヘッダーのWidgets
        # 「PJ名」フレーム
        pj_name_label = Label(self.header_frame, text=f'PJ名: {self.project_info["name"]}')
        pj_name_label.grid(row=0, column=0)
        pj_name_frame = ttk.Frame(self.header_frame)
        pj_name_frame.grid(row=0, column=1)
        # 「新規作成」ボタン
        new_file_btn = ttk.Button(self.header_frame, text='新規作成')
        new_file_btn.grid(row=0, column=2)
        # 「ファイルを選択」ボタン
        select_file_btn = ttk.Button(self.header_frame, text='ファイルを選択')
        select_file_btn.grid(row=0, column=3)
        # 「PJを選択」ボタン
        select_pj_btn = ttk.Button(self.header_frame, text='PJを選択')
        select_pj_btn.grid(row=0, column=4)
        # ブラウザのドライバーの選択
        browser_select = ttk.Combobox(
            self.header_frame, 
            values=BROWSER_LIST,
            width=20
        )
        browser_select.grid(row=1, column=0, columnspan=2)
        # 実行ボタン
        run_btn = ttk.Button(self.header_frame, text='実行', width=10)
        run_btn.grid(row=1, column=2)

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
