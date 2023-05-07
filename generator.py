#!/usr/bin/env python3
"""
password_generator.py

A Python script for generating secure passwords.

Author: Mahammad Salimov
Contact: salimovm.7@gmail.com

Summary:
The PasswordGenerator class generates random passwords based on the arguments passed to it.

Installation:
This script requires Python 3.6 or later.

Usage:
To generate a password, run the script with the desired arguments. The following arguments are available:

    - length: The length of the password to generate.
    - -l or --lowercase: Include lowercase letters in the password.
    - -u or --uppercase: Include uppercase letters in the password.
    - -n or --numbers: Include numbers in the password.
    - -s or --symbols: Include special symbols in the password.
    - -f or --no-first-number-or-symbol: The password cannot begin with a number or symbol.
    - -r or --no-repeated-characters: The password cannot contain the same character more than once.
    - -q or --quantity: The number of passwords to generate.
    - --no-sequential-characters: The password cannot contain sequential characters.

Example usage:

    python password_generator.py 12 -luns -q 10
    => ['C2d}Oa5&^9R8', 'L3x#Kg7@%1D0', 'U7h$Nf5#^1Y9', 'B8r#Jn5*!2Z0', 'Q2z@Tc4!%6X9', 'V4u!Pd8^#3I6', 'M6w#Tg4^%7Z1', 'A4e#Lg6^%2N1', 'F5y!Ea9@%2K1', 'D7r%Nk6#^1W5']

"""
import argparse
import secrets
import string
import sys


class PasswordGenerator:
    def __init__(
        self,
        length=6,
        include_lowercase=True,
        include_uppercase=True,
        include_numbers=True,
        include_special_symbols=True,
        dont_begin_with_number_or_symbol=False,
        no_repeated_characters=False,
        no_sequential_characters=False,
        quantity=1,
    ):
        self.length = length or 6
        self.include_lowercase = include_lowercase
        self.include_uppercase = include_uppercase
        self.include_numbers = include_numbers
        self.include_special_symbols = include_special_symbols
        self.dont_begin_with_number_or_symbol = dont_begin_with_number_or_symbol
        self.no_repeated_characters = no_repeated_characters
        self.no_sequential_characters = no_sequential_characters
        self.quantity = quantity

        self.alphabet = self.build_alphabet()
        self.passwords = []

    def build_alphabet(self):
        alphabet = ""

        if self.include_lowercase:
            alphabet += string.ascii_lowercase
        if self.include_uppercase:
            alphabet += string.ascii_uppercase
        if self.include_numbers:
            alphabet += string.digits
        if self.include_special_symbols:
            alphabet += string.punctuation

        return alphabet

    def validate_arguments(self):
        if self.dont_begin_with_number_or_symbol and not (
            self.include_lowercase or self.include_uppercase
        ):
            return "Error: When using --no-first-number-or-symbol, you must also use -l or -u."

        if self.include_numbers and not (
            self.include_lowercase
            or self.include_uppercase
            or self.include_special_symbols
        ):
            if self.include_numbers and (
                self.dont_begin_with_number_or_symbol or self.no_repeated_characters
            ):
                return "Error: When using -n, you can't use -r or -f."

        return None

    def generate(self):
        if (
            not self.include_lowercase
            and not self.include_uppercase
            and not self.include_numbers
            and not self.include_special_symbols
        ):
            return "Please activate at least one of include_lowercase, include_uppercase, include_numbers, include_special_symbols"

        first_char_alphabet = ""

        if self.include_lowercase:
            first_char_alphabet += string.ascii_lowercase
        if self.include_uppercase:
            first_char_alphabet += string.ascii_uppercase
        if self.include_numbers and (
            not self.dont_begin_with_number_or_symbol
            or not (
                self.include_lowercase
                or self.include_uppercase
                or self.include_special_symbols
            )
        ):
            first_char_alphabet += string.digits
        if self.include_special_symbols and (
            not self.dont_begin_with_number_or_symbol
            or not (
                self.include_lowercase or self.include_uppercase or self.include_numbers
            )
        ):
            first_char_alphabet += string.punctuation

        if not first_char_alphabet:
            first_char_alphabet = string.ascii_letters

        for i in range(self.quantity):
            password = None
            while (
                not password
                or not any(c in password for c in self.alphabet)
                or (
                    self.dont_begin_with_number_or_symbol
                    and (password[0] in string.digits + string.punctuation)
                    and (self.include_lowercase or self.include_uppercase)
                )
                or (self.no_repeated_characters and len(set(password)) != len(password))
                or (
                    self.no_sequential_characters
                    and any(
                        password[i : i + 3] in string.ascii_letters + string.digits
                        for i in range(len(password) - 2)
                    )
                )
            ):
                password = secrets.choice(first_char_alphabet) + "".join(
                    secrets.choice(self.alphabet) for i in range(self.length - 1)
                )
            self.passwords.append(password)

        if self.quantity == 1:
            return self.passwords[0]

        return self.passwords

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("length", type=int, help="the length of the password")
    parser.add_argument(
        "-l", "--lowercase", action="store_true", help="include lowercase letters"
    )
    parser.add_argument(
        "-u", "--uppercase", action="store_true", help="include uppercase letters"
    )
    parser.add_argument("-n", "--numbers", action="store_true", help="include numbers")
    parser.add_argument(
        "-s", "--symbols", action="store_true", help="include special symbols"
    )
    parser.add_argument(
        "-f",
        "--no-first-number-or-symbol",
        action="store_true",
        help="the password cannot begin with a number or symbol",
    )
    parser.add_argument(
        "-r",
        "--no-repeated-characters",
        action="store_true",
        help="the password cannot contain the same character more than once",
    )
    parser.add_argument(
        "-q",
        "--quantity",
        type=int,
        default=1,
        help="the number of passwords to generate",
    )
    parser.add_argument(
        "--no-sequential-characters",
        action="store_true",
        help="the password cannot contain sequential characters",
    )
    args = parser.parse_args()

    generator = PasswordGenerator(
        args.length,
        args.lowercase,
        args.uppercase,
        args.numbers,
        args.symbols,
        args.no_first_number_or_symbol,
        args.no_repeated_characters,
        args.no_sequential_characters,
        args.quantity,
    )

    validation_error = generator.validate_arguments()
    if validation_error:
        print(validation_error)
        sys.exit(1)

    passwords = generator.generate()

    print(passwords)
