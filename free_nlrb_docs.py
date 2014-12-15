import feedparser
import os
import urllib2

def get_pdf_file(url):
    response = urllib2.urlopen(url)
    html = response.read()

    temp_pdf_file = open('temp.pdf', 'wb')
    temp_pdf_file.write(html)
    temp_pdf_file.close()

print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')

print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']

print "\nFirst Document URL:"
board_decision_doc = board_decisions_entries[0]['links'][0]['href']
print board_decision_doc

print "\nDownloading file..."
print get_pdf_file(board_decision_doc)

print "File downloaded as temp.pdf"
os.system('pdf2txt.py temp.pdf')
