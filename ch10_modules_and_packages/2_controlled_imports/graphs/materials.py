
def spam():
    print('spam')

def grok():
    print('grok')

def unf():
    print('unf')

#Only export spam and grok
#Note this only works for 'from x import *'
__all__ = ['spam', 'grok']
