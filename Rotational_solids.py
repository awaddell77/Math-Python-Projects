import math
import scipy.integrate


class Rotational_solids:
	def __init__(self, expression, bounds, r_axis, r_axis_value = 0):
		if hasattr(expression, '__call__'): self.expression = expression
	    else: raise TypeError("Expression must be function")
		self.bounds = bounds
		self.r_axis = r_axis
		self.r_axis_value = int(r_axis_value)
	



class Expression_pr:
	def __init__(self, expression, r_axis, r_axis_value):
		self.expression = expression
		self.r_axis = r_axis
		self.r_axis_value = int(r_axis_value)
		self._safe_op = {'+', '-', '/', '*', '**', '(', ')'}
    def parse_exp(self):
    	pass