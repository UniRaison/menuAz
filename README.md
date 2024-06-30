```markdown
# MenuAz: A Flexible Menu System for Python CLI Applications

MenuAz is a powerful and flexible menu system for creating
hierarchical command-line interfaces in Python.
It provides an easy-to-use framework for building
interactive menus with submenus, actions, and navigation
that can be also used in direct cmd line.

## Features

- Create multi-level menu structures
- Support for submenus
- Easy navigation with arrow keys
- Customizable menu titles and options
- Direct execution of menu items via command-line arguments

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/uniraison/menuaz.git
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

1. Import the necessary functions and modules:

   ```python
   from menuAz_lib import create_menu_structure, run_menu, create_submenu
   import typer
   from typing import Optional
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

   def main(item_path: Optional[str] = typer.Argument(None)):
       menu_structure = create_menu_structure(
           ["Option 1", "Option 2", "Submenu"],
           [option1, option2, submenu()],
           "Main Menu"
       )
       run_menu(menu_structure, item_path)

   if __name__ == "__main__":
       typer.run(main)
   ```

3. Run the script:

   ```
   python menutest.py
   ```

## Command-line Direct Execution

MenuAz supports direct execution of menu items via command-line arguments. This allows you to bypass the interactive menu and execute specific actions directly.

Example:

```
python menutest.py 1        # Executes Option 1
python menutest.py 3.1      # Executes Suboption 1 in the Submenu
```

The argument format is based on the menu structure:
- Use numbers to navigate through the menu levels
- Separate levels with a dot (.)

For example, `3.1` means:
1. Select the 3rd option in the main menu (Submenu)
2. Select the 1st option in the submenu

This feature is particularly useful for scripting or when you need to execute specific actions quickly without navigating through the menu.

## Sample Output

When run interactively, the menu will look like this:

```
Main Menu
─────────
> 1. Option 1
  2. Option 2
  3. Submenu +
```

You can navigate using arrow keys and press Enter to select an option.

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README.md file now includes:

1. A brief introduction to MenuAz
2. Installation instructions with the correct GitHub repository URL
3. Usage instructions with a complete example, including all necessary imports
4. An explanation of the command-line direct execution feature with examples
5. A sample output of what the menu looks like when run interactively
6. Documentation for key functions
7. Information about contributing and licensing

This should provide a comprehensive guide for users of your MenuAz library,
covering both interactive use and direct command-line execution.
