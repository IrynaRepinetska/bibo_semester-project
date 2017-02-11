#!/usr/bin/python3
import string
import re
from urllib.request import urlopen
from urllib.parse import urlparse, urlunparse, urljoin, parse_qsl, urlencode
from bs4 import BeautifulSoup as Bsoup
from bs4 import Comment
from multiprocessing import Pool

def build_keyword(opt, field):
    """
    Function checks if opt contains exact or contain to decide which opt belongs to which
    code. Then Builds the string and retuns a url equivalent of search query for one word
    """
    #TODO Try clause not working
    search = '&vl(freeText' + field  + ')=' + opt[0]
    try:
        if len(opt)==3:
            if opt[1] == 'exact' or opt[1] == 'contains':
                search = '&vl(1UI0)=' + opt[1] + search
                search = '&vl(123424466UI0)=' + opt[2] + search
            else:
                search = '&vl(1UI0)=' + opt[2] + search
                search = '&vl(123424466UI0)=' + opt[1] + search

        elif len(opt)==2:
            if opt[1] == 'exact' or opt[1] == 'contains':
                search = '&vl(123424466UI0)=any' + '&vl(1UI0)=' + opt[1] + search
            else:
                search = '&vl(123424466UI0)=' + opt[1] + '&vl(1UI0)=contains' + search
        else:
            search = '&vl(123424466UI0)=any&vl(1UI0)=contains' + search
    except (TypeError):
        print('No valid option!')
    return search

def build_url(base, tail , term1, term2=None, term3=None, time=None, material=None, lang=None):
    """
    Builds the whole search url
    Usage:Base URL of Primo libary
    term[1-3]: A List containing at least the searchword
    time, material, lang: Valid opt from Primo as string (to be included)
    !Every opt thats not used has to be called with False!
    """
    url = base + build_keyword(term1, '0')
    if term3:
        url = url + build_keyword(term2, '1') + build_keyword(term3, '2')
    elif term2:
        url = url + build_keyword(term2, '1')
    if time:
        url = url + '&vl(123424475UI6)=' + time
    if material:
        url = url + '&vl(123424476UI7)=' + material
    if lang:
        url = url + '&vl(123424477UI8)=' + lang
    return url + tail

base ='http://primo.kobv.de/primo_library/libweb/action/search.do?tab=default_tab'
tail ='&Submit=&fn=search&ct=search&mode=Advanced&vid=hub_ub&indx=1&dum=true&srt=rank&initialSearch=true'

"""
author  = lambda target: hit['author'] = target.find("li",{"id":"Autor-1"}).find('a').contents[0]
publ    = lambda target: target.find("li", {"id":"Verlag-1"}).find('span').contents[0]
year    = lambda target: target.find("li",{"id":"Erscheinungsjahr-1"}).find('span').contents[0] 
forma   = lambda target: target.find("li", {"id":"Format-1"}).find('span').contents[0]
ids     = lambda target: target.find("li", {"id":"Identifikator-1"}).find('span').contents[0]
desc    = lambda target: target.find("li", {"id":"Beschreibung-1"}).find('span').contents[0]
connect = lambda target: target.find("li", {"id":"Verknüpfte Titel-1"}).find('span').contents[0]
lang    = lambda target: str(target.find("li",{"id":"Sprache-1"}).contents[8]).strip('\t\n')
rvk     = lambda target: target.find("li", {"id":"RVK-Klassifikation-1"}).find('a').contents[0]
source  = lambda target: target.find("li", {"id":"Quelle-1"}).find('span').contents[0]

author2  = lambda target: target.find("li",{"id":"Autor1"}).find('a').contents[0]
publ2    = lambda target: target.find("li", {"id":"Verlag1"}).find('span').contents[0]
year2    = lambda target: target.find("li",{"id":"Erscheinungsjahr1"}).find('span').contents[0] 
forma2   = lambda target: target.find("li", {"id":"Format1"}).find('span').contents[0]
ids2     = lambda target: target.find("li", {"id":"Identifikator1"}).find('span').contents[0]
desc2    = lambda target: target.find("li", {"id":"Beschreibung1"}).find('span').contents[0]
connect2 = lambda target: target.find("li", {"id":"Verknüpfte Titel1"}).find('span').contents[0]
lang2    = lambda target: str(target.find("li",{"id":"Sprache1"}).contents[8]).strip('\t\n')
rvk2     = lambda target: target.find("li", {"id":"RVK-Klassifikation1"}).find('a').contents[0]
source2  = lambda target: target.find("li", {"id":"Quelle1"}).find('span').contents[0]
"""

