from .token import *


class Lexer(Object):
	__slots__ = ('code', 'token_types', 'tokens')

	def __init__(self, code):
		self.code = code
		self.token_types: list[LexToken] = []
		self.tokens: list[Token] = []

	def add_token(self, token: LexToken):
		assert isinstance(token, LexToken), f"Token needs to be a LexToken object, not a {type(token).__name__}"
		self.token_types.append(token)

	def lex(self) -> list[Token]:
		for i in range(0, len(self.code)):
			char = self.code[i]
			for _i in range(0, len(self.token_types)):
				if char in self.token_types[_i].values:
					if len(self.token_types[_i].values) == 1:
						self.tokens.append(Token(self.token_types[_i].type))
						continue
					self.tokens.append(Token(self.token_types[_i].type, char))
		self.fix()
		return self.tokens

	def fix(self):
		idx = 0
		for i in self.tokens:
			if i.type == self.tokens[idx - 1].type:
				self.tokens[idx - 1].value = str(self.tokens[idx - 1].value) + str(self.tokens[idx].value)
				self.tokens.pop(idx)
			idx += 1
