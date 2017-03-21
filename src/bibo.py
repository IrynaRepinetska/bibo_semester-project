#!/usr/bin/python2
# coding: utf8
import aiml
import sys
import url


def finder(request):
    result_list = url.crawler(request)
    print result_list
    """
    db = [{'title': 'Beginning XML','author': 'Joe Fawcett ; Liam Quin ; Danny Ayers','publisher': 'Indianapolis, Ind. : Wiley : Indianapolis, Ind. : Wiley','year': '2012','desc': 'Verantwortlichkeit: Joe Fawcett ; Liam R. E. Quin ; Danny Ayers ','lang': 'Englisch', 'shelf': 'ST 250 X70','status': 'Exemplar ist am Standort', 'location': 'ZwB Naturwissenschaften'},
            {'title': 'HTML : kompakt, komplett, kompetent','author': ' Alexandra Brodmüller-Schmitz; Alexandra Brodmüller- Schmitz','publisher': 'Muenchen : Markt+Technik-Verl. : Muenchen : Markt+Technik-Verl. ','year': '2002','desc': 'Verantwortlichkeit: Alexandra Brodmüller-Schmitz ','lang': 'Deutsch', 'shelf': 'ST 250 H85 B864','status':'Exemplar ist am Standort' , 'location': 'ZwB Naturwissenschaften'},
           {'title': 'CSS : das umfassende Handbuch','author':' Kai. Laborenz' ,'publisher': 'Bonn : Rheinwerk ','year': '2016','desc': 'Verantwortlichkeit: Kai Laborenz','lang': '', 'shelf': 'ST 250 H85 L123 C9(3)','status':'Exemplar ist am Standort '},
            {'title': 'Datenbanken  Praxis, Methode und mathematische Darstellung','author': 'Theo Lutz','publisher': 'Stuttgart [u.a.] : Science Research Assoc. : Stuttgart [u.a.] : Science Research Assoc. ','year': '1976','desc': 'Verantwortlichkeit: Theo Lutz','lang': 'Deutsch', 'shelf': '','status': ''},
            {'title': 'XML.com','author': '','publisher': 'San Francisco, Calif. : OReilly Network : San Francisco, Calif. ','year': '1994','desc': 'Online-Ressource','lang': 'Englisch', 'shelf': '','status': ''},
            {'title': 'XML : Schritt für Schritt. XML - step by step','author': 'Michael J. Young;Michael Young;Marc Young','publisher': 'Unterschleißheim : Microsoft Press : Unterschleißheim : Microsoft Press','year': '2002','desc':  'Verantwortlichkeit: Michael J. Young','lang': 'Deutsch', 'shelf': '','status': ''},
            {'title': '','author': '','publisher':'' ,'year':'' ,'desc':'' ,'lang': '', 'shelf':'' ,'status':'' }]
    """
    """
    result_list = []
    for key, value in request.iteritems():
        if key == 'any':
            for book in db:
                for db_value in book.values():
                    try:
                        if value.lower() in db_value.lower():
                            if book not in result_list:
                                result_list.append(book)
                    except:
                        pass
        else:
            for book in db:
                try:
                    if value.lower() in book[key].lower():
                        if book not in result_list:
                            result_list.append(book)
                except:
                    pass

    """
    global a
    global limitb
    global count
    global leihe
    global req
    global thing
    thing = False
    req={}
    a = len(result_list)
    limitb = 0
    count  = 1
    leihe=[]
    return result_list


def print_nice(book_list):
    if len(book_list) == 0:
        print('Wait....Oops, seems like nothing matches in our libary!'+ '\n')
    else:
        global a
        global limitb
        global count
        limita=limitb
        if a > 2:
            limitb += 2
            a     -= 2
        else:
            limitb += a
            a = 0
        for book in book_list[limita:limitb]:
            print(str(count)+'--------------------------------------------------------------------------\n')
            count += 1
            print('Titel: ' + book.get('title', 'Nicht vorhanden!')+ '\n')
            print('Autor: ' + book.get('author', 'Nicht vorhanden!')+ '\n')
            print('Inhalt: ' + book.get('desc', 'Nicht vorhanden!')+ '\n')
            print('Sprache: ' + book.get('lang', 'Nicht vorhanden!')+ '\n')
            print('Veröffentlichung: ' + book.get('year', 'Nicht vorhanden!')+ '\n')
            print('Status: ' + book.get('status', 'Nicht vorhanden!') + ' ' + book.get('location', 'Nicht Vorhanden!') + ' im Regal ' + book.get('shelf','Nicht vorhanden!')+ '\n')
            print('---------------------------------------------------------------------------'+ '\n')

def print_leihe(book_list):
    if len(book_list) != 0:
        for book in book_list:
            print(str(count)+'--------------------------------------------------------------------------\n')
            print('Titel: ' + book.get('title', 'Nicht vorhanden!')+ '\n')
            print('Autor: ' + book.get('author', 'Nicht vorhanden!')+ '\n')
            print('Inhalt: ' + book.get('desc', 'Nicht vorhanden!')+ '\n')
            print('Sprache: ' + book.get('lang', 'Nicht vorhanden!')+ '\n')
            print('Veröffentlichung: ' + book.get('year', 'Nicht vorhanden!')+ '\n')
            print('Status: ' + book.get('status', 'Nicht vorhanden!') + ' ' + book.get('location', 'Nicht Vorhanden!') + ' im Regal ' + book.get('shelf','Nicht vorhanden!')+ '\n')
            print('---------------------------------------------------------------------------'+ '\n')








