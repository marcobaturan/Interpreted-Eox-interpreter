# Eox language in Python

A Python (3.6+) implementation of the Lox language with a synthaxis in esperanto, from the in-progress book [Crafting Interpreters](https://craftinginterpreters.com/) by [Bob Nystrom](https://github.com/munificent).

This project is a port of **jlox**, the Java-based implementation presented throughout part of the book.

## What is Eox?

Eox is a full-featured, object-oriented scripting language with dynamic typing, garbage collection, lexical scope, first-class functions, closures, classes and inheritance, and more.
It is derived from Lox in python [Lox-Python](https://github.com/ehomrich/lox) as learning tool about how to implement interpreters. [the lox language](https://craftinginterpreters.com/the-lox-language.html)
In my case I do this for fun. I express my gratitude to the original author and the community. 
[Émerson P. Homrich](https://github.com/ehomrich) when I get the interpreter of interpreter for Eox I will do the same with the C compile version.


## Under development

This implementation is still ongoing, and there is a desire to extend the project later for educational purposes.

At the moment, the implementation follows almost every step and decision in the book, however:

- Not all challenges have been implemented yet.
- I'll be using `nula` instead of `nil`.
- I will try to handle both `int` and `float` numbers.
- The `TokenType` enum has many more tokens and keywords than those described by the book. I recorded all the ideas that came to mind while reading the language planning section.
- I add 'x' convention in substitution of circumflex accent.
## Requirements

The only requirement to run this project is Python 3.6+, due to the type hints used almost everywhere.

This project was developed on OS X, but it should work on any OS without any problems.
I'm testing on Ubuntu 21.04 with Python 3.9.7 without problems.

## Usage

#### REPL

```shell
python -m Eox
```

Enter `eliro` or press Ctrl+D to leave.

#### Running a file:

```shell
python -m Eox path/to/file
```

## Translated Keywords
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
    VARIABLE = 'variablo'
    PRIVATE = 'privata'
    END = 'fino'
    PRINT = 'presi'
    IDENTIFIER = 'identigilo'
    INTEGER = 'entjero'
    FLOAT = 'flosi'
    STRING = 'sxnuro'

## License

MIT License
