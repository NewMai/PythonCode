#

class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
	pass
	
try:
	raise MyError(5)
except MyError as er:
	print("Error : ", er)
	
	