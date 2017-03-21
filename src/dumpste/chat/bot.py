import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

#sessionId = raw_input("Tell me yout unique session Id")
#sessionData = kernel.getSessionData(sessionId)


while True:
        message = raw_input("Enter your message to the bot: ")
        if message == "quit":
            print "Well, bye then."
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            print kernel.respond(message)
