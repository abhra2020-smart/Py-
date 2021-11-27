from ._types import Object
from ._overload import *


class Token(Object, metaclass=OverloadMeta):
	__slots__ = ('type', 'value')

	@overload
	def __init__(self, type, value):
		self.type = type
		self.value = value

	@overload
	def __init__(self, type):
		self.value = None
		self.type = type

	def __eq__(self, other):
		if self.value:
			return self.type == other.type and self.value == other.value
		return self.type == other.type

	def __repr__(self):
		if self.value is not None:
			return f"{self.type}: {self.value}"
		return str(self.type)


class LexToken(Object):
	__slots__ = ("type", "values")

	def __init__(self, type, possible_values):
		self.type = type
		self.values = possible_values
