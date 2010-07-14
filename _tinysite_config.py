base = '/p/ocw_physics/'

default_filters = [filters.outline]

default_vars = {
	'course': '',
}

var_filters = {
	'lecture': int,
}

def url_pattern(x):
	return (x+'.html').replace('index.html', '')
	
import markdown
from markdown import etree

class TagToTagPattern(markdown.inlinepatterns.Pattern):
	def __init__ (self, stag, tag, attr, verbatim=True):
		markdown.inlinepatterns.Pattern.__init__(self, r'\<%s\>([^\<]+)\<\/%s\>'%(stag, stag))
		self.tag = tag
		self.attr = attr
		self.verbatim=verbatim

	def handleMatch(self, m):
		el = etree.Element(self.tag)
		el.text = markdown.AtomicString(m.group(2))
		for i in self.attr:
			if self.attr[i]=='$':
				v=m.group(2)
			else:
				v=self.attr[i]
			el.set(i, v)
		return el
		
class MathExtension(markdown.Extension):
	def extendMarkdown(self, md, md_globals):
		# Insert instance of 'mypattern' before 'references' pattern
		md.inlinePatterns.add('mathpattern', TagToTagPattern('math', 'span', {'class':'math'}), '_begin')
		md.inlinePatterns.add('mathpattern2', TagToTagPattern('m', 'span', {'class':'math'}), '_begin')
        
        
filters.md.registerExtensions( [
	MathExtension()
], {})