mybot = aiml.Kernel()
mybot.learn("std-startup.xml")
mybot.respond("load aiml bibo")
bot_response_before = ""

message = "start"
bot_response = mybot.respond(message)
print(bot_response)

while True:
    message = raw_input("Enter your message to Bibo: ")
    if message == "quit":
       exit()
    else:
        bot_response = mybot.respond(message)

#number of the book to borrow are collected hier

        global leihe

        if bot_response== "check the list":
            list_of_books = [int(s) for s in message.split() if s.isdigit()]
            for b in list_of_books:
                if int(b) <=len(result):
                    if result[int(b)-1] not in leihe:
                       leihe.append(result[int(b)-1])
            if len(leihe) == 0:
                bot_response = mybot.respond('empty')
            else:
                bot_response = mybot.respond('not empty')


#title directly      
        if bot_response == "title":
            message = "get title"
            title= mybot.respond(message)
            req = {'title': title}
            message = "next step"
            bot_response = mybot.respond(message)


        print(bot_response)

#title	
        if bot_response_before == "Great! I will find it for you in no time. But I need to know the name of the book.":
            title = message
            req = {'title': title}

        if bot_response_before == "In this case, I will check if we have it. Tell me please its name.":
            title = message
            req = {'title': title}

        if bot_response_before == "Ok, in order to find it, I need to know its name.":
            title = message
            req = {'title': title}

#author
        if bot_response_before == "The author's name would be helpful as well. If you do not remember it, just say NO.":
            if message !="no":
                if message !="No":
                    if message !="nO":
                        if message !="NO":
                            author = message
                            req['author'] = author

        if bot_response_before == "I also would like to know who the author of this book is. If you do not recall it, please type NO.":
            if message !="no":
                if message !="No":
                    if message !="nO":
                        if message !="NO":
                            author = message
                            req['author'] = author

        if bot_response_before == "If you know the author of the book, please share it with me. Otherwise, just type NO.":
            if message !="no":
                if message !="No":
                    if message !="nO":
                        if message !="NO":
                            author = message
                            req['author'] = author
#keyword
        if bot_response_before == "Alright, what does this book should be about?":
            keyword = message
            req = {'any': keyword}


        if bot_response_before == "In this case, tell me just a keyword related to a book.":
            keyword = message
            req = {'any': keyword}

        if bot_response_before == "Ok, a simple keyword describing a book would be enough!":
            keyword = message
            req = {'any': keyword}


#co-author
        if bot_response_before == "Now tell me, who the co-author actually is.":
            coauthor = message
            req['coauthor'] = coauthor

#publisher
        if bot_response_before == "Alright, type me now a name of a publisher please.":
            publisher = message
            req['publisher'] = publisher


#year
        if bot_response_before == "So what year was the book published in?" :
            year = message
            req['year'] = year

#isbn
        if bot_response_before == "Ok, What the actual ISBN of the book is?":
            isbn = message
            req['isbn'] = isbn

#issn
        if bot_response_before == "Now tell me please the ISSN value of a book.":
            issn = message
            req['issn'] = issn

#number
        if bot_response_before == "Now I would ask you to type an actual number of the book you are searching for.":
            number = message
            req['number'] = number


#answers ..


# a != 0 bedeutet, dass es sinnvoll ist der Benuter zu fragen. ob er noch weitere Buecher in der Liste sehen moechte. dh weitere Buecher mueossen in der Liste anwesen sein
        global a
        global result
        if bot_response == "I have found the following books that are related to your keyword:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "Smartie, there is a list of the literature that may interest you based on the keyword you have given:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "This is everything that I have found for you based on the keyword you have provided:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "Guess what! I have already found something for you:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "The result of your search is:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "I have already found an answer on you query!":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "Alright, this is what I have found for you:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "I have already found something for you:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

        if bot_response == "Guess what! I have already found information for you:":
            result = finder(req)
            if a == 0:
                message = "end2"
            else:
                message = "notend"
            bot_response = mybot.respond(message)
            print_nice(result)
            print(bot_response+ '\n')
            req.clear()

#die liste weiter ausgeben
        if bot_response == "As you asked:":
            #hier liste auszugeben
            if a == 0:
                message2 = "Wait a second..I have showen you already all the books..Sorry, my mistake!"
                print(message2 + '\n')
                message = "end"
            else:
                message = "notend"
            print_nice(result)
            bot_response = mybot.respond(message)
            print(bot_response + '\n')

        if bot_response == "Here it goes:":
            #hier liste auszugeben
            if a == 0:
                message2 ="Ooh no..I have just noticed that I do not have any other literature for you. Excuse me, please. Today I am being slightly unconcentrated. I think I am getting old..!"
                print(message2 + '\n')
                message = "end"
            else:
                message = "notend"
            print_nice(result)
            bot_response = mybot.respond(message)
            print(bot_response + '\n')




#books to borrow are printed out

        if bot_response== "This is the list of the books you would like to borrow with detailed information:":
            if thing:
                leihe = result
            print_leihe(leihe)
            message = "move"
            bot_response = mybot.respond(message)
            print(bot_response+ '\n')

        if bot_response== "I would like to give you the literature you have chosen from the list:":
            if thing:
                leihe = result
            print_leihe(leihe)
            message = "move"
            bot_response = mybot.respond(message)
            print(bot_response+ '\n')

#the list with the choosen books to print..numbers should be collected in three if statements above
                                   
        bot_response_before = bot_response
