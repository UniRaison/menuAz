```markdown
# MenuAz: A Flexible Menu System for Python CLI Applications

MenuAz is a powerful and flexible menu system for creating hierarchical command-line interfaces in Python.
It provides an easy-to-use framework for building interactive menus with submenus, actions, and navigation.

## Features

- Create multi-level menu structures
- Support for submenus
- Easy navigation with arrow keys
- Customizable menu titles and options
- Direct execution of menu items via command-line arguments

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/menuaz.git
   ```

2. Navigate to the project directory:
   ```
   cd menuaz
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the necessary functions from `menuAz_lib.py`:

   ```python
   from menuAz_lib import create_menu_structure, run_menu, create_submenu
   ```

2. Define your menu structure and actions:

   ```python
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

   menu_structure = create_menu_structure(
       ["Option 1", "Option 2", "Submenu"],
       [option1, option2, submenu()],
       "Main Menu"
   )
   ```

3. Run the menu:

   ```python
   run_menu(menu_structure)
   ```

## Documentation

### `create_menu_structure(options, actions, title, path='', is_submenu=False)`

Creates a menu structure with the given options, actions, and title.

- `options`: List of menu option labels
- `actions`: List of corresponding actions (functions or submenus)
- `title`: Menu title
- `path`: (Optional) Current menu path
- `is_submenu`: (Optional) Whether this is a submenu

### `run_menu(menu_structure, item_path=None)`

Runs the menu system with the given menu structure.

- `menu_structure`: The menu structure created by `create_menu_structure`
- `item_path`: (Optional) Direct path to execute a specific menu item

### `create_submenu(options, actions, title)`

Creates a submenu structure.

- `options`: List of submenu option labels
- `actions`: List of corresponding actions for the submenu
- `title`: Submenu title

## Sample

Here's a simple example of how to use MenuAz:

```python
from menuAz_lib import create_menu_structure, run_menu, create_submenu
import typer

def option1():
    typer.echo(typer.style("Executing option 1", fg=typer.colors.GREEN))

def option2():
    typer.echo(typer.style("Executing option 2", fg=typer.colors.BLUE))

def submenu():
    return create_submenu(
        ["Suboption 1", "Suboption 2"],
        [
            lambda: typer.echo(typer.style("Executing suboption 1", fg=typer.colors.YELLOW)),
            lambda: typer.echo(typer.style("Executing suboption 2", fg=typer.colors.MAGENTA))
        ],
        "Submenu"
    )

def main():
    menu_structure = create_menu_structure(
        ["Option 1", "Option 2", "Submenu"],
        [option1, option2, submenu()],
        "Main Menu"
    )
    run_menu(menu_structure)

if __name__ == "__main__":
    typer.run(main)
```

This example creates a simple menu with two options and a submenu, demonstrating the basic usage of MenuAz.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README provides a comprehensive overview of your MenuAz project, including installation instructions, usage examples, documentation for key functions, and a sample implementation. You can adjust the content as needed to better fit your project's specific details or requirements.

