from enum import Enum
from typing import Dict, Any, Tuple


class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACKET = '['
    RIGHT_BRACKET = ']'
    LEFT_CURLY_BRACE = '{'
    RIGHT_CURLY_BRACE = '}'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    COLON = ':'
    SEMICOLON = ';'
    SLASH = '/'
    BACKSLASH = '\\'
    STAR = '*'
    UNDERSCORE = '_'
    QUOTATION_MARK = '?'
    PERCENT = '%'
    AT_SIGN = '@'
    AMPERSAND = '&'
    DOLLAR_SIGN = '$'
    CARET = '^'
    TILDE = '~'
    PIPE = '|'

    # One or two+ character tokens
    BANG = '!'
    BANG_EQUAL = '!='
    EQUAL = '='
    EQUAL_EQUAL = '=='
    GREATER = '>'
    GREATER_EQUAL = '>='
    LESS = '<'
    LESS_EQUAL = '<='
    ARROW = '=>'
    SHEBANG = '#!'
    HASH = '#'
    ELLIPSIS = '...'
    TRIPLE_QUOTE = '"""'

    # Keywords
    GET = 'akiri'
    SET = 'aro'
    DELETE = 'forigi'
    AND = 'kaj'
    OR = 'aux'
    NOT = 'ne'
    IF = 'se'
    ELSE = 'alie'
    SWITCH = 'sxalti'
    CASE = 'kazo'
    WHEN = 'kiam'
    WHILE = 'dum'
    UNLESS = 'krom-se'
    BREAK = 'rompu'
    FOR = 'por'
    IN = 'en'
    DO = 'faru'
    NULL = 'nula'
    TRUE = 'vera'
    FALSE = 'malvera'
    TRY = 'provu'
    CATCH = 'kapti'
    FINALLY = 'fine'
    NEW = 'nova'
    CLASS = 'klaso'
    EXTENDS = 'etendas'
    SUPER = 'super'
    SELF = 'mem'
    THIS = 'cxi-tio'
    INTERFACE = 'interfaco'
    IMPLEMENTS = 'ilojn'
    FUNCTION = 'funkcio'
    RETURN = 'reveni'
    GENERATOR = 'generatoro'
    YIELD = 'cedi'
    ASYNC = 'nesinkronigi'
    AWAIT = 'atendu'
    STATIC = 'statika'
    LAMBDA = 'lambda'
    CONST = 'konstanta'
    LET = 'lasu'
    VAR = 'var'
    PRIVATE = 'privata'
    END = 'fino'
    PRINT = 'presi'

    # String starters
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    # New line
    NEW_LINE = '\n'

    # Space
    TAB = '\t'
    SPACE = ' '

    # String terminator
    NULL_CHARACTER = '\0'

    # End-user identifiers
    IDENTIFIER = 'identigilo'
    INTEGER = 'entjero'
    FLOAT = 'flosi'
    STRING = 'sxnuro'

    # end-of-file
    EOF = ''


_keywords: Tuple[str] = (
    'vera', 'malvera', 'nula', 'kaj', 'aux', 'se', 'alie', 'funkcio', 'reveni',
    'por', 'klaso', 'super', 'cxi-tio', 'konstanta', 'lasu', 'dum', 'var', 'presi'
)

KEYWORDS: Dict[str, TokenType] = {key: TokenType(key) for key in _keywords}

SINGLE_CHARS: Tuple[str] = (
    '(', ')', '{', '}', ',', '.', '-', '+', ';', '*',
)

ONE_OR_MORE_CHARS: Tuple[str] = ('!', '!=', '=', '==', '>', '>=', '<', '<=')

WHITESPACE: Tuple[str] = (' ', '\r', '\t')

STRING_STARTERS: Tuple[str] = ('"', "'")


class Token:
    def __init__(
            self,
            typ: TokenType,
            lexeme: str,
            literal: Any,
            line: int
    ) -> None:
        self.type = typ
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f'{self.type}: {self.lexeme}, {self.literal}, {self.line}'

    def __repr__(self) -> str:
        properties = f'{self.type}, {self.lexeme}, {self.literal}, {self.line}'
        return f'{self.__class__.__name__}({properties})'
