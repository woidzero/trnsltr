from misc.util import get_list

def _help() -> None:
    return print(
        """
    usage: <abc> [TEXT]
    
    @help - show this message
    @list - view all alphabets
    @exit - exit program
    """
    )

def _list() -> None:
    abc_list = get_list()
    msg = ""
    
    for abc in abc_list:
        msg += f"{abc} - {abc_list[abc]['description']}\n"

    print(msg)