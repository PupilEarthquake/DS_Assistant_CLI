from prompt_toolkit import PromptSession
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.styles import Style
import os

my_style = Style.from_dict(
    {
        'mg': '#00DB00',
        'mp': '#FF1493',
        'mb': '#1E90FF'
    }
)

kb = KeyBindings()
@kb.add('c-d')
def _(event):
    event.current_buffer.validate_and_handle()


def create_session(message, toolbar_content):
    session = PromptSession(
        message=HTML(f"<b><style color='#00DB00'>{message}</style></b>"),
        multiline=True,
        key_bindings=kb,
        wrap_lines=True,
        bottom_toolbar=HTML(f"{toolbar_content}"),
        cursor=CursorShape.BLINKING_BLOCK
    )
    return session


def print_text(sender, text):
    print_formatted_text(HTML(f"<b><mp>{sender} > </mp></b>{text}"), style=my_style)


def draw_line():
    columns = os.get_terminal_size().columns
    line = ''
    while len(line) < columns:
        line += '-'
    print(line[:columns])

