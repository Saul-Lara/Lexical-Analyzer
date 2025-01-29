from TokenType import TokenType

# Mapping specific token types to their column in the transition table
input_transitions_map = {
    TokenType["LINE_NUMBER"].value: 0,
    TokenType["BASIC_KEYWORDS"].value[1]: 1,  # INPUT
    TokenType["BASIC_KEYWORDS"].value[0]: 2,  # PRINT
    TokenType["BASIC_KEYWORDS"].value[2]: 3,  # IF
    TokenType["BASIC_KEYWORDS"].value[5]: 4,  # FOR
    TokenType["BASIC_KEYWORDS"].value[8]: 5,  # REM
    TokenType["BASIC_KEYWORDS"].value[4]: 6,  # GOTO
    TokenType["ALNUM_IDENTIFIER"].value: 7,
    TokenType["NUM_IDENTIFIER"].value: 8,
    TokenType["BASIC_KEYWORDS"].value[7]: 9,  # NEXT
    TokenType["BASIC_KEYWORDS"].value[9]: 10,  # END
    TokenType["STRING"].value: 11,
    TokenType["BASIC_KEYWORDS"].value[3]: 12,  # THEN
    TokenType["PLUS"].value: 13,
    TokenType["LE"].value: 13,
    TokenType["GE"].value: 13,
    TokenType["MINUS"].value: 13,
    TokenType["TIMES"].value: 13,
    TokenType["DIVIDE"].value: 13,
    TokenType["OR"].value: 14,
    TokenType["NUMBER"].value: 15,
    TokenType["COMMENT"].value: 16,
    TokenType["SEMMICOLON"].value: 17,
    TokenType["BASIC_KEYWORDS"].value[6]: 18,  # TO
    TokenType["EQUALS"].value: 19,
    TokenType["UNKNOWN"].value: 20,
    TokenType["NE"].value: 21,
}
