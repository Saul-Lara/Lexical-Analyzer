from src.Lexer import Lexer
from src.Parser import Parser


def test_validate_input_keyword_string_alnum_identifier():
    """
    Test a INPUT statement containing a string and an alphanumeric identifier
    is correctly parsed without errors.
    """
    raw_code = '10 INPUT "What is your name:"; NN$'
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_input_keyword_alnum_identifier():
    """
    Test a INPUT statement containing an alphanumeric identifier
    is correctly parsed without errors.
    """
    raw_code = "10 INPUT NN$"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_input_keyword_num_identifier():
    """
    Test a INPUT statement containing an numeric identifier
    is correctly parsed without errors.
    """
    raw_code = "10 INPUT N"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_print_keyword_string_alnum_identifier():
    """
    Test a PRINT statement containing a string and an alphanumeric identifier
    is correctly parsed without errors.
    """
    raw_code = '20 PRINT "Hello world";NN$'
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_print_keyword():
    """
    Test a PRINT statement is correctly parsed without errors.
    """
    raw_code = "20 PRINT"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_print_keyword_alnum_identifier():
    """
    Test a PRINT statement containing an alphanumeric identifier
    is correctly parsed without errors.
    """
    raw_code = "20 PRINT AS$"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_print_keyword_num_identifier():
    """
    Test a PRINT statement containing an numeric identifier
    is correctly parsed without errors.
    """
    raw_code = "20 PRINT N"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_if_keyword_alnum_identifier_operator_string_then_keyword_num_identifier_equals_number():
    """
    Test a IF statement containing an alphanumeric identifier, an operator, a string,
    THEN keyword, numeric identifier, equals and number
    is correctly parsed without errors.
    """
    raw_code = '25 IF AS$ = "hello" THEN N = 0'
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_alnum_identifier_equals_string():
    """
    Test an assignment containing an alphanumeric identifier, equals and a string
    is correctly parsed without errors.
    """
    raw_code = '25 AS$=""'
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_for_keyword_num_identifier_equals_number_to_keyword_num_identifier():
    """
    Test a FOR statement containing a numeric identifier, equals, number, TO keyword and a number
    is correctly parsed without errors.
    """
    raw_code = "25 FOR I=1 TO N"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_next_keyword_num_identifier():
    """
    Test an assignment containing an NEXT keyword and a numeric identifier
    is correctly parsed without errors.
    """
    raw_code = "25 NEXT I"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_goto_keyword_number():
    """
    Test an assignment containing an NEXT keyword and a number
    is correctly parsed without errors.
    """
    raw_code = "25 GOTO 10"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."


def test_validate_rem_keyword_comment():
    """
    Test an assignment containing an REM keyword and a comment
    is correctly parsed without errors.
    """
    raw_code = "25 REM This is a comment"
    tokens = Lexer(raw_code).extract_tokens()
    result = Parser(tokens).validate_syntax()

    assert result.get("successful") is True
    assert result.get("message") == "No errors found. Analysis successful."
