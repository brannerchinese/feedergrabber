#!/usr/bin/env python3
# feedergrabber.py
# 20130420
# David Prager Branner

import re
import urllib.request
import urllib.error
import urllib.parse
import bs4
import feedparser
import time
import datetime

http_pattern = re.compile('^https?://')
reference_pattern = re.compile('^#')
illformed_slash_pattern = re.compile('/\.*(\.|/)+/*')

def retrieve_file_contents(url):
    try:
        file_contents = feedparser.parse(url) 
        errors = None
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        # For later: do logging and report at end, along with domain affected
        errors.append([url, e])
        file_contents = None
    return file_contents, errors

def parse_domain(url):
    '''Divide a URL into its three principal parts. Test with no slash at all, multiple slashes. Slashes within remainder should *not* be removed.
    '''
    ParseResult = urllib.parse.urlparse(url)
    return ParseResult.scheme, ParseResult.netloc, ParseResult.path

def add_domain_to_any_relative_URI(scheme, domain, link, title,
            post_links_and_titles):
    '''If link begins with anything other than http://, https://, or #, add http:// to it.  Test with http and #, perh also http:// and https, all at start of string. Perhaps also with these not at start?
    '''
    if not ((re.search(http_pattern, str(link)) or
            re.search(reference_pattern, str(link)))):
        link = re.sub('^', scheme+'://'+domain+'/', str(link))
    if not title:
        title = 'No title found.'
    post_links_and_titles.append((link, title))
    return post_links_and_titles

def postprocess(link):
    '''Ensures that there is no combination of . or /
    following the initial :// . Test using a range of //, /./, /.../., etc.  '''
    scheme_name, domain, remainder = parse_domain(link)
    remainder = re.sub(illformed_slash_pattern, '/', remainder)
    return scheme_name + '://' + domain + remainder

def check_wellformed(url):
    # ggg this still needs to be written)
    # ggg Should look at urllib.parse.urlparse before proceeding.
    # remove any spaces
    url = url.replace(' ', '')
    # make all lower case
    url = url.lower()
    # fix "htp"
    # if no scheme name at start, place one at start
    # if ill-formed delimiter (:/ or //), replace
    # if no ://, then check for http or http at start and place delimiter next
    #
    return url

def feedergrabber(url=None, select_strings=None):
    if not url:
        return None, ['Empty URL.']
    url = check_wellformed(url) # ggg should we include parse_domain here?
    scheme, domain, path = parse_domain(url)
    if not (scheme and domain):
        return None, ['URL malformed: ' + scheme + domain + path]
    # Initialize some variables
    errors = []
    file_contents = ''
    post_links_and_titles = []
    post_date = ''
    # Get file contents
    file_contents, _ = retrieve_file_contents(url)
    # Gather links, titles, and dates
    for i in file_contents.entries:
        try:
            link = i.link
        except AttributeError as e:
            errors.append([url + 
                    ': A link was unexpectedly not returned by feedparse.'])
            continue
        link = postprocess(link)
        if i.updated_parsed:
            post_date = i.updated_parsed
        elif i.published_parsed:
            post_date = i.published_parsed
        if post_date:
            post_date = datetime.datetime.fromtimestamp(time.mktime(post_date))
        else:
            post_date = datetime.datetime.now()
        post_links_and_titles.append((link, i.title, post_date))
    if not post_links_and_titles:
        post_links_and_titles = None
        errors.append(url + ': Parsing methods not successful.')
    return post_links_and_titles, errors
