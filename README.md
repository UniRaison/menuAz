```markdown
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

This sample demonstrates how to create a simple menu with two options and a submenu using the MenuAz library.
```

This updated section now includes:
1. The correct GitHub repository URL for cloning.
2. All necessary imports based on the provided `menuAz_lib.py` file.
3. A complete example of how to use the MenuAz library to create and run a menu.

Thank you for bringing this to my attention. Providing accurate and complete information is crucial for users to effectively use your library.
