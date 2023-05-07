# Password Generator

A Python library for generating secure passwords.

## Installation

You can install the package using `pip`:

```sh
pip install password-generator-lib
```

## Usage - CLI

To generate a password using the command-line interface, you can use the following command:

```sh
python password_generator.py <length> [-l] [-u] [-n] [-s] [-f] [-r] [-q <quantity>] [--no-sequential-characters]
```

The available options are:

- `<length>`: the length of the password (required)
- `-l`, `--lowercase`: include lowercase letters
- `-u`, `--uppercase`: include uppercase letters
- `-n`, `--numbers`: include numbers
- `-s`, `--symbols`: include special symbols
- `-f`, `--no-first-number-or-symbol`: the password cannot begin with a number or symbol
- `-r`, `--no-repeated-characters`: the password cannot contain the same character more than once
- `-q <quantity>`, `--quantity <quantity>`: the number of passwords to generate (default: 1)
- `--no-sequential-characters`: the password cannot contain sequential characters

Example usage:

```sh
python password_generator.py 10 -l -u -n -s -f -r --no-sequential-characters
```

## Usage - Importing the Class

You can also import the `PasswordGenerator` class from the `password_generator` module and use it in your Python code:

```python
from password_generator import PasswordGenerator

generator = PasswordGenerator(
    length=10,
    include_lowercase=True,
    include_uppercase=True,
    include_numbers=True,
    include_special_symbols=True,
    dont_begin_with_number_or_symbol=True,
    no_repeated_characters=True,
    no_sequential_characters=True,
    quantity=1
)

passwords = generator.generate()

print(passwords)
```

## Author

This project was created by Mahammad Salimov. You can contact me at salimovm.7@gmail.com.