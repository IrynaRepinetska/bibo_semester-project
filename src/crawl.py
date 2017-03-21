#!/usr/bin/python2
# coding: utf8
def title(target, hit):
    hit['title']    = target.find("h1",{"class":"EXLResultTitle"}).contents[0]
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

def bib(target, hit):
    li = target.find_all("li", {"class":"width60"})
    span = li[0].find_all('span')
    hit['shelf']    = span[1].contents[0] + " " + span[0].contents[0]
    hit['shelf']    = hit['shelf'].strip('\t\n').replace(u"\xa0","")
