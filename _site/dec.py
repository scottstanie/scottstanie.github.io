print '****'*10
print 'DECORATOR: NO ARGS'
print '****'*10
class decNoArgs(object):
	def __init__(self, func):
		'''with no dec args, funciton to be decorated is passed
		to the constructor, exeuted at time of decoration'''
		self.func = func
		print 'inside __init__()'

	def __call__(self, *a, **kw):
		'''___call__ not called until the decorated function is called'''
		print 'inside __call__'
		print '*a', a
		print '**kw', kw
		self.func(*a, **kw)
		print 'after self.f(*a, **kw)'


@decNoArgs
def sayHi(a1, a2, k1=None, k2=None):
	print 'Hi! args:', a1, a2, 'kw', k1, k2


print 'after decoration'

print 'prapare to call sayHi()'
sayHi('say', 'hi', k1='to', k2='me')
print 'prapare to call sayHi()'
sayHi('diff', 'set', k1='of', k2='stuff')
print 'after second call'

print '****'*10
print 'DECORATOR WITH ARGS'
print '****'*10

class decWithArgs(object):
	def __init__(self, a1, a2, kw1=None):
		print '__init__'
		self.a1 = a1
		self.a2 = a2
		self.kw1 = kw1

	def __call__(self, f):
		print '__call__'

		def wrapped_f(*a, **kw):
			# Do f in here with extra stuff
			# You can access the decorator args with self.a1...
			print 'wrapped_f()'
			print 'Function args:'
			print '*a', a
			print '**kw', kw
			print 'dec args: ', self.a1, self.a2, self.kw1
			f(*a, **kw)
			print 'after f(*a, **kw)'
		# __call__ must return a function that takes in f,
		# the function getting decorated, as an argument
		return wrapped_f


@decWithArgs('arg1', 'arg2', kw1='KW1')
def sayHi2(a1, a2, k1=None, k2=None):
	print 'Hi! args:', a1, a2, 'kw', k1, k2

print 'prapare to call sayHi2()'
(set-background-color "honeydew")
sayHi2('say', 'hi', k1='to', k2='me')
print 'prapare to call sayHi2()'
sayHi2('diff', 'set', k1='of', k2='stuff')
print 'after second call'

print '****'*10
print 'FUNCTION DECORATOR WITH ARGS'
print '****'*10


def funcWithArgs(a1, a2, kw1=None):
	print 'in funcWithArgs'

	def wrap(f):
		print 'in wrap'

		def wrapped_f(*a, **kw):
			print 'third level deep'
			print 'have func args:'
			print a, kw
			print 'and dec args'
			print a1, a2, kw1
			f(*a, **kw)
			print 'after f(*a, **kw)'

		return wrapped_f
	return wrap


@funcWithArgs('arg1', 'arg2', kw1='KW1')
def sayHi3(a1, a2, k1=None, k2=None):
	print 'Hi! args:', a1, a2, 'kw', k1, k2

print 'prapare to call sayHi3()'
sayHi3('say', 'hi', k1='to', k2='me')
print 'prapare to call sayHi3()'
sayHi3('diff', 'set', k1='of', k2='stuff')
print 'after second call'

