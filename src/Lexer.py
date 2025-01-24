import re


class Token:
    """Represents a 'Token' identified during the analysis.

    Attributes:
        type: A string indicating the token type.
        value: A string with the value of the token
    """

    def __init__(self, type: str, value: str):
        """Initializes a new Token instance with a type and value.

        Args:
            type: Define the 'TokenType' corresponding to the type of the 'Token'.
            value: Define the 'String' value of the token. The actual characters of the lexeme.
        """
        self.type = type
        self.value = value
