# Name
Spok_Pager is a python library that takes advantage of the spok paging api to send messages to spok pagers.

# Synopsis
The library can be used from shell/cmd or imported as a library.

## Use from command line

`python3 Pager.py [pager number] [pager message]`

## Import Pager as a library
If pager.py is imported, the pager class can be used.

### init
When the pager class is instantiated, it takes one argument, the pager number as a string.

`p = pager.pager('5551234567')`

### send_page
The send page method takes one argument, the message to be sent as a string.

`p.send_page('Test Message')`
