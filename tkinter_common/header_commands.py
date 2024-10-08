import os
import json
from tkinter import filedialog


def select_pj(pj_info):
    initial_directory = os.path.join(os.getcwd(), 'projects')
    # フォルダ選択のダイアログを表示
    folder_path = filedialog.askdirectory(initialdir=initial_directory)

    pj_info['path'] = folder_path
    pj_info['name'] = os.path.basename(folder_path)

def select_file(pj_info):
    file_type = [('', 'json')]
    folder_path = pj_info['path']
    if folder_path == '':
        folder_path = os.path.join(os.getcwd(), 'projects')

    # ファイル選択のダイアログを表示
    file_path = filedialog.askopenfilename(filetypes=file_type, initialdir=folder_path)
    pj_info['path'] = os.path.dirname(os.path.dirname(file_path))
    pj_info['name'] = os.path.basename(os.path.dirname(file_path))
    pj_info['last_file'] = os.path.basename(file_path)

    json_file_path = os.path.join(pj_info['path'], 'source', pj_info['last_file'])
    print(json_file_path)
    load_json(json_file_path)

def load_json(target_json_file):
    with open(target_json_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
        command_list = d['commands']
