import os
import msvcrt
import typer
import sys
from typing import List, Callable, Dict, Any, Optional

class MenuSystem:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_menu(options: List[str], selected: int, title: str):
        MenuSystem.clear_screen()
        
        styled_title = typer.style(f"{title}", fg=typer.colors.CYAN, bold=True)
        typer.echo(styled_title)
        
        separator = typer.style("─" * len(title), fg=typer.colors.CYAN)
        typer.echo(f"{separator}\n")

        for idx, option in enumerate(options):
            if idx == selected:
                typer.echo(typer.style(f"> {option}", fg = typer.colors.MAGENTA, bold=True))
            else:
                typer.echo(typer.style(f"  {option}", fg=typer.colors.WHITE))

    @staticmethod
    def get_key():
        try:
            key = msvcrt.getch()
            return msvcrt.getch() if key == b'\xe0' else key
        except KeyboardInterrupt:
            sys.exit(0)

    @classmethod
    def menu_selection(cls, options: List[str], title: str):
        selected = 0
        while True:
            cls.print_menu(options, selected, title)
            key = cls.get_key()
            if key == b'H':  # Flèche haut
                selected = (selected - 1) % len(options)
            elif key == b'P':  # Flèche bas
                selected = (selected + 1) % len(options)
            elif key == b'\r':  # Touche Entrée
                return selected

def create_menu(options: List[str], actions: List[Callable], title: str = "Menu Principal", is_main_menu: bool = True):
    if len(options) != len(actions):
        raise ValueError("Le nombre d'options doit correspondre au nombre d'actions.")
    
    if is_main_menu:
        options.append("Quitter")
        actions.append(lambda: sys.exit(0))
    else:
        options.append("Retour au menu précédent")
        actions.append(lambda: None)
        options.append("Quitter")
        actions.append(lambda: sys.exit(0))
    
    while True:
        choice = MenuSystem.menu_selection(options, title)
        if choice == len(options) - 1:  # Dernière option (Quitter)
            actions[choice]()  # Exécute sys.exit(0)
        elif not is_main_menu and choice == len(options) - 2:  # Avant-dernière option (Retour au menu précédent)
            return
        else:
            typer.clear()
            action = actions[choice]
            if callable(action):
                result = action()
                if isinstance(result, bool) and result:  # Si l'action renvoie True, on quitte le programme
                    sys.exit(0)
            elif isinstance(action, dict):  # Sous-menu
                create_menu(action['options'], action['actions'], action['title'], is_main_menu=False)
            else:
                typer.echo("\nAction non valide.")
            if not isinstance(action, dict):  # Ne pas afficher ce message pour les sous-menus
                typer.echo("\nAppuyez sur une touche pour revenir au menu...")
                msvcrt.getch()


def main_menu(options: List[str], actions: List[Callable], title: str = "Menu Principal"):
    create_menu(options, actions, title, is_main_menu=True)





def create_submenu(options: List[str], actions: List[Callable], title: str = "Sous-menu"):
    return {'options': options, 'actions': actions, 'title': title}

def execute_menu_item(menu_structure: Dict[str, Any], item_path: str):
    parts = item_path.split('.')
    current_menu = menu_structure
    
    for part in parts:
        idx = int(part) - 1
        if idx < 0 or idx >= len(current_menu['options']):
            typer.echo(f"Invalid menu path: {item_path}")
            return
        if isinstance(current_menu['actions'][idx], dict):
            current_menu = current_menu['actions'][idx]
            if part == parts[-1]:  # If this is the last part and it's a submenu
                typer.echo(f"Vous tentez d'executer le sous menu : {current_menu['title']} n° {part}") 
                for i, option in enumerate(current_menu['options'], 1):
                    typer.echo(f"utilisez {part}.{i} pour le sous menu {option}")
        else:
            action = current_menu['actions'][idx]
            if callable(action):
                action()
            else:
                typer.echo("Invalid action")
            return

def run_menu(menu_structure: Dict[str, Any], item_path: Optional[str] = None):
    if item_path:
        execute_menu_item(menu_structure, item_path)
    else:
        main_menu(menu_structure['options'], menu_structure['actions'], menu_structure.get('title', 'Menu Principal'))

def create_menu_structure(options: List[str], actions: List[Callable], title: str = "Menu Principal") -> Dict[str, Any]:
    return {
        'options': options,
        'actions': actions,
        'title': title
    }
