#!/usr/bin/python
import feedparser

NewsFeed = feedparser.parse("https://advisories.ncsc.nl/rss/advisories")

entry = NewsFeed.entries[1]

print entry.published
print "******"
print entry.summary
print "------News Link--------"
print entry.link