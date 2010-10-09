import re

from zope.interface import implements, Interface
from zope.component import adapts

from aaolm.typogrify.typogrify import typogrify

from plone.transformchain.interfaces import ITransform

class TypogrifyTransform(object):
    implements(ITransform)
    adapts(Interface, Interface) # any context, any request
    
    order = 1000
    
    def __init__(self, published, request):
        self.published = published
        self.request = request
    
    def transformBytes(self, result, encoding):
        return typogrify(result)
        
    def transformUnicode(self, result, encoding):
        return typogrify(result)
    
    def transformIterable(self, result, encoding):
        return [typogrify(r) for r in result]
