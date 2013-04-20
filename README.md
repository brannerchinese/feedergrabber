feedergrabber
==============

Retrieves the links and titles of recent posts from blog feeds.

Version
------
0.2, 20130420 (initial commit; previous version was as bloggergrabber v. 0.1)

Set-up
------

1. Note the existence of `requirements.txt` files. 
2. There are versions for Python v. 2.7 (contain "27" in the file names) and for Python 3 (no special notations). They are in separate PYTHON27 and PYTHON3 directories.
3. The main program is `feedergrabber.py` and its main function is `feedergrabber()`, which takes a single URL as an argument. The URL should point to an RSS or Atom feed; it normally returns an error if it encounters ordinary HTML or non-well-formed XML.

Output
------
1. File `feedergrabber.py` returns a 3-tuple containing two lists and a `datetime.datetime` object:
 * a first list of 2-tuples, each containing the URL and title of a single post; this tuple may be `None` if something went wrong with the look-up or parsing.
 * a second list of 2-tuples, each containing the URL and error message associated with an error encountered; if this tuple is `None`, no errors were observed.
 * a `datetime.datetime` object containing the date of either publication or updating, preferring the latter if possible, of the post.
1. A supplementary program is `supply_feedergrabber.py`, which runs through a list of known feeds and non-feed blogs, calling `feedergrabber` for each, and reporting a period (.) if the look-up and parsing proceeded smoothly. Since non-feed sources are no longer supported, they will return an error, "Parsing methods not successful."

New in this version
-------------------
The initial prototype of this module used Beautiful Soup 4 to scrape both feeds and ordinary HTML. Here, however, support for HTML blogs is discontinued, in order to eliminate the need for manual configuration of the scraping process for each new blog and to speed the parsing process.

Future work
------------
1. Unit testing. 
1. Error-logging.
1. Doc-strings not yet written for the most part.
1. Systematize error codes.
2. Is it possible to subscribe to a feed using a socket, so that there is no need to process anything more than once or wait for HTTP requests to be answered?

[end]