def author(target, hit):
    hit['author']   = target.find("li",{"id":"Autor-1"}).find('a').contents[0]
def publ(target, hit):
    hit['publ']     = target.find("li", {"id":"Verlag-1"}).find('span').contents[0]
def year(target, hit):
    hit['year']     = target.find("li",{"id":"Erscheinungsjahr-1"}).find('span').contents[0]
def forma(target, hit):
    hit['forma']    = target.find("li", {"id":"Format-1"}).find('span').contents[0]
def ids(target, hit):
    hit['ids']      = target.find("li", {"id":"Identifikator-1"}).find('span').contents[0]
def desc(target, hit):
    hit['desc']     = target.find("li", {"id":"Beschreibung-1"}).find('span').contents[0]
def connect(target, hit):
    hit['connect']  = target.find("li", {"id":"Verknüpfte Titel-1"}).find('span').contents[0]
def lang(target, hit):
    hit['lang']     = str(target.find("li",{"id":"Sprache-1"}).contents[8]).strip('\t\n')
def rvk(target, hit):
    hit['rvk']      = target.find("li", {"id":"RVK-Klassifikation-1"}).find('a').contents[0]
def source(target, hit):
    hit['source']   = target.find("li", {"id":"Quelle-1"}).find('span').contents[0]

def author2(target, hit):
    hit['author']   = target.find("li",{"id":"Autor1"}).find('a').contents[0]
def publ2(target, hit):
    hit['publ']     = target.find("li", {"id":"Verlag1"}).find('span').contents[0]
def year2(target, hit):
    hit['year']     = target.find("li",{"id":"Erscheinungsjahr1"}).find('span').contents[0]
def forma2(target, hit):
    hit['forma']    = target.find("li", {"id":"Format1"}).find('span').contents[0]
def ids2(target, hit):
    hit['ids']      = target.find("li", {"id":"Identifikator1"}).find('span').contents[1]
def desc2(target, hit):
    hit['desc']     = target.find("li", {"id":"Beschreibung1"}).find('span').contents[0]
def connect2(target, hit):
    hit['connect']  = target.find("li", {"id":"Verknüpfte Titel1"}).find('span').contents[0]
def lang2(target, hit):
    hit['lang']     = str(target.find("li",{"id":"Sprache1"}).contents[8]).strip('\t\n')
def rvk2(target, hit):
    hit['rvk']      = target.find("li", {"id":"RVK-Klassifikation1"}).find('a').contents[0]
def source2(target, hit):
    hit['source']   = target.find("li", {"id":"Quelle1"}).find('span').contents[0]

functions =[author, publ, year, forma, ids, desc, connect, lang, rvk, source,
        author2, publ2, year2, forma2, ids2, desc2, connect2, lang2, rvk2, source2]



html = urlopen(build_url(base,tail,['xml']))
soup = Bsoup(html, 'lxml')
docs=[]
for targeter in soup.find_all('li', {'class':'EXLDetailsTab EXLResultTab '}):
    #pool = Pool(processes=10)
    hit={}
    co = ""
    link = targeter.find("a").text.strip(), '=>', targeter.find("a").attrs['href']
    target = Bsoup(urlopen("http://primo.kobv.de/primo_library/libweb/action/display.do"
        +re.search(r'\?tabs.*',str(link)).group(0)), 'lxml')
    for func in functions:
        try:
            #pool.apply_async(func, [target,hit])
            func(target, hit)
        except:
            pass
    docs.append(hit)
    print(hit)
    """
    print("http://primo.kobv.de/primo_library/libweb/action/display.do"
        +re.search(r'\?tabs.*',str(link)).group(0))
"""
