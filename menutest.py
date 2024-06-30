from menuAz_lib import create_menu_structure, run_menu, create_submenu
import typer
from typing import Optional

def option1():
    print("Executing option 1")

def option2():
    print("Executing option 2")

def submenu():
    return create_submenu(
        ["Suboption 1", "Suboption 2"],
        [
            lambda: print("Executing suboption 1"),
            lambda: print("Executing suboption 2")
        ],
        "Submenu"
    )

def main(item_path: Optional[str] = typer.Argument(None)):
    menu_structure = create_menu_structure(
        ["Option 1", "Option 2", "Submenu"],
        [option1, option2, submenu()],
        "Main Menu"
    )
    run_menu(menu_structure, item_path)

if __name__ == "__main__":
    typer.run(main)
