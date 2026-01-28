class WaterError(Exception):
	pass

try:
	raise WaterError("Water Error", "tmp", "ls", "ar", a="Hello world")
except WaterError as e:
	print(e)
