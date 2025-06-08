#!/usr/bin/env python3

import argparse
from pathlib import Path

SOLUTION_MARKER = "% SOLUTION"

def process_file(file_path: Path, hide_solutions: bool) -> None:
    printing = True

    with file_path.open('r', encoding='utf-8') as file:
        for line in file:
            if SOLUTION_MARKER in line:
                printing = not printing
                print()  # Insert a blank line on marker
            elif printing or not hide_solutions:
                print(line, end='')

def parse_args():
    parser = argparse.ArgumentParser(
        description="Prints a file, optionally hiding sections marked with '% SOLUTION'."
    )
    parser.add_argument(
        "--filename",
        type=Path,
        help="Path to the input text file."
    )
    parser.add_argument(
        "--hide-solutions",
        action="store_true",
        help="Hide lines between '% SOLUTION' markers."
    )

    args = parser.parse_args()

    if not args.filename.is_file():
        parser.error(f"File '{args.filename}' not found or is not a file.")

    return args.filename, args.hide_solutions

def main():
    file_path, hide_solutions = parse_args()
    process_file(file_path, hide_solutions)

if __name__ == "__main__":
    main()
