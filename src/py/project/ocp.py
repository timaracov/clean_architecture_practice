from enum import Enum


## BAD BAD CODE


class Token(Enum):
    QMARK   = "?"
    EMARK   = "!"
    DOT     = "."
    SEMICOL = ";"
    ILLEGAL = ""
    # ADD HERE


def char_to_token(char: str):
    if len(char) > 1:
        raise ValueError("Char must be 1 character long")

    # AND MODIFY HERE
    match char:
        case "?": return Token.QMARK
        case "!": return Token.EMARK
        case ".": return Token.DOT
        case ";": return Token.SEMICOL
        case _: return Token.ILLEGAL


## GOOD CODE??


TOKENS = {
    "?": Token.QMARK,
    "!": Token.EMARK,
    ".": Token.DOT,
    ";": Token.SEMICOL,
    "" : Token.ILLEGAL,
    # ADD HERE
}


def char_to_token_cool(char: str):
    if len(char) > 1:
        raise ValueError("Char must be 1 character long")

    # EVERYTHING STAYS THE SAME
    if char in TOKENS:
        return TOKENS[char]
    return Token.ILLEGAL
