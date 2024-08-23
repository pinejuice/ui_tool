# 標準モジュール
import sys
import configparser
from tkinter import *
from tkinter import ttk
from tkinter import font

sys.dont_write_bytecode = True

# 外部モジュール


# 自作モジュール
from tkinter_common import *


# システム設定
APP_NAME = 'BrowserPilot'
BROWSER_LIST = ['Chrome', 'Firefox']
CONFIG_FILE_PATH = 'current_pj.ini'

# メインフレームの表のヘッダーの情報
HEADER_LIST = [('No.', 10), ('コマンド', 30), ('パラメータ1', 30), ('パラメータ2', 30), ('備考', 50)]

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
        conf.read(CONFIG_FILE_PATH, encoding='utf-8')
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
        # フォントの設定
        Label_font_bold = font.Font(size=10, weight='bold')
        style = ttk.Style()
        style.configure('header.TButton', font=('', 10))

        # ヘッダー1のWidgets
        # 「PJ名」ラベル
        pj_name_label_head = ttk.Label(
            self.header_frame1, 
            text=f'プロジェクト名', 
            background='#0000aa', 
            foreground='#ffffff', 
            padding=(5, 10), 
            relief='solid', 
            font=Label_font_bold
        )
        pj_name_label_head.pack(side='left')
        self.pj_name_label_body = ttk.Label(
            self.header_frame1, 
            text=f'{self.project_info["name"]}', 
            width=25, 
            padding=(5, 10), 
            relief='solid', 
            font=Label_font_bold
        )
        self.pj_name_label_body.pack(side='left', after=pj_name_label_head, padx=[0, 10])

        # 「ファイル名」ラベル
        file_name_label_head = ttk.Label(
            self.header_frame1, 
            text=f'ファイル名', 
            background='#0000aa', 
            foreground='#ffffff', 
            padding=(5, 10), 
            relief='solid', 
            font=Label_font_bold
        )
        file_name_label_head.pack(side='left')
        self.file_name_label_body = ttk.Label(
            self.header_frame1, 
            text=f'{self.project_info["last_file"]}', 
            width=40, 
            padding=(5, 10), 
            relief='solid', 
            font=Label_font_bold
        )
        self.file_name_label_body.pack(side='left', after=file_name_label_head, padx=[0, 10])

        # 「PJを選択」ボタン
        select_pj_btn = ttk.Button(
            self.header_frame1, 
            text='PJを選択', 
            padding=[5, 10, 5, 10],
            style='header.TButton'
        )
        select_pj_btn.bind('<Button-1>', lambda x: select_pj(self.project_info))
        select_pj_btn.bind('<Button-1>', lambda x: self.update_header(), '+')
        select_pj_btn.pack(side='right', padx=[10, 0])
        # 「ファイルを選択」ボタン
        select_file_btn = ttk.Button(
            self.header_frame1, 
            text='ファイルを選択', 
            padding=[5, 10, 5, 10],
            style='header.TButton'
        )
        select_file_btn.bind('<Button-1>', lambda x: select_file(self.project_info))
        select_file_btn.bind('<Button-1>', lambda x: self.update_header(), '+')
        select_file_btn.pack(side='right', padx=[10, 0])
        # 「新規作成」ボタン
        new_file_btn = ttk.Button(
            self.header_frame1, 
            text='新規作成', 
            state=Label_font_bold, 
            padding=[5, 10, 5, 10],
            style='header.TButton'
        )
        new_file_btn.pack(side='right')
        
        # ヘッダー2のWidgets
        # 実行ボタン
        run_btn = ttk.Button(
            self.header_frame2, 
            text='実行', 
            padding=[5, 5, 5, 5],
            style='header.TButton'
        )
        run_btn.pack(side='right', padx=[10, 0])
        # ブラウザのドライバーの選択
        browser_select = ttk.Combobox(
            self.header_frame2, 
            values=BROWSER_LIST,
            width=25
        )
        browser_select.pack(side='right')

    def setup_main_frame(self):
        # メインフレームのWidgets
        self.row_num = 0
        # 表全体を管理する2次元配列
        self.table = []
        # 表のヘッダーを作成
        header_row = []
        for i in range(len(HEADER_LIST)):
            col = ttk.Label(self.main_frame, width=HEADER_LIST[i][1], text=HEADER_LIST[i][0])
            col.grid(row=self.row_num, column=i)
            header_row.append(col)
        self.table.append(header_row)
        # 表のボディを作成

    def insert_row(self, row_num, num=None, command='', param1=None, param2=None, memo=None):
        row = []
        for i in range(len(HEADER_LIST)):
            if i == 0:
                col = ttk.Label(self.main_frame, width=HEADER_LIST[i][1], text=self.row_num+1)
            else:
                col = ttk.Entry(self.main_frame, width=HEADER_LIST[i][1])
            col.grid(row=row_num, column=i)
            row.append(col)
        self.table.append(row)


    def update_config(self):
        conf = configparser.ConfigParser()
        conf['Default'] = {
            'PROJECT_PATH': self.project_info['path'],
            'PROJECT_NAME': self.project_info['name'],
            'LAST_FILE': self.project_info['last_file'],
            'LAST_BROWSER': self.project_info['browser'],
        }
        with open(CONFIG_FILE_PATH, 'w', encoding='utf-8') as f:
            conf.write(f)

    def update_header(self):
        self.pj_name_label_body['text'] = self.project_info['name']
        self.file_name_label_body['text'] = self.project_info['last_file']
        self.update_config()

    def main(self):
        self.create_frame()
        self.setup_header()
        self.setup_main_frame()
        # UIの起動
        self.root.mainloop()


if __name__ == '__main__':
    tkinter_obj = TkinterOBJ()
    tkinter_obj.main()
