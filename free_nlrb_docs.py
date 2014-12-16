import feedparser
import os
import urllib2

def get_pdf_file(url, output_file):
    response = urllib2.urlopen(url)
    html = response.read()

    temp_pdf_file = open(output_file, 'wb')
    temp_pdf_file.write(html)
    temp_pdf_file.close()

print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')

print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']

print "\nFirst Document URL:"
board_decision_doc = board_decisions_entries[0]['links'][0]['href']
print board_decision_doc

foo = 1
for entry in board_decisions_entries:
    get_pdf_file(entry['links'][0]['href'], 'sample' + str(foo) + '.pdf')
    os.system('pdf2txt.py sample' + str(foo) + '.pdf > sample' + str(foo) + '.txt')
    foo = foo + 1


