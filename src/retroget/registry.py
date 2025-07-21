"""This is the example module.

This module does stuff.
"""

import json
from pathlib import Path

SYSTEMINFO = Path("systeminfo.json")


def systeminfo(json_file: Path = SYSTEMINFO) -> dict[str, dict[str, str]]:
    """A dummy docstring."""

    return json.loads(json_file.read_text())


def choices(system: str) -> bool:
    """A dummy docstring."""

    return system in systeminfo()
