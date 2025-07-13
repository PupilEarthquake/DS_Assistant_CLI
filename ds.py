#!/path/to/your/python

import argparse
from openai import AsyncOpenAI
import httpx
import tools
import chat


client = AsyncOpenAI(
    api_key="xxx", 
    base_url="https://api.deepseek.com",
    http_client=httpx.AsyncClient(proxy='xxx')
    )

def main():
    parser = argparse.ArgumentParser(
        prog='ds',
        description='Terminal Chat'
    )

    subparsers = parser.add_subparsers(
        dest='cmd'
    )



    parser_ls = subparsers.add_parser(
        'ls',
        help='List the historical chat records.'
    )



    parser_new = subparsers.add_parser(
        'new',
        help='Create new chat.'
    )
    parser_new.add_argument(
        '-n', '--name',
        help='Chat title'
    )



    parser_load = subparsers.add_parser(
        'load',
        help='Load chat.'
    )
    parser_load.add_argument(
        '-d', '--date',
        help='File date'
    )
    parser_load.add_argument(
        '-n', '--name',
        help='File name'
    )


    args = parser.parse_args()

    if args.cmd == 'new':
        chatname = args.name
        chatdate = tools.get_date_now()
        chat.create_chat(client, chatdate, chatname)

    elif args.cmd == 'load':
        chatdate = args.date
        chatname = args.name
        chat.create_chat(client, chatdate, chatname)

    elif args.cmd == 'ls':
        tools.list_chats()




if __name__ == '__main__':
    main()

