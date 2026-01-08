import asyncio
import sys
from openai import AsyncOpenAI
import httpx
import utils
import editor





async def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(f'\r{cursor} ')
            sys.stdout.flush()
            await asyncio.sleep(0.5)


async def get_response(client, msg_list: list, model: str, tempreture: float, stream: bool):

    spin_task = asyncio.create_task(spinning_cursor())
    ai_task = client.chat.completions.create(
                    model=model,
                    messages=msg_list,
                    stream=stream,
                    temperature=tempreture
                    )

    response = await ai_task
    spin_task.cancel()
    sys.stdout.write('\r' + ' ' * 50 + '\r') # 清除该行
    response_message = response.choices[0].message.content

    if model == 'deepseek-reasoner':
        response_reasoning_msg = response.choices[0].message.reasoning_content
    else:
        response_reasoning_msg = None

    return response_reasoning_msg, response_message





def create_chat(filename: str, sys_announce, mode_text_head, show_thinking_com, model: str, toolbar_additional_content: str):
    config = utils.loadconf()
    apikey = config['network']['apikey']
    proxy_url = config['network']['proxy']
    tempreture = config.getfloat('model', 'tempreture')
    stream = config.getboolean('model', 'stream')
    show_thinking_conf = config.getboolean('output', 'thinking')


    if proxy_url in ['None', 'False']:
        client = AsyncOpenAI(
        api_key=apikey, 
        base_url="https://api.deepseek.com"
        )
    else:
        client = AsyncOpenAI(
        api_key=apikey, 
        base_url="https://api.deepseek.com",
        http_client=httpx.AsyncClient(proxy=proxy_url)
        )


    js_path, md_path = utils.create_save_path(filename)

    session = editor.create_session(headtext="usr > ", toolbar_content=f"{toolbar_additional_content}")

    msg_list_inner, msg_list_export = [], []

    while True:
        try:
            sent_msg = session.prompt()
            msg_list_inner.append({"role": "system", "content": sys_announce})
            msg_list_inner.append({"role": "user", "content": f"{mode_text_head}:\n{sent_msg}"})
            msg_list_export.append({"role": "user", "content": f"{mode_text_head}:\n\n{sent_msg}"})
            utils.draw_line()

            try:
                response_think, response_answ = asyncio.run(get_response(client, msg_list_inner, model, tempreture, stream))
                if response_think:
                    if show_thinking_conf or show_thinking_com:
                        editor.print_text('ds (thinking) > ', response_think, color='mb')
                        utils.draw_line()
        
                editor.print_text('ds (answer) > ', response_answ)
                utils.draw_line()

                msg_list_inner.append({"role": "assistant", "content": response_answ})
                msg_list_export.append({"role": "assistant", "content": response_answ})

                utils.save_chat_json(js_path, msg_list_inner)
                utils.save_chat_md(md_path, msg_list_export)

                # print(msg_list_inner)

            except Exception as e:
                del msg_list_inner[-1]
                editor.print_error(e)
                utils.draw_line()

        except KeyboardInterrupt:
            break

        except EOFError:
            break


  
