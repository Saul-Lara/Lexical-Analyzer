import re

from TokenType import TokenType


class Token:
    """Represents a 'Token' identified during the analysis.

    Attributes:
        type: A string indicating the token type.
        value: A string with the value of the token.
        line: A string with the line number of the token.
    """

    def __init__(self, type: str, value: str, line: str):
        """Initializes a new Token instance with a type and value.

        Args:
            type: Define the 'TokenType' corresponding to the type of the 'Token'.
            value: Define the 'String' value of the token. The actual characters of the lexeme.
            line: Define the line number where the token was encountered.
        """
        self.type = type
        self.value = value
        self.line = line


class Lexer:
    """Represents a tokenizer for source code analysis.

    Attributes:
        input: A string with the source code to tokenize.
        position: Current position in the source code.
        current_char: Current character being processed.
        line: Current line number
    """

    def __init__(self, input: str):
        """Initializes a Lexer instance with the source code provided.

        Args:
            input: A string with the source code.
        """
        self.input = input
        self.position = 0
        self.current_char = self.input[self.position]
        self.line = 0

    def advance(self):
        """Moves the current position in the input string.

        Args:
            None

        Updates:
            position: Increments by 1 to indicate the next character position.
            current_char: The next character in the input string or `None` if the end of the string is reached.
        """
        self.position += 1
        self.current_char = (
            self.input[self.position]
            if self.position < len(self.input)
            else None
        )

    def extract_tokens(self):
        """Tokenizes the input text and generates a list of tokens.

        Returns:
            list: A list of Token objects representing the parsed tokens.
        """
        is_newline = True
        is_rem = False
        tokens = []

        while self.current_char is not None:
            char = self.current_char

            # Handle newlines
            if char == "\n":
                is_newline = True
                self.advance()
                continue

            # Skip whitespace
            elif char.isspace():
                self.advance()
                continue

            # Line must start with a line number
            if is_newline and self.current_char in TokenType["DIGITS"].value:
                token_value = self.recognize_number()
                tokens.append(
                    Token(
                        TokenType["LINE_NUMBER"].value,
                        token_value,
                        token_value,
                    )
                )
                self.line = token_value
                is_newline = False

            # Handle comments
            elif (
                is_rem
                and self.current_char
                in TokenType["LETTERS"].value + TokenType["DIGITS"].value
            ):
                tokens.append(
                    Token(
                        TokenType["COMMENT"].value,
                        self.recognize_comment(),
                        self.line,
                    )
                )
                is_rem = False

            # Get numbers
            elif self.current_char in TokenType["DIGITS"].value:
                tokens.append(
                    Token(
                        TokenType["NUMBER"].value,
                        self.recognize_number(),
                        self.line,
                    )
                )

            # Get strings
            elif self.current_char == '"':
                tokens.append(
                    Token(
                        TokenType["STRING"].value,
                        self.recognize_string(),
                        self.line,
                    )
                )

            # Get identifiers
            elif self.current_char in TokenType["LETTERS"].value:
                token_value = self.recognize_identifier()
                token_type = self.recognize_token_type(token_value)
                if token_value == "REM":
                    is_rem = True
                tokens.append(Token(token_type, token_value, self.line))

            # Get operators
            elif self.current_char in TokenType["SYMBOLS"].value:
                token_value = self.recognize_operator()
                token_type = self.recognize_token_type(token_value)
                tokens.append(Token(token_type, token_value, self.line))

        return tokens

    def recognize_number(self):
        number = ""

        while (
            self.current_char
            and self.current_char in TokenType["DIGITS"].value
        ):
            number += self.current_char
            self.advance()

        return number
