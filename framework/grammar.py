from utils.types import Object
from utils.errors import TypeErr
from inspect import isfunction


class Rule(Object):
	def __init__(self, rule, handler):
		self.rule = rule
		self.handler = handler

		if not isinstance(self.rule, str):
			raise TypeErr(f"Grammar rule must be a string, not a {type(self.rule).__name__}")
		if not isfunction(self.handler):
			raise TypeErr(f"Handler must be a function for grammar rule {self.rule}")
