"""This is the example module.

This module does stuff.
"""

import os
import urllib.parse
import urllib.request
from pathlib import Path

from retroget import registry


def scheduler(
    roms: list[str],
    system: str,
    output_path: Path,
) -> None:
    """A dummy docstring."""

    systeminfo = registry.systeminfo()
    config = systeminfo[system]

    num_roms = len(roms)

    for i, name in enumerate(roms, start=1):

        file_name = f"{name}{config['extension']}"

        url = urllib.parse.urljoin(config["repo"], file_name)

        output_file = Path(os.path.join(output_path, file_name))

        print(f'(ROM {i}/{num_roms}) Downloading "{output_file.name}"')
        get(url, output_path=output_file)


def get(url: str, output_path: Path) -> None:
    """A dummy docstring."""

    os.makedirs(output_path.parent, exist_ok=True)

    encoded_url = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=")

    try:
        urllib.request.urlretrieve(encoded_url, output_path)
    except urllib.error.HTTPError as err:
        print(f"{output_path.name}: {err}")
    except urllib.error.URLError as err:
        print(f"Unable to connect, {err}")
