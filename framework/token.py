from utils.types import Object
from utils._overload import *


class Token(Object, metaclass=OverloadMeta):
	@overload
	def __init__(self, type, value):
		self.type = type
		self.value = value

	@overload
	def __init__(self, type):
		self.type = type

	def __eq__(self, other):
		if self.value:
			return self.type == other.type and self.value == other.value
		return self.type == other.type


class LexToken(Object):
	def __init__(self, type, possible_values):
		self.type = type
		self.values = possible_values
