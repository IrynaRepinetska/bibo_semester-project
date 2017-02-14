import aiml
import os

mybot = aiml.Kernel()
mybot.learn("std-startup.xml")
mybot.respond("load aiml bibo")
bot_response_before = ""

while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
       exit()
    else:
        bot_response = mybot.respond(message)
        print bot_response

#title	
	if bot_response_before == "Great! I will find it for you in no time. But I need to know the name of the book.":
	   title = message
	   dict = {'title': title}

	if bot_response_before == "In this case, I will check if we have it. Tell me please its name.":
           title = message
	   dict = {'title': title}

	if bot_response_before == "Ok, in order to find it, I need to know its name.":
           title = message
	   dict = {'title': title}

#author
	if bot_response_before == "The author's name would be helpful as well. If you do not remember it, just say NO.":
		if message !="no":
		  if message !="No":
	            if message !="nO":
		       if message !="NO":
       		          author = message
		          dict['author'] = author

	if bot_response_before == "I also would like to know who the author of this book is. If you do not recall it, please type NO.":
		if message !="no":
		  if message !="No":
	            if message !="nO":
		       if message !="NO":
       		          author = message
		          dict['author'] = author

	if bot_response_before == "If you know the author of the book, please share it with me. Otherwise, just type NO.":
       		if message !="no":
		  if message !="No":
	            if message !="nO":
		       if message !="NO":
       		          author = message
		          dict['author'] = author

#keyword
	if bot_response_before == "Alright, what does this book should be about?":
       		keyword = message
		dict = {'keyword': keyword}


	if bot_response_before == "In this case, tell me just a keyword related to a book.":
       		keyword = message
		dict = {'keyword': keyword}

	if bot_response_before == "Ok, a simple keyword describing a book would be enough!":
       		keyword = message
		dict = {'keyword': keyword}


#co-author
	if bot_response_before == "Now tell me, who the co-author actually is.":
		         coauthor = message
		         dict['coauthor'] = coauthor

#publisher
	if bot_response_before == "Alright, type me now a name of a publisher please.":
		         publisher = message
		         dict['publisher'] = publisher


#year
        if bot_response_before == "So what year was the book published in?" :
		         year = message
		         dict['year'] = year

#isbn
        if bot_response_before == "Ok, What the actual ISBN of the book is?":
		        isbn = message
		        dict['isbn'] = isbn

#issn
	if bot_response_before == "Now tell me please the ISSN value of a book.":
		         issn = message
		         dict['issn'] = issn

#number
	if bot_response_before == "Now I would ask you to type an actual number of the book you are searching for.":
		         number = message
		         dict['number'] = number


#answers .. 
	if bot_response == "I have found the following books that are related to your keyword:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value
		
	if bot_response == "Smartie, there is a list of the literature that may interest you based on the keyword you have given:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value

	if bot_response == "This is everything that I have found for you based on the keyword you have provided:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value

	if bot_response == "Guess what! I have already found something for you:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		

	if bot_response == "The result of your search is:":
 		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value

	if bot_response == "I have already found an answer on you query!":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value

	if bot_response == "Alright, this is what I have found for you:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', valu

	if bot_response == "Kiddo, I have already found something for you:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', valu

	if bot_response == "Guess what! I have already found information for you:":
		pass
		message = "whatever"
		bot_response = mybot.respond(message)
		print bot_response
		for key, value in dict.iteritems():
    		     print key, '\t', value
		dict.clear()
		for key, value in dict.iteritems():
    		     print key, '\t', value


	bot_response_before = bot_response
