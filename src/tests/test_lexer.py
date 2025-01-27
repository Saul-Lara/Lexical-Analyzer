from src.Lexer import Lexer


def test_validate_line_number_token():
    """
    Test the extract_tokens function to ensure it returns line number token.
    """
    tokens = Lexer("10").extract_tokens()

    token_dicts = [
        {"type": token.type, "value": token.value, "line": token.line}
        for token in tokens
    ]

    expected_tokens = [{"type": "LINE NUMBER", "value": "10", "line": "10"}]

    assert token_dicts == expected_tokens


def test_validate_keyword_token():
    """
    Test the extract_tokens function to ensure it returns line number and END token.
    """
    tokens = Lexer("200 END").extract_tokens()

    token_dicts = [
        {"type": token.type, "value": token.value, "line": token.line}
        for token in tokens
    ]

    expected_tokens = [
        {"type": "LINE NUMBER", "value": "200", "line": "200"},
        {"type": "KEYWORD", "value": "END", "line": "200"},
    ]

    assert token_dicts == expected_tokens


def test_validate_identifier_plus_number_tokens():
    """
    Test the extract_tokens function to ensure it returns line number, identifier, plus and number token.
    """
    tokens = Lexer("20 r = r + 10").extract_tokens()

    token_dicts = [
        {"type": token.type, "value": token.value, "line": token.line}
        for token in tokens
    ]

    expected_tokens = [
        {"type": "LINE NUMBER", "value": "20", "line": "20"},
        {"type": "NUMERIC IDENTIFIER", "value": "r", "line": "20"},
        {"type": "EQUALS", "value": "=", "line": "20"},
        {"type": "NUMERIC IDENTIFIER", "value": "r", "line": "20"},
        {"type": "PLUS", "value": "+", "line": "20"},
        {"type": "NUMBER", "value": "10", "line": "20"},
    ]

    assert token_dicts == expected_tokens


def test_validate_identifier_string_tokens():
    """
    Test the extract_tokens function to ensure it returns line number, keyword and string token.
    """
    raw_code = '20 PRINT "Hello World!"'
    tokens = Lexer(raw_code).extract_tokens()

    token_dicts = [
        {"type": token.type, "value": token.value, "line": token.line}
        for token in tokens
    ]

    expected_tokens = [
        {"type": "LINE NUMBER", "value": "20", "line": "20"},
        {"type": "KEYWORD", "value": "PRINT", "line": "20"},
        {"type": "STRING", "value": "Hello World!", "line": "20"},
    ]

    assert token_dicts == expected_tokens


def test_validate_comment():
    """
    Test the extract_tokens function to ensure it returns line number, keyword and comment token.
    """
    raw_code = "185 REM This is a comment"
    tokens = Lexer(raw_code).extract_tokens()

    token_dicts = [
        {"type": token.type, "value": token.value, "line": token.line}
        for token in tokens
    ]

    expected_tokens = [
        {"type": "LINE NUMBER", "value": "185", "line": "185"},
        {"type": "KEYWORD", "value": "REM", "line": "185"},
        {"type": "COMMENT", "value": "This is a comment", "line": "185"},
    ]

    assert token_dicts == expected_tokens
