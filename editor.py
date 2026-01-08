from prompt_toolkit import PromptSession
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
import os
from prompt_toolkit.shortcuts import choice
import utils

my_style = Style.from_dict(
    {
        'mg': '#00DB00',
        'mp': '#FF1493',
        'mb': '#1E90FF',
        'mo': '#FF8C00',
    }
)

kb = KeyBindings()
@kb.add('c-d')
def _(event):
    event.current_buffer.validate_and_handle()


def create_session(headtext, toolbar_content):
    session = PromptSession(
        message=HTML(f"<b><style color='#00DB00'>{headtext}</style></b>"),
        multiline=True,
        key_bindings=kb,
        wrap_lines=True,
        bottom_toolbar=HTML(f"{toolbar_content}"),
        cursor=CursorShape.BLINKING_BLOCK
    )
    return session


def print_text(head, text, color='mp'):
    print_formatted_text(HTML(f"<b><{color}>{head}</{color}></b>{text}"), style=my_style)

def print_error(text):
    print_formatted_text(HTML(f"<mo>{text}</mo>"), style=my_style)

def select_model(options):
    print()
    utils.draw_line(color='#00DB00')
    res = choice(message=HTML("<b><style color='#00DB00'>Select a model</style></b>"), 
                                options=options,
                                default="salad")
    utils.draw_line(color='#00DB00')
    print()
    return res

def ask_delet():
    print()
    utils.draw_line(color='#F54927')
    res = choice(message=HTML("<b><style color='#F54927'>Delet all histories?</style></b>"),
                 options=[(True, 'Yes'), (False, 'No')], 
                 default="salad")
    utils.draw_line(color='#F54927')
    print()
    return res


