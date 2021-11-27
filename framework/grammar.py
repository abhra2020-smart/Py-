from _types import Object
from inspect import isfunction


class Rule(Object):
	__slots__ = ('rule', 'handler')

	def __init__(self, rule, handler):
		self.rule = rule
		self.handler = handler

		assert isinstance(self.rule, str), f"Grammar rule must be a string, not a {type(self.rule).__name__}"
		assert isfunction(self.handler), f"Handler must be a function for grammar rule {self.rule}"
