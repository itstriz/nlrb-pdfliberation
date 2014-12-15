import feedparser

print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')
print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']
print "\nFirst Document URL:"
print board_decisions_entries[0]['links'][0]['href']
