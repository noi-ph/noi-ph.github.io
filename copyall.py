#!/usr/bin/env python3.10

from argparse import ArgumentParser
from pathlib import Path
from shutil import copytree, rmtree


def main():
    parser = ArgumentParser(description="Copy editorial files from somewhere else. WARNING: DON'T USE THIS UNLESS THE CONTEST IS ALREADY OVER!")

    parser.add_argument('source', type=Path, help="Source folder")
    parser.add_argument('contest', type=Path, help="Contest path")

    args = parser.parse_args()

    source = args.source / args.contest / 'editorials'
    target = args.contest

    print("SOURCE IS", source)
    print("TARGET IS", target)

    if not source.is_dir():
        raise RuntimeError(f"{source} is not an existing folder")

    print(f"CLEARING FOLDER: {target}")
    rmtree(target, ignore_errors=True)

    print("COPYING STUFF")
    copytree(source, target)

    print()
    print("DONE. PLEASE RUN ./compileall.py NEXT")


if __name__ == '__main__':
    main()