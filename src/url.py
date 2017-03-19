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
    #TODO Try clause not working
    search = '&vl(123424466UI0)=' + opt + '&vl(freeText' + str(field)  + ')=' + term
    return search
"""
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
"""

def build_url(request, time=None, material=None, lang=None):
    """
    Builds the whole search url
    Usage:Base URL of Primo libary
    term[1-3]: A List containing at least the searchword
    time, material, lang: Valid opt from Primo as string (to be included)
    !Every opt thats not used has to be called with False!
    """
    #base ='http://primo.kobv.de/primo_library/libweb/action/search.do?tab=default_tab'
    base='http://hu-berlin.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do?tab=default_tab'
    tail ='&Submit=&fn=search&ct=search&mode=Advanced&vid=hub_ub&indx=1&dum=true&srt=rank&initialSearch=true'
    url = base
    field_num=0
    for term in request:
        if term == 'coauthor':
            url = url + build_keyword(request[term],'author',field_num)
        else:
            url = url + build_keyword(request[term],term,field_num)
        field_num += 1
    return url+tail
    
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
    """


functions =[crawl.author, crawl.publ, crawl.year, crawl.forma, crawl.ids, crawl.desc, crawl.connect, crawl.lang, crawl.rvk, crawl.source,crawl.author2, crawl.publ2, crawl.year2, crawl.forma2, crawl.ids2, crawl.desc2, crawl.connect2, crawl.lang2, crawl.rvk2, crawl.source2]
function_place=[crawl.bib]
if __name__ == "__main__":
    base = "http://hu-berlin.hosted.exlibrisgroup.com/primo_library/libweb/action/"
    #key = raw_input("Keyword: ")
    key = "xml"
    request={'any':key}
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
            print "try no.1: "+ str(e)
            result_counter +=1
        try:
            place_link = base + result_tab.find(title="Bestand - "+ str(result_counter))['href']
        except Exception as e:
            print 'place link error'
        """
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
            docs.append(hit)
        except Exception as e:
            result_counter +=1
            print str(e)
        """
        try:
            req = ul.urlopen(place_link).read()
            while 'Was ist neu' in req:
                req = ul.urlopen(place_link).read()
            d_target =Bsoup(req, 'lxml')
            #print d_target
            for func in function_place:
                try:
                    func(d_target, hit)
                except:
                    pass
            result_counter +=1
            docs.append(hit)
        except Exception as e:
            result_counter +=1
            print str(e)
        print hit
