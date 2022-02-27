from sys import argv

from Eox.eox import Eox


def main(args) -> None:
    if len(args) > 1:
        Eox.usage(64)
    elif len(args) == 1:
        Eox.run_file(args[0])
    else:
        Eox.prompt()


main(argv[1:])
