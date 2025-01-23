from enum import Enum
import string


class TokenType(Enum):
    """Represents the different types of tokens that can be identified.

    This Enum class is used to categorize and define constants for various token types.

    Attributes:
        Each constant in the Enum represents a unique token type, making it easier to classify
        and process
    """

    LETTERS = string.ascii_letters
    DIGITS = '0123456789$'
    SYMBOLS = '+-*/=><;'

    # Keywords
    BASIC_KEYWORDS = [
        "PRINT",
        "INPUT",
        "IF",
        "THEN",
        "GOTO",
        "FOR",
        "TO",
        "NEXT",
        "REM",
        "END",
    ]

    # Special token types
    LINE_NUMBER = "LINE NUMBER"
    KEYWORD = "KEYWORD"
    UNKNOWN = "UNKNOWN"
    COMMENT = "COMMENT"

    # Delimiters
    SEMMICOLON = "SEMMICOLON"

    # Assignment operators
    EQUALS = "EQUALS"

    # Identifier and Literals
    NUM_IDENTIFIER = "NUMERIC IDENTIFIER"
    ALNUM_IDENTIFIER = "ALPHANUMERIC IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # Boolean operators
    OR = "OR"

    # Arithmetic operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    DIVIDE = "DIVIDE"

    # Comparison operators
    LE = "LESS EQUAL"
    GE = "GREATER EQUAL"
    NE = "NOT EQUAL"
