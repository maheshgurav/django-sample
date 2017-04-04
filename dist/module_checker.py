import sys

if __name__ == '__main__':
	try:
		import nltk
		print('\n nltk is installed')
	except Exception, ex:
		print('\n nltk is not installed')
	
	try:
		import distance
		print('\n distance is installed')
	except Exception, ex:
		print('\n distance is not installed')
	
	try:
		import sortedcontainers
		print('\n sortedcontainers is installed')
	except Exception, ex:
		print('\n sortedcontainers is not installed')

	try:
		import django
		print('\n django is installed')
	except ImportError:
		print('\n django is not installed')
		
	try:
		import djangorestframework
		print('\n djangorestframework is installed')
	except ImportError:
		print('\n djangorestframework is not installed')
