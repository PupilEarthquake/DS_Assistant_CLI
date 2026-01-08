#!/path/to/your/python

import argparse
from prompt_toolkit import prompt
import editor
import utils
import chat




parser = argparse.ArgumentParser(prog="DS Assistant Cli")
parser.add_argument("--version", "-v", action="version", version="DS Assistant Cli 2.0")
subparsers = parser.add_subparsers(dest="cmd")


parser_ls = subparsers.add_parser("ls", help="list all histories")
parser_ls.add_argument("--delet", "-d", help="delet all chat histories", action="store_true")


parser_c = subparsers.add_parser("chat", help="start a normal chat")
parser_c.add_argument("--think", "-t", help="show thinking chain (available in think-mode)", action="store_true")


parser_ec = subparsers.add_parser("ec", help="translate en to cn")
parser_ec.add_argument("--syns", "-ss", help="show the syntatic structure", action="store_true")
parser_ec.add_argument("--acbk", "-ab", help="specify the academic backgroud", metavar="_")
parser_ec.add_argument("--think", "-t", help="show thinking chain (available in think-mode)", action="store_true")


parser_ce = subparsers.add_parser("ce", help="translate cn to en")
parser_ce.add_argument("--mult", "-mt", help="provide multiple translations", action="store_true")
parser_ce.add_argument("--acbk", "-ab", help="specify the academic backgroud", metavar="_")
parser_ce.add_argument("--think", "-t", help="show thinking chain (available in think-mode)", action="store_true")

parser_syc = subparsers.add_parser("syc", help="syntax check (en)")
parser_syc.add_argument("--think", "-t", help="show thinking chain (available in think-mode)", action="store_true")


parser_dc = subparsers.add_parser("dict", help="an ai dictionary")
parser_dc.add_argument("--detail", "-d", help="show details", action="store_true")



args = parser.parse_args()



model_options = [("deepseek-chat", "Fast model"), ("deepseek-reasoner", "Reasoning model")]
text_head_ls = {"ec": "你是一个翻译器, 将下面内容翻译成中文",
             "ce": "你是一个翻译器, 将下面内容翻译成英文",
             "syc": "检查该句子的语法和用词是否正确",
             "dict": "翻译下方单词或短语"}
text_head_options_ls = {"ec-ss": "要求给出句子的结构", 
                     "ec-ab": "要求在此学科的背景下进行翻译",
                     "ce-mt": "要求尽可能给出多种翻译",
                     "ce-ab": "要求在此学科的背景下进行翻译",
                     "dict-d": "并给出详细信息"}
toolbar_help = ["<b>[Ctrl]+[D]</b> Send", "<b>[Ctrl]+[C]</b> Exit"]



if args.cmd == "ls":
    utils.ls_chats()

    if args.delet == True:
        res = editor.ask_delet()
        if res:
            utils.del_chats()



elif args.cmd == "chat":
    model = editor.select_model(model_options)
    text_head = ""
    sys_announce = "You are a helpful assistant"
    show_thinking_com = args.think
    toolbar_info = ["<b>Func</b> Chat"]

    if model == model_options[0][0]:
        toolbar_info.append("<b>Mod</b> Fast")
    elif model == model_options[1][0]:
        toolbar_info.append("<b>Mod</b> Think")

    filename = f"{utils.time_now()}_{str.upper(args.cmd)}"
    toolbar_additional_content = utils.make_table([toolbar_info, toolbar_help])
    

    # 创建聊天
    chat.create_chat(filename, sys_announce, text_head, show_thinking_com, model, toolbar_additional_content=toolbar_additional_content)



elif args.cmd == "ec":
    model = editor.select_model(model_options)
    text_head = text_head_ls["ec"]
    sys_announce = "You are a helpful assistant"
    show_thinking_com = args.think
    toolbar_info = ["<b>Func</b> EN2CN"]

    if model == model_options[0][0]:
        toolbar_info.append("<b>Mod</b> Fast")
    elif model == model_options[1][0]:
        toolbar_info.append("<b>Mod</b> Think")
    if args.syns:
        text_head = text_head + f", {text_head_options_ls["ec-ss"]}"
        toolbar_info.append("<b>SynS</b> On")
    else:
        toolbar_info.append("<b>SynS</b> Off")
    if args.acbk:
        text_head = text_head + f", {text_head_options_ls["ec-ab"]}: {args.acbk}"
        toolbar_info.append(f"<b>Bkg</b> {str.capitalize(args.acbk)}")
    else:
        pass


    filename = f"{utils.time_now()}_{str.upper(args.cmd)}"
    toolbar_additional_content = utils.make_table([toolbar_info, toolbar_help])
    

    # 创建聊天
    chat.create_chat(filename, sys_announce, text_head, show_thinking_com, model, toolbar_additional_content=toolbar_additional_content)
    
    

elif args.cmd == "ce":

    model = editor.select_model(model_options)
    text_head = text_head_ls["ce"]
    sys_announce = "You are a helpful assistant"
    show_thinking_com = args.think
    toolbar_info = ["<b>Func</b> CN2EN"]

    if model == model_options[0][0]:
        toolbar_info.append("<b>Mod</b> Fast")
    elif model == model_options[1][0]:
        toolbar_info.append("<b>Mod</b> Think")
    if args.mult:
        text_head = text_head + f", {text_head_options_ls["ce-mt"]}"
        toolbar_info.append("<b>MRes</b> On")
    else:
        toolbar_info.append("<b>MRes</b> Off")
    if args.acbk:
        text_head = text_head + f", {text_head_options_ls["ce-ab"]}: {args.acbk}"
        toolbar_info.append(f"<b>Bkg</b> {str.capitalize(args.acbk)}")
    else:
        pass


    filename = f"{utils.time_now()}_{str.upper(args.cmd)}"
    toolbar_additional_content = utils.make_table([toolbar_info, toolbar_help])
    

    # 创建聊天
    chat.create_chat(filename, sys_announce, text_head, show_thinking_com, model, toolbar_additional_content=toolbar_additional_content)
    


elif args.cmd == "syc":
    model = editor.select_model(model_options)
    text_head = text_head_ls["syc"]
    sys_announce = "You are a helpful assistant"
    show_thinking_com = args.think
    toolbar_info = ["<b>Func</b> SynChk"]

    if model == model_options[0][0]:
        toolbar_info.append("<b>Mod</b> Fast")
    elif model == model_options[1][0]:
        toolbar_info.append("<b>Mod</b> Think")
    
    filename = f"{utils.time_now()}_{str.upper(args.cmd)}"
    toolbar_additional_content = utils.make_table([toolbar_info, toolbar_help])
    

    # 创建聊天
    chat.create_chat(filename, sys_announce, text_head, show_thinking_com, model, toolbar_additional_content=toolbar_additional_content)


elif args.cmd == "dict":
    model = model_options[0][0]
    text_head = text_head_ls["dict"]
    sys_announce = "你是一个英汉词典"
    show_thinking_com = False
    toolbar_info = ["<b>Func</b> Dict(CN-EN)"]
    
    if args.detail:
        text_head = text_head + f", {text_head_options_ls["dict-d"]}"
        toolbar_info.append("<b>Dtl</b> On")
    else:
        toolbar_info.append("<b>Dtl</b> Off")

    filename = f"{utils.time_now()}_{str.upper(args.cmd)}"
    toolbar_additional_content = utils.make_table([toolbar_info, toolbar_help])
    

    # 创建聊天
    chat.create_chat(filename, sys_announce, text_head, show_thinking_com, model, toolbar_additional_content=toolbar_additional_content)
