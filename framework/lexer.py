from utils.types import Object
from utils.errors import TypeErr
from token import Token
from token import LexToken


class Lexer(Object):
	def __init__(self, code):
		self.code = code
		self.token_types: list[LexToken] = []
		self.tokens: list[Token] = []

	def add_token(self, token: LexToken):
		if not isinstance(token, LexToken):
			raise TypeErr(f"Token needs to be a LexToken object, not a {type(token).__name__}")
		self.token_types.append(token)

	def lex(self):
		for i in range(0, len(self.code)):
			char = self.code[i]
			for _i in range(0, len(self.token_types)):
				if char in self.token_types[_i].values:
					if len(self.token_types[_i].values) == 1:
						self.tokens.append(Token(self.token_types[_i].type))
						continue
					self.tokens.append(Token(self.token_types[_i].type), char)
		self.fix()
		return self.tokens

	def fix(self):
		for i in range(0, len(self.tokens)):
			if i == 0:
				continue
			if self.tokens[i].type == self.tokens[i-1].type:
				self.tokens[i-1].value += self.tokens[i].value
				self.tokens.pop(i-1)
