from urllib.request import urlopen
from urllib.parse import urlparse, urlunparse, urljoin, parse_qsl, urlencode
from bs4 import BeautifulSoup as Bsoup

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
        url = url + '&vl(123424476UI6)=' + material
    if lang:
        url = url + '&vl(123424477UI6)=' + lang
    return url + tail

base ='http://primo.kobv.de/primo_library/libweb/action/search.do?tab=default_tab'
tail ='&Submit=&fn=search&ct=search&mode=Advanced&vid=hub_ub&indx=1&dum=true&srt=rank&initialSearch=true'
"""print(build_url(base,tail,['xml']))
print(build_url(base,tail,['xml'],['html']))
print(build_url(base,tail,['xml'],['html'],['zucker']))
print(build_url(base,tail,['xml'],False,False,'20-YEAR'))
print(build_url(base,tail,['xml'],False,False,False,'maps'))
print(build_url(base,tail,['xml'],False,False,False,False,'ger'))
"""

"""playing with html"""
pattern =[x for x in input('Three comma seperated keywords: ').split(',')]
#html = urlopen(build_url(base,tail,pattern))
#soup = Bsoup(html, 'lxml')
print(build_url(base,tail,pattern))

"""#every element(book) contains in a tr element wit id "exlidResult[0..9]"
tr = "exlidResult"
#parse html
#print all tr elements
#print(soup.find_all('tr'))
x = html.read()
x = str(x).replace("\\n","").replace("\\t","").replace("\\r","")
print(x)"""
