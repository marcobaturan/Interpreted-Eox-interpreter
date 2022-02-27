from pathlib import Path
from sys import version_info, platform

from Eox.interpreter import Interpreter, EoxRuntimeError
from Eox.parser import Parser, ParseError
from Eox.scanner import Scanner
from Eox.tokens import Token, TokenType


def Eox_copyright():
    print(
        'Not copyright.\n'
        'Ne copirajto.\n'
    )


def Eox_license():
    print('MIT License')


def Eox_credits():
    print(
        'Thank for GitHub community and authors of Eox and python-Eox'
        'Eox development. See example.org for more information.'
    )


COMMANDS = {
    'eliru': exit,
    'kreditojn': Eox_credits,
    'kopirajton': Eox_copyright,
    'Licencon': Eox_license,
}


class Eox:
    interpreter = Interpreter()
    had_error = False
    had_runtime_error = False

    @staticmethod
    def repl_intro() -> None:
        python_version = '.'.join(str(i) for i in version_info[:3])

        print(
            'Eox REPL',
            f'[CPython {python_version}] en {platform}',
            'tajpu "kopirajton", "kreditojn" aŭ "licencon" por pliaj informoj.',
            'Tajpu "eliru" aŭ premu Ctrl-D (t.e. EOF) por foriri.',
            sep='\n'
        )

    @staticmethod
    def usage(code: int) -> None:
        print('Uzado: Eox [dosiero]')
        exit(code)

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f'[linio {line}] eraro {where}: {message}')

        Eox.had_error = True

    @staticmethod
    def error(token: Token, message: str) -> None:
        if token.type == TokenType.EOF:
            Eox.report(token.line, ' fine ', message)
        else:
            Eox.report(token.line, f" cxe '{token.lexeme}'", message)

    @staticmethod
    def runtime_error(error: EoxRuntimeError) -> None:
        print(f'{error}\n[linio {error.token.line}]')

        Eox.had_runtime_error = True

    @staticmethod
    def run(source: str) -> None:
        try:
            scanner = Scanner(source)
            tokens = scanner.scan_tokens()
            parser = Parser(tokens)
            stmts = parser.parse()

            Eox.interpreter.interpret(stmts)
        except ParseError as pe:
            Eox.error(pe.token, str(pe))
        except EoxRuntimeError as lre:
            Eox.runtime_error(lre)

    @staticmethod
    def run_file(filename) -> None:
        path = Path(filename).absolute()
        source = path.read_text(encoding='utf-8', errors='strict')
        Eox.run(source)

        if Eox.had_error:
            exit(65)
        elif Eox.had_runtime_error:
            exit(70)

    @staticmethod
    def prompt() -> None:
        Eox.repl_intro()

        while True:
            try:
                print('>>> ', end='')

                expr = input()
                first = expr.split(' ')[0]

                if first in COMMANDS:
                    COMMANDS[first]()
                else:
                    Eox.run(expr)
                    Eox.had_error = False
                    Eox.had_runtime_error = False
            except KeyboardInterrupt as ki:
                print(f'\n{ki.__class__.__name__}')
            except EOFError:
                exit(0)
