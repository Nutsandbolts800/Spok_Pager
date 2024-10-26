# Name
Spok_Pager is a python library that takes advantage of the spok paging api to send messages to spok pagers.

# Synopsis
Pager.py [pager number] [pager message]

# Import Pager Class
If pager.py is imported, the pager class can be used.

### init
When the pager class is instantiated, it takes one argument, the pager number as a string.

`p = pager.pager('5551234567')`

### send_page
The send page method takes one argument, the message to be sent as a string.

`p.send_page('Test Message')`
