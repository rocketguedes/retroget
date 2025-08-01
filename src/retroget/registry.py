"""This is the example module.

This module does stuff.
"""

import json
import sys
from pathlib import Path

SYSTEMINFO = Path("systeminfo.json")


def systeminfo(json_file: Path = SYSTEMINFO) -> dict[str, dict[str, str]]:
    """A dummy docstring."""

    try:
        return json.loads(json_file.read_text())
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)


def choices(system: str) -> bool:
    """A dummy docstring."""

    return system in systeminfo()
