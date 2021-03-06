# -*- coding: utf-8 -*-

"""
Handler class for processing built-in commands and delegating messages.
"""
from __future__ import absolute_import, division, unicode_literals

import re
import logging
import shlex
import json
import urllib
from inspect import getmembers, ismethod
from random import randint

from sevabot.bot import modules
from sevabot.utils import ensure_unicode

logger = logging.getLogger('sevabot')


class CommandHandler:
    """A handler for processing built-in commands and delegating messages to reloadable modules.
    """

    def __init__(self, sevabot):
        self.sevabot = sevabot
        self.calls = {}
        request = urllib.urlopen('http://vast-castle-1062.herokuapp.com/tags')
        self.tagWords = json.loads(request.read())  
        self.cache_builtins()

    def cache_builtins(self):
        """Scan all built-in commands defined in this handler.
        """

        def wanted(member):
            return ismethod(member) and member.__name__.startswith('builtin_')

        self.builtins = {}
        for member in getmembers(self, wanted):
            command_name = re.split('^builtin_', member[0])[1]
            self.builtins[command_name] = member[1]
            logger.info('Built-in command {} is available.'.format(command_name))

    def handle(self, msg, status):
        """Handle command messages.
        """

        # If you are talking to yourself when testing
        # Ignore non-sent messages (you get both SENDING and SENT events)
        if status == "SENDING" or status == "SENT":
            return

        # Some Skype clients (iPad?)
        # double reply to the chat messages with some sort of ACK by
        # echoing them back
        # and we need to ignore them as they are not real chat messages
        # and not even displayed in chat UI
        if status == "READ":
            return

        # Check all stateful handlers
        for handler in modules.get_message_handlers():
            processed = handler(msg, status)
            if processed:
                # Handler processed the message
                return

        # We need utf-8 for shlex
        body = ensure_unicode(msg.Body).encode('utf-8')

        logger.debug(u"Processing message, body %s" % msg.Body)

        # shlex dies on unicode on OSX with null bytes all over the string
        try:
            words = shlex.split(body, comments=False, posix=True)
        except ValueError:
            # ValueError: No closing quotation
            return

        words = [word.decode('utf-8') for word in words]
        endWord = words[-1]
        wordsLength = len(body)
	
	#Check to see if the words contain a link. if so find the word that has it and save it
        if (('http://' in body) or ('https://' in body)):  
            for word in words:
                if "http://" in word:
                    command_name = "linkCafe"
                    command_args = [word,msg.FromDisplayName]
                    self.run_commands(command_name,command_args,msg,status,'false')    
                    return 

        if len(words) < 1:
            return

        command_name = words[0]
        command_args = words[1:]

        # Beyond this point we process script commands only
        if (command_name.startswith('!') or command_name == 'hayate'):            
            if command_name == 'hayate':
                command_name = words[1]
                command_args = words[2:]
            else: 
                command_name = command_name[1:]

            self.run_commands(command_name,command_args,msg,status,'true')            
        elif (body in self.tagWords):
            command_name = "omu"
            command_args = [body.replace (" ", "%20")]
            self.run_commands(command_name,command_args,msg,status,'true')    
            return  
        elif len(words) <= 7 :            
            for word in self.tagWords:
                if (body.find(word) >= 0 and ((len(words)==1 and (word in words)) or ( len(words) > 1 and (body.find(word+" ")==0) or (" "+word+" " in body) or (body.find(" "+word)==(wordsLength-len(word)-1))))):                        
                    command_name = "omu"
                    command_args = [word.replace (" ", "%20")]
                    self.run_commands(command_name,command_args,msg,status,'true')    

                    return                    

    def builtin_reload(self, args, msg, status):
        """Reload command modules.
        """
        request = urllib.urlopen('http://vast-castle-1062.herokuapp.com/tags')
        self.tagWords = json.loads(request.read())  

        commands = modules.load_modules(self.sevabot)
        msg.Chat.SendMessage('I feel refreshed! Awaiting your command.')

    def run_commands(self,command_name,command_args,msg,status,output_enabled):
        script_module = modules.get_script_module(command_name)
        if command_name in self.builtins:
            # Execute a built-in command
            logger.debug('Executing built-in command {}: {}'.format(command_name, command_args))
            self.builtins[command_name](command_args, msg, status)
        elif script_module:
	    if output_enabled == 'true':	
                # Execute a module asynchronously
                def callback(output):
                    msg.Chat.SendMessage(output)
            else:
                def callback(output):
                    someVar = 'whatevs'
            
            script_module.run(msg, command_args, callback)
        else:
            phrases = ["I don't think I understand what you are asking for...","Is there a typo in that command? I don't know what you want. ","I didn't watch the show, i don't know what that means."]
            phrasenum = randint(0,2)
            msg.Chat.SendMessage(phrases[phrasenum])    
    
