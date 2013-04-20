#!/usr/bin/python3
# supply_feedergrabber.py
# 20130420
# David Prager Branner

import feedergrabber
import time
import sys

def try_url(url):
    try:
        result = feedergrabber.feedergrabber(url)
    except Exception as e:
        print(url, e)
        raise e
    if result[1]:
        print(result[1], '\n')
    elif not result[0]:
        print('\nEmpty result on {0} with error report:\n{1}.\n'.
                format(url, result[1]))
        sys.exit(0)
    else:
        print('.', end='')
        sys.stdout.flush()

def main():
    feeds = [
            'http://akaptur.github.io/atom.xml',
            'http://alliejon.es/blog/atom.xml',
            'http://antoviaque.org/blog/feed/',
            'http://blog.accursedware.com/atom',
            'http://blog.leahhanson.us/feeds/all.atom.xml',
            'http://blog.leocad.io/feed',
            'http://blog.sashalaundy.com/atom.xml',
            'http://brannerchinese.wordpress.com/feed/',
            'http://chuckha.com/atom.xml',
            'http://dave.is/atom',
            'http://davemckenna.tumblr.com/rss',
            'http://dev.theladders.com/atom.xml',
            'http://feeds.feedburner.com/JuliaLang',
            'http://feeds.feedburner.com/KristianKristensensBlog',
            'http://foobarmustache.tumblr.com/rss',
            'http://https417.blogspot.com/feeds/posts/default',
            'http://initbecca.wordpress.com/feed/',
            'http://jmsdnns.tumblr.com/rss',
            'http://maryrosecook.com/feed',
            'http://maxlikely.tumblr.com/rss',
            'http://netrabaha.tumblr.com/rss',
            'http://newsomc.github.io/rss',
            'http://rcjara.github.io/rss',
            'http://sidnicio.us/feed/',
            'http://thegoldenspot.blogspot.com/feeds/posts/default',
            'http://tks2103.tumblr.com/rss',
            'http://unschooled.org/atom',
            'http://www.daniellesucher.com/feed/',
            'http://www.thomasboyt.com/rss',
            'http://zachallaun.com/atom',
            'https://idea.popcount.org/rss.xml',
            'https://scott.mn/posts.atom',
            'http://syntacticsugar.github.io/atom.xml',
            'http://santialbo.com/atom.xml',
            'http://cs.mcgill.ca/~abeaul10/feed.xml',
            'http://galtman.com/?feed=rss2',
            'http://blog.studiogel.com/rss',
            'http://qqrs.github.com/atom.xml'
        ]
    print('\nNow beginning {} feeds.'.format(len(feeds)))
    start_time = time.time()
    for url in feeds:
        try_url(url)
    end_time = time.time()
    print('\nTime elapsed: {0:.0f} seconds for {1} URLs.'
            '\n\nNow beginning non-feeds.'.
            format(end_time-start_time, len(feeds)))
    nonfeeds = [
            ('http://blog.angiepanfil.com', [[
                '''div[class="post"] h3 a[href]''',
                '''div[class="post"] h3 a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ('http://blog.bn.ee', [['''div[id*="post-"] a''',
                '''div[id*="post-"] a''',
                lambda link:  link.get('href'),
                lambda title: title.get('title')]]),
            ('http://edgemon.org/blog/', [[
                '''div[class="blog-entry"] h4[class="title"] a[href]''',
                '''div[class="blog-entry"] h4[class="title"] a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ('http://jordanorelli.com/', [[
                '''a[class="permalink"]''',
                '''h2''',
                lambda link:  link.get('href'),
                lambda title: title.text]]),
            ('http://stoneg.github.io/archives.html', [[
                '''dd a[href]''',
                '''dd a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ('http://www.dustingetz.com/', [[
                '''dd a[href]''',
                '''dd a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ('http://www.userbound.com/blog/', [[
                '''li a[href]''',
                '''li a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ('http://julieswoope.com/archive.html', [[
                '''div[class="content"] li a[href]''',
                '''div[class="content"] li a[href]''',
                lambda link:  link.attrs.get('href'),
                lambda title: title.text]]),
            ]
    start_time = time.time()
    for data in nonfeeds:
        url = data[0]
        try_url(url)
    end_time = time.time()
    print('\nTime elapsed: {0:.0f} seconds for {1} URLs.\nDone.'.
            format(end_time-start_time, len(nonfeeds)))

if __name__ == '__main__':
    main()
