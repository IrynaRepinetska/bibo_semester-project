require 'exlibris-primo'
#search = Exlibris::Primo::Search.new(:base_url => "http://primo.kobv.de",:institution => "HU Berlin")
search = Exlibris::Primo::Search.new(:base_url => "http://primo.kobv.de/primo_library/libweb/action/search.do?vid=FUB",:institution => "HU Berlin")
search.add_query_term "xml", "any", "exact"
count = search.size
facets = search.facets
records = search.records
p search
p 
p facets
p 
p records
