from datetime import datetime
import os
import json
import configparser
from prompt_toolkit import print_formatted_text, HTML
import shutil


def time_now():
    date = datetime.now().strftime('%Y%m%d%H%M')
    return date

     


def create_save_path(filename):
    base_path = os.path.dirname(os.path.realpath(__file__))
    base_path = base_path + '/chathist'
    if os.path.exists(base_path):
        pass
    else:
        os.mkdir(base_path)
    save_dir_js = f"{base_path}/js"
    save_dir_md = f"{base_path}/md"
    if os.path.exists(save_dir_js):
        pass
    else:
        os.mkdir(save_dir_js)
    if os.path.exists(save_dir_md):
        pass
    else:
        os.mkdir(save_dir_md)
    json_save_path = f'{save_dir_js}/{filename}.json'
    md_save_path = f'{save_dir_md}/{filename}.md'

    return json_save_path, md_save_path


def draw_line(color='#FFFFFF'):
    columns = os.get_terminal_size().columns
    line = ''
    while len(line) < columns:
        line += '-'
    # print(line[:columns])
    print_formatted_text(HTML(f"<b><style color='{color}'>{line[:columns]}</style></b>"))


def make_table(table_matrix):
    num_row = len(table_matrix)
    num_col = max([len(item) for item in table_matrix])

    cell_len_ls = []
    for row in table_matrix:
        for item in row:
            cell_len_ls.append(len(item))

    cell_len = max(cell_len_ls)

    out = ''
    for i in range(num_row):
        for j in range(num_col):
            # print(i, j)
            try:
                content = table_matrix[i][j] + ' '*(cell_len - len(table_matrix[i][j]) + 4)
            except:
                content = ' '*(cell_len + 4)
            
            if j == num_col - 1:
                if i < num_row - 1:
                    out = out + content + '\n'
                else:
                    out = out + content
            else:
                out = out + content
    
    return out



def save_chat_json(path, data):
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


def save_chat_md(path, data):
    with open(path, 'w') as md_file:
        for i in range(len(data)):
            role_i = data[i]['role']
            content_i = data[i]['content']
            if role_i in ['user', 'assistant']:
                md_file.write(f'__{role_i}:__\n {content_i} \n\n')


# json_save_path, md_save_path = create_save_path('test')

def loadconf():
    base_path = os.path.dirname(os.path.realpath(__file__))
    conf_path = base_path + '/user.conf'
    config = configparser.ConfigParser()
    config.read(conf_path)

    return config




def ls_chats():
    base_path = os.path.dirname(os.path.realpath(__file__))
    base_path = base_path + '/chathist'
    try:
        file_ls = os.listdir(base_path+'/js')
        print_formatted_text(HTML(f"<b><style color='#00DB00'>{base_path}</style></b>"))
        num_files = len(file_ls)
        for n in range(num_files):
            file_name = file_ls[n]
            file_name = file_name.split('.')[0]
            if n == num_files - 1:
                print(f'    └─{file_name}')
            else:
                print(f'    ├─{file_name}')
    except:
        print('No historical chats')



def del_chats():
    base_path = os.path.dirname(os.path.realpath(__file__))
    base_path = base_path + '/chathist'
    # os.rmdir(base_path)
    if os.path.exists(base_path) and os.path.isdir(base_path):
        shutil.rmtree(base_path)
        print('Done!\n')
    else:
        print('No such file or directory')