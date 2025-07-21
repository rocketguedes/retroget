"""This is the example module.

This module does stuff.
"""

import os
import sys

from retroget import external, network, registry


def main() -> int:
    """A dummy docstring."""

    args = external.cli_parser()

    if not os.path.isfile(args.xml):
        print(f"{args.xml}: No such file or directory")
        return 1

    if not registry.choices(args.system):
        print(
            f"{args.system}: Invalid, check systeminfo.json for more details"
        )
        return 1

    rom_list: list[str] = []
    for name, mia in external.data(args.xml):

        if mia and args.exclude_mia:
            continue

        rom_list.append(name)

    network.scheduler(
        roms=rom_list,
        system=args.system,
        output_path=args.output_path,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
