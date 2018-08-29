#pip install wikipedia
import wikipedia
print wikipedia.summary('Pythonidae')
print wikipedia.search('C++')

taipei = wikipedia.page('Taipei')
print taipei.title, taipei.url
print taipei.content
print taipei.links[0]
wikipedia.set_lang('zh')
print wikipedia.summary('Taipei', sentences=5)
wikipedia.set_lang('ja')
print wikipedia.summary('Taipei', sentences=5)