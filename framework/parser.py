from utils.types import Object
from grammar import Rule


class Parser(Object):
	def __init__(self):
		self.rules = []

	def add_rule(self, rule, handler):
		self.rules.append(Rule(rule, handler))
