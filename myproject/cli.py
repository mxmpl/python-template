import argparse


def parser_hello(subparsers) -> None:
    parser = subparsers.add_parser("hello", description="Welcome message")
    parser.add_argument("name")


def command_hello(args: argparse.Namespace) -> None:
    print(f"Hello {args.name}!")


def parser_goodbye(subparsers) -> None:
    parser = subparsers.add_parser("bye", description="Welcome message")
    parser.add_argument("name")


def command_goodbye(args: argparse.Namespace) -> None:
    print(f"Goodbye {args.name}!")


def main() -> None:
    """As set in pyproject.toml, this function is
    the entry point of this module.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title="myproject commands",
        description="Use 'myproject <command> --help' for more details.",
        dest="command",
    )

    parser_hello(subparsers)
    parser_goodbye(subparsers)
    args = parser.parse_args()

    if args.command == "hello":
        command_hello(args)
    elif args.command == "bye":
        command_goodbye(args)
