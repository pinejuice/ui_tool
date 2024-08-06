# 標準モジュール
import sys
import configparser
from tkinter import *
from tkinter import ttk
from tkinter import font

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
        self.root.geometry("1280x720")
        # 最小画面サイズ(width, height)
        self.root.minsize(1280, 720)
        # # 画面最大化
        # self.root.state("zoomed")

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
        frame = Frame(self.root, background="#E8FFE6")
        frame.pack(expand=True, fill=BOTH)

        # ヘッダーの設定
        self.header_frame1 = ttk.Frame(frame)
        self.header_frame1.pack(fill='x', padx=[10, 10], pady=[10, 0])
        self.header_frame2 = ttk.Frame(frame)
        self.header_frame2.pack(fill='x', padx=[10, 10], pady=[5, 5])

        # メインフレームの設定
        self.main_frame = ttk.Frame(frame)
        self.main_frame.pack(fill=BOTH, padx=[10, 10], pady=[0, 10])

    def setup_header(self):
        # ヘッダー1のWidgets
        # フォントの設定
        font_bold = font.Font(size=10, weight='bold')
        # 「PJ名」ラベル
        pj_name_label_head = ttk.Label(
            self.header_frame1, 
            text=f'プロジェクト名', 
            background='#0000aa', 
            foreground='#ffffff', 
            padding=(5, 10), 
            relief='solid', 
            font=font_bold
        )
        pj_name_label_head.pack(side='left')
        pj_name_label_body = ttk.Label(
            self.header_frame1, 
            text=f'{self.project_info["name"]}', 
            width=25, 
            padding=(5, 10), 
            relief='solid', 
            font=font_bold
        )
        pj_name_label_body.pack(side='left', after=pj_name_label_head, padx=[0, 10])
        # 「ファイル名」ラベル
        file_name_label_head = ttk.Label(
            self.header_frame1, 
            text=f'ファイル名', 
            background='#0000aa', 
            foreground='#ffffff', 
            padding=(5, 10), 
            relief='solid', 
            font=font_bold
        )
        file_name_label_head.pack(side='left')
        file_name_label_body = ttk.Label(
            self.header_frame1, 
            text=f'{self.project_info["last_file"]}', 
            width=40, 
            padding=(5, 10), 
            relief='solid', 
            font=font_bold
        )
        file_name_label_body.pack(side='left', after=file_name_label_head, padx=[0, 10])

        # 「PJを選択」ボタン
        select_pj_btn = ttk.Button(self.header_frame1, text='PJを選択')
        select_pj_btn.pack(side='right')
        # 「ファイルを選択」ボタン
        select_file_btn = ttk.Button(self.header_frame1, text='ファイルを選択')
        select_file_btn.pack(side='right')
        # 「新規作成」ボタン
        new_file_btn = ttk.Button(
            self.header_frame1, 
            text='新規作成', 
            state=font_bold, 
            padding=[5, 10, 5, 10]
        )
        new_file_btn.pack(side='right')
        
        # ヘッダー2のWidgets
        # 実行ボタン
        run_btn = ttk.Button(
            self.header_frame2, 
            text='実行', 
            padding=[5, 5, 5, 5]
        )
        run_btn.pack(side='right', padx=[10, 0])
        # ブラウザのドライバーの選択
        browser_select = ttk.Combobox(
            self.header_frame2, 
            values=BROWSER_LIST,
            width=20
        )
        browser_select.pack(side='right')

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
