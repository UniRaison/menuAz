from menuAz_lib import create_menu_structure, run_menu, create_submenu
import typer
from typing import Optional

def option1():
    typer.echo(typer.style("Exécution de l'option 1", fg=typer.colors.MAGENTA))

def option2():
    typer.echo(typer.style("Exécution de l'option 2", fg=typer.colors.CYAN))

def sub_sub_menu1():
    return create_submenu(
        ["Sous-sous-option", "Sous-sous-option"],
        [
            lambda: typer.echo(typer.style("Exécution de la sous-sous-option 1", fg=typer.colors.YELLOW)),
            lambda: typer.echo(typer.style("Exécution de la sous-sous-option 2", fg=typer.colors.BLUE))
        ],
        "Sous-sous-menu"
    )

def sub_sub_menu2():
    return create_submenu(
        ["Sous-sous-option", "Sous-sous-option", "Sous-sous-sous-menu"],
        [
            lambda: typer.echo(typer.style("Exécution de la sous-sous-option 1", fg=typer.colors.GREEN)),
            lambda: typer.echo(typer.style("Exécution de la sous-sous-option 2", fg=typer.colors.RED)),
            sub_sub_sub_menu()
        ],
        "Sous-sous-menu"
    )

def sub_sub_sub_menu():
    return create_submenu(
        ["Sous-sous-sous-option", "Sous-sous-sous-option"],
        [
            lambda: typer.echo(typer.style("Exécution de la sous-sous-sous-option 1", fg=typer.colors.WHITE)),
            lambda: typer.echo(typer.style("Exécution de la sous-sous-sous-option 2", fg=typer.colors.MAGENTA))
        ],
        "Sous-sous-sous-menu"
    )

def submenu():
    return create_submenu(
        ["Sous-option", "Sous-option", "Sous-sous-menu", "Sous-sous-menu"],
        [
            lambda: typer.echo(typer.style("Exécution de la sous-option 1", fg=typer.colors.RED)),
            lambda: typer.echo(typer.style("Exécution de la sous-option 2", fg=typer.colors.GREEN)),
            sub_sub_menu1(),
            sub_sub_menu2()
        ],
        "Menu Secondaire"
    )

def main(item_path: Optional[str] = typer.Argument(None)):
    menu_structure = create_menu_structure(
        ["Option", "Option", "Sous-menu"],
        [option1, option2, submenu()],
        "Menu Principal"
    )
    run_menu(menu_structure, item_path)

if __name__ == "__main__":
    typer.run(main)
