"""This is the example module.

This module does stuff.
"""

import argparse
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def data(xml: os.PathLike) -> list[tuple[str, bool]]:
    """A dummy docstring."""

    try:
        tree = ET.parse(source=xml)
        root = tree.getroot()
    except ET.ParseError as err:
        print(xml, err)
        sys.exit(1)

    game_list: list[tuple[str, bool]] = []

    for game in root.findall("game"):

        name = game.get("name", default="")

        rom = game.find("rom")
        if rom is not None:
            mia = rom.get("mia") == "yes"
        else:
            mia = False

        game_list.append((name, mia))

    return game_list


def cli_parser() -> argparse.Namespace:
    """A dummy docstring."""

    parser = argparse.ArgumentParser()

    parser.add_argument("xml", type=Path, help="")
    parser.add_argument("--system", required=True, type=str, help="")
    parser.add_argument(
        "--overwrite", action="store_true", default=False, help=""
    )
    parser.add_argument(
        "--exclude-mia", action="store_true", default=False, help=""
    )
    parser.add_argument(
        "-o", "--output-path", type=Path, default="ROMs", help=""
    )

    return parser.parse_args()
