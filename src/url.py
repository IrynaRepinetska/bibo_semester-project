#!/usr/bin/python2
# coding: utf8
import string
import itertools
import re
import urllib2 as ul
#python 3 Version
#from urllib.request import urlopen
from bs4 import BeautifulSoup as Bsoup
from bs4 import Comment
import crawl


def build_keyword(term, opt, field):
    """
    Function checks if opt contains exact or contain to decide which opt belongs to which
    code. Then Builds the string and retuns a url equivalent of search query for one word
    """
    #modes={'any':'225352144UI0', 'creator':'200784467UI0', 'title':'225352144UI0',
    #        'lsr48':'225352144UI0', 'isbn':'200784467UI0', 'issn':'225463117UI2'}
    modes={'0':'225352144UI0', '1':'225352247UI1', '2':'225463117UI2'}
    search = '&vl('+modes[str(field)]+')=' + opt + '&vl(freeText' + str(field)  + ')=' + term.replace(" ","+")
    return search

def build_url(request, time=None, material=None, lang=None):
    base='http://hu-berlin.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?searchscope=Primus'
    tail ='&Submit=&fn=search&ct=search&mode=Advanced&vid=hub_ub&indx=1&dum=true&srt=rank&initialSearch=true'
    url = base
    field_num=0
    for term in request:
        if term == 'coauthor':
            url = url + build_keyword(request[term],'creator',field_num)
        else:
            url = url + build_keyword(request[term],term,field_num)
        field_num += 1
    return url+tail
    


#if __name__ == "__main__":
def crawler(request):
    functions =[crawl.title, crawl.creator, crawl.publ, crawl.year, crawl.forma, crawl.ids, crawl.desc, crawl.connect, crawl.lang, crawl.rvk, crawl.source,crawl.creator2, crawl.publ2, crawl.year2, crawl.forma2, crawl.ids2, crawl.desc2, crawl.connect2, crawl.lang2, crawl.rvk2, crawl.source2]
    base = "http://hu-berlin.hosted.exlibrisgroup.com/primo_library/libweb/action/"
    html = ul.urlopen(build_url(request))
    soup = Bsoup(html, 'lxml')
    docs=[]
    result_counter = 0
    for result_tab in soup.find_all('ul', {'class':'EXLResultTabs'})[0:6]:
        hit={}
        co = ""
        try:
            detail_link = base + result_tab.find(id="exlidResult"+ str(result_counter)  +"-detailsTabLink")['href']
        except Exception as e:
            #print "try no.1: "+ str(e)
            result_counter +=1
        try:
            place_link = base + result_tab.find(title="Bestand - "+ str(result_counter))['href']
        except Exception as e:
            #print 'place link error'
            pass
        try:
            req = ul.urlopen(detail_link).read()
            while 'Was ist neu' in req:
                req = ul.urlopen(detail_link).read()
            d_target =Bsoup(req, 'lxml')
            for func in functions:
                try:
                    func(d_target, hit)
                except:
                    pass
        except Exception as e:
            result_counter +=1
            #print str(e)
        try:
            req = ul.urlopen(place_link).read()
            while 'Was ist neu' in req:
                req = ul.urlopen(place_link).read()
            d_target =Bsoup(req, 'lxml')
            place_link = d_target.iframe['src']
            """link hides in iFrame"""
            req = ul.urlopen(place_link).read()
            while 'Was ist neu' in req:
                req = ul.urlopen(place_link).read()
            d_target =Bsoup(req, 'lxml')
            try:
                crawl.bib(d_target, hit)
            except:
                pass
            result_counter +=1
            docs.append(hit)
        except Exception as e:
            result_counter +=1
            #print str(e)
    return docs
    #print docs
