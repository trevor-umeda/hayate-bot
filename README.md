hayate-bot
==========

This project is built on the open source skype bot project here. [sevabot](https://github.com/opensourcehacker/sevabot).
The only work i've done is added scripts and modified the command handler to better fit my needs. 


Hayate bot mainly works through receiving commands and contacting external services for appropriate responses. This allows work to be done on a function without having to do maintenance on the bot itself. Parsing command parameters or adding new paramters is done through modifying or adding scripts to the bot.



*** List of fetaures 

* Image response - Hayate will parse the typed sentence and respond with an appropriately tagged image.
* Youtube search - will search youtube. Done by using the serveme command.
* Link save - Hayate will save links posted in the chat. 
* Question answer - Hayate will answer questions. The question and answers are prepared before hand atm.

** The main changes to the bot itself ( not scripts or external services)

* You may activate commands via !command or hayate command. 
* Parsing of the sentence to find links
* Parsing of the sentence to find picture tags.



