from urllib.request import urlopen
from urllib.parse import urlparse, urlunparse, urljoin, parse_qsl, urlencode
from bs4 import BeautifulSoup as Bsoup

#TODO didn't help for now
def encoded_dict(in_dict):
    out_dict = {}
    for k, v in in_dict.items():
        if isinstance(v, str):
            v = v.encode('utf8')
        elif isinstance(v, bytes):
            # Must be encoded in UTF-8
            v.decode('utf8')
        out_dict[k] = v
    return out_dict


"""playing with url's"""
#body ="&vl%28freeText0%29=" + pattern +"&fn=search"
#minimal search url wit search of xml
min_search = "http://primo.kobv.de/primo_library/libweb/action/search.do?&vl%28freeText0%29=xml&fn=search&mode=Basic&vid=hub_ub"
#encode url from base url and parameters
#TODO unicode problems % gets encode to %25
#pattern = [str(x) for x in input('Search Pattern').split()]
pattern = input("Insert Search Pattern. But just one...for now")
#TODO put extra parameters in dict fn modeand vid have to be there!!!
#TODO change dicht to list for multiple keys
params = {'fn':'search','mode':'Basic','vid':'hub_ub'}#,'vl%28freeText0%29':'xml'}
params['vl%28freeText0%29'] = pattern

base ='http://primo.kobv.de/primo_library/libweb/action/search.do?'
url = list(urlparse(base))
query = dict(parse_qsl(url[4]))
query.update(params)
url[4] = urlencode(query)
url = urlunparse(url)

#TODO temporary fix for unicode Problem
url=url.replace('%25','%')
print(url)

"""playing with html"""
html = urlopen(min_search)
#every element(book) contains in a tr element wit id "exlidResult[0..9]"
tr = "exlidResult"
#parse html
soup = Bsoup(html, 'lxml')
#print all tr elements
#print(soup.find_all('tr'))








"""
x = html.read()
x = str(x).replace("\\n","").replace("\\t","").replace("\\r","")
print(x)
"""
