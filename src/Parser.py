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

# A nested dictionary representing a sparse FSM transition table.
# Outer keys: FSM state (row index).
# Inner keys: Input symbol (column index).
# Inner values: Next state.
sparse_transitions_table = {
    0: {0: 1},
    1: {
        0: 1,
        1: 2,
        2: 7,
        3: 12,
        4: 24,
        5: 41,
        6: 43,
        7: 38,
        8: 33,
        9: 30,
        10: 32,
    },
    2: {0: 1, 7: 6, 8: 5, 11: 3},
    3: {17: 4},
    4: {7: 6, 8: 5},
    5: {0: 1},
    6: {0: 1},
    7: {0: 1, 7: 10, 8: 11, 11: 8},
    8: {17: 9},
    9: {0: 1, 7: 10, 8: 11},
    10: {0: 1},
    11: {0: 1},
    12: {7: 13, 8: 14},
    13: {13: 15, 19: 15, 21: 15},
    14: {13: 16, 21: 16},
    15: {11: 17},
    16: {15: 18},
    17: {12: 19, 14: 12},
    18: {12: 19, 14: 12},
    19: {6: 21, 8: 20, 12: 19, 14: 12},
    20: {19: 22},
    21: {15: 23},
    22: {15: 23},
    23: {0: 1},
    24: {8: 25},
    25: {19: 26},
    26: {15: 27},
    27: {18: 28},
    28: {8: 29, 15: 29},
    29: {0: 1},
    30: {8: 31},
    31: {0: 1},
    32: {8: 29, 15: 29},
    33: {19: 34},
    34: {8: 35, 15: 35},
    35: {0: 1, 13: 36},
    36: {8: 37, 15: 37},
    37: {0: 1},
    38: {19: 39},
    39: {7: 40, 11: 40},
    40: {0: 1, 13: 39},
    41: {16: 42},
    42: {0: 1, 13: 39},
    43: {15: 44},
    44: {0: 1, 13: 39},
}
