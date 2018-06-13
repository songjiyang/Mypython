class Sington():

	def __new__(cls,*args,**kwargs):
		if not hasattr(cls,'_instace'):
			orig = super()
			cls._instace = orig.__new__(cls,*args,**kwargs)
		return cls._instace


a = Sington()
b = Sington()
c = Sington()
print(a is b,a,b)
print(a is c)

def singleton(cls):
	instances = {}
	def get_instance(*args,**kwargs):
		if cls not in instances:
			instances[cls] = cls(*args,**kwargs)
		return instances[cls]
	return get_instance

@singleton
class MyClass():
	pass

x = MyClass()
y = MyClass()

print(x==y, x is y, x, y)
