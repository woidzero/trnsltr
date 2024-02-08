from config import Config

from misc.commands import _help, _list
from misc.util import get_list, get_abc

from misc import __version__

def translator(text, abc) -> None:
    out = ""
    abc = get_abc(abc)
    
    for s in text:
        if s in abc:
            out += abc[s]
        else:
            out += s
            
    print(out+"\n")

def cli() -> None:
    print(f"trnsltr v{__version__}\n")
    print("view commands and help // @help\n")

    while True:
        prompt = input("-> ")
        if prompt.startswith("@"):
            execute_command(prompt)
        elif prompt.startswith(tuple([abc for abc in get_list()])):
            abc = prompt.split()[0]
            text = prompt.replace(abc, "").strip()
            translator(text, abc)
        else:
            translator(prompt, Config.DEFAULT_ABC)

def execute_command(prompt: str) -> None:
    match prompt: 
        case "@help":
            _help()
        case "@list":
            _list() 
        case "@exit":
            exit(0)
        case _:
            print(f"undefined command `{prompt}`")

if __name__ == "__main__":
    cli()
