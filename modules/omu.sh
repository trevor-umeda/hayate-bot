#!/bin/sh
#
# Example shell script for sending a message into sevabot
#
# Give command line parameters [chat id] and [message].
# The message is md5 signed with a shared secret specified in settings.py
# Then we use curl do to the request to sevabot HTTP interface.
#
#

tag=$1
curl --silent "http://vast-castle-1062.herokuapp.com/image?tag=$tag"

