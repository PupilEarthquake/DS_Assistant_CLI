from datetime import datetime
import os
import json
from prompt_toolkit import print_formatted_text, HTML


def get_date_now():
    date = datetime.now().strftime('%Y%m%d')
    return date


def get_chat_file_paths(date, chatname):
    base_path = os.path.dirname(os.path.realpath(__file__))
    save_dir = f'{base_path}/messages/{date}'
    if os.path.exists(save_dir):
        pass
    else:
        os.mkdir(save_dir)
    json_save_path = f'{save_dir}/{date}-{chatname}.json'
    md_save_path = f'{save_dir}/{date}-{chatname}.md'

    return json_save_path, md_save_path



def load_chat_json(json_save_path):
    if os.path.exists(json_save_path):
        with open(json_save_path, mode='r', encoding='utf-8') as f:
            messages = json.load(f)
    else:
        messages = []
    return messages



def save_chat_json(path, data):
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


def save_chat_md(path, data):
    with open(path, 'w') as md_file:
        for i in range(len(data)):
            role_i = data[i]['role']
            content_i = data[i]['content']
            md_file.write(f'__{role_i}:__\n {content_i} \n\n')



def list_chats():
    base_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = f'{base_path}/messages'
    dates = os.listdir(dir_path)
    for n, date in enumerate(dates):
        print_formatted_text(HTML(f"<b><style color='#00DB00'>{date}</style></b>"))
        files = os.listdir(f'{dir_path}/{date}')
        for fname in files:
            print(f'    -{fname}')
        if n == 5:
            break
