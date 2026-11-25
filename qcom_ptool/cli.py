# Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
# SPDX-License-Identifier: BSD-3-Clause
"""
``qcom-ptool`` - the command line, and its only entry point.

Every subcommand module exposes ``register(subparsers)``, which declares
its arguments and binds them to its ``run(args) -> int``.
"""

from __future__ import annotations

import argparse

from qcom_ptool import __version__, build, gen_udev_rules, show

COMMANDS = (build, show, gen_udev_rules)
SUBCOMMANDS = tuple(command.NAME for command in COMMANDS)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="qcom-ptool",
        description="Qualcomm partition tool - GPT partition table and flashing artifact generator.",
    )
    root.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = root.add_subparsers(dest="subcommand", metavar="subcommand", required=True)
    for command in COMMANDS:
        command.register(subparsers)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    result: int = args.run(args)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
