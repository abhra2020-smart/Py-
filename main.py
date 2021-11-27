from framework.lexer import Lexer
from framework.token import LexToken

lexer = Lexer("12 + 367")

lexer.add_token(LexToken("NUMBER", "0123456789"))
lexer.add_token(LexToken("PLUS", "+"))

print(lexer.lex())
