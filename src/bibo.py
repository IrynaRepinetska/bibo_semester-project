#!/usr/bin/python2
# coding: utf8
import aiml
import sys
import url
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def finder(request): 
    result_list = url.crawler(request)
    global a
    global limitb
    global count
    global leihe
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
            print('Autor: ' + book.get('creator', 'Nicht vorhanden!')+ '\n')
            print('Inhalt: ' + book.get('desc', 'Nicht vorhanden!')+ '\n')
            print('Sprache: ' + book.get('lang', 'Nicht vorhanden!')+ '\n')
            print('Veröffentlichung: ' + book.get('year', 'Nicht vorhanden!')+ '\n')
            print('Status: ' + book.get('shelf','Nicht vorhanden!')+ '\n')
            print('---------------------------------------------------------------------------'+ '\n')

def print_leihe(book_list):
    if len(book_list) != 0:
        for book in book_list:
            print('---------------------------------------------------------------------------\n')
            print('Titel: ' + book.get('title', 'Nicht vorhanden!')+ '\n')
            print('Autor: ' + book.get('author', 'Nicht vorhanden!')+ '\n')
            print('Inhalt: ' + book.get('desc', 'Nicht vorhanden!')+ '\n')
            print('Sprache: ' + book.get('lang', 'Nicht vorhanden!')+ '\n')
            print('Veröffentlichung: ' + book.get('year', 'Nicht vorhanden!')+ '\n')
            print('Status: ' + book.get('shelf','Nicht vorhanden!')+ '\n')
            print('---------------------------------------------------------------------------'+ '\n')

def email_string(book_list):
    email = u""
    if len(book_list) != 0:
        for book in book_list:
            email+= '------------------------------------------------------------------------\n'
            email+='Titel: ' + book.get('title', 'Nicht vorhanden!')+ '\n'
            email+='Autor: ' + book.get('author', 'Nicht vorhanden!')+ '\n'
            email+='Inhalt: ' + book.get('desc', 'Nicht vorhanden!')+ '\n'
            email+='Sprache: ' + book.get('lang', 'Nicht vorhanden!')+ '\n'
            email+='Veröffentlichung: '.decode('utf-8') + book.get('year', 'Nicht vorhanden!')+ '\n'
            email+='Status: ' + book.get('shelf','Nicht vorhanden!')+ '\n'
            email+='------------------------------------------------------------------------'+ '\n'
    return email

mybot = aiml.Kernel()
mybot.learn("std-startup.xml")
mybot.respond("load aiml bibo")
bot_response_before = ""

print("You have started a program called Bibo. Bibo can be your best helper in finding literature in the HU library. If you want to stop talking to Bibo, just type QUIT. Enjoy!" + '\n')

message = "start"
bot_response = mybot.respond(message)
print(bot_response)

while True:
    message = raw_input("Enter your message to Bibo: ")
    if message == "quit":
        exit()
    else:
        if bot_response_before == "Could you type me your email adress?" or bot_response_before == "Alright, in order to do this I need to know your email adress." or bot_response_before == "Give me please your email adress.":

            email = message
            message = "move"
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

#the end of the conversation
        if bot_response == "theend":
            message = "end"
            bot_response = mybot.respond(message)
            print(bot_response + '\n')
            exit()
#email abfragen and die liste per email verschicken
#        if bot_response == "email":
        if bot_response_before == "Could you type me your email adress?" or bot_response_before == "Alright,     in order to do this I need to know your email adress." or bot_response_before == "Give me please your email     adress.":
            message = "give email"
            bot_response = mybot.respond(message)
            email = bot_response
#in the variable email is saved an email adress of a user.. here should the list of books be sent to an email
            fromaddr = "bibothefriendliest@gmail.com"
            toaddr = 'ch.roeseler@gmail.com'#str(email)
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Your Book List"

            body = email_string(leihe)
            msg.attach(MIMEText(body.encode('utf-8'), 'plain'))

            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromaddr, "cpxzmzkehjfovuwu")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            message = "move"
            bot_response = mybot.respond(message)

#title directly
        if bot_response == "title":
            message = "get title"
            title= mybot.respond(message)
            req = {'title': title}
            message = "next step"
            bot_response = mybot.respond(message)


        print(bot_response)

#title	
        if bot_response_before == "Ok, in order to find it, I need to know its name." or bot_response_before == "In this case, I will check if we have it. Tell me please its name." or bot_response_before == "Great! I will find it for you in no time. But I need to know the name of the book.":
            title = message
            req = {'title': title}
#author
        if bot_response_before == "If you know the author of the book, please share it with me. Otherwise, just type NO." or bot_response_before == "I also would like to know who the author of this book is. If you do not recall it, please type NO." or bot_response_before == "The author's name would be helpful as well. If you do not remember it, just say NO.":
            if message !="no" or message !="No" or message !="nO" or message !="NO":
                req['creator'] = message
#keyword
        if bot_response_before == "Ok, a simple keyword describing a book would be enough!" or bot_response_before == "In this case, tell me just a keyword related to a book." or bot_response_before == "Alright, what does this book should be about?":
            keyword = message
            req = {'any': keyword}

#co-author
        if bot_response_before == "Now tell me, who the co-author actually is.":
            coauthor = message
            req['coauthor'] = coauthor

#publisher
        if bot_response_before == "Alright, type me now a name of a publisher please.":
            publisher = message
            req['lsr48'] = publisher


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
        if bot_response == "Guess what! I have already found information for you:" or bot_response == "I have already found something for you:" or bot_response == "Alright, this is what I have found for you:" or bot_response == "I have already found an answer on you query!" or bot_response == "The result of your search is:" or bot_response == "Guess what! I have already found something for you:" or bot_response == "This is everything that I have found for you based on the keyword you have provided:" or bot_response == "Smartie, there is a list of the literature that may interest you based on the keyword you have given:" or bot_response == "I have found the following books that are related to your keyword:":
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
        if bot_response == "Here it goes:" or bot_response == "As you asked:":
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


#books to borrow are printed out

        if bot_response== "I would like to give you the literature you have chosen from the list:" or bot_response== "This is the list of the books you would like to borrow with detailed information:":
            if thing:
                leihe = result
            print_leihe(leihe)
            message = "move"
            bot_response = mybot.respond(message)
            print(bot_response+ '\n')
#the list with the choosen books to print..numbers should be collected in three if statements above
                                   
        bot_response_before = bot_response
