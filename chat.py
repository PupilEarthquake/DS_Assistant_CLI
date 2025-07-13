import tools
import editor
import asyncio
import sys
from prompt_toolkit import print_formatted_text, HTML


async def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(f'\r{cursor}')
            sys.stdout.flush()
            await asyncio.sleep(0.5)


async def get_response(messages: list, client):
    response = await client.chat.completions.create(
                    model='deepseek-reasoner',
                    messages=messages,
                    stream=False,
                    temperature=1.0
                    )

    response_message = response.choices[0].message.content
    return response_message


# async def fake_get_response(messages: list, client):
#     response = await asyncio.sleep(2)
#     return 'fake response'


async def one_round(messages, client):
    spin_task = asyncio.create_task(spinning_cursor())
    res_task = asyncio.create_task(get_response(messages, client))
    response = await res_task
    spin_task.cancel()
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    return response


def create_chat(client, date, chatname):
    json_path, md_path = tools.get_chat_file_paths(date, chatname)
    messages = tools.load_chat_json(json_path)

    session = editor.create_session('usr > ', f'{date}  {chatname}')


    while True:

        try:
            sent_message = session.prompt()
            messages.append({'role': 'user', 'content': sent_message})
            editor.draw_line()
            try:
                # respons = get_response(messages, client)
                response = asyncio.run(one_round(messages, client))
                editor.print_text('ds', response)
                messages.append({'role': 'assistant', 'content': response})
                editor.draw_line()
            except:
                print('error')
        except KeyboardInterrupt:
            break

        except EOFError:
            break

        tools.save_chat_json(json_path, messages)
        tools.save_chat_md(md_path, messages)
