import os
from tkinter import filedialog


def select_pj(pj_info):
    folder_path = filedialog.askdirectory()
    pj_info['path'] = folder_path
    pj_info['name'] = os.path.basename(folder_path)

