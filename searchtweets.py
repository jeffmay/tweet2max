#!/usr/bin/env python

import tweepy

# VIEWS #

def main(args):
    import argparse
    parser = argparse.ArgumentParser(
        description="Print a list of tweets from a twitter search.")
    parser.add_argument('query', nargs='+', help='the twitter search query.')
    parser.add_argument('-l', type=int, nargs='?', default=10, dest='limit')
    opts = parser.parse_args(args)
    searchtweets(' '.join(opts.query), limit=opts.limit)

def searchtweets(query, limit=None):
    print(query)
    # Just hangs on this line...
    tweepy.search(q=query)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
