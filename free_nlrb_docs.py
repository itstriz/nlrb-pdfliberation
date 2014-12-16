import feedparser
import os
import urllib2

def get_pdf_file(url, output_file):
    response = urllib2.urlopen(url)
    html = response.read()

    temp_pdf_file = open(output_file, 'wb')
    temp_pdf_file.write(html)
    temp_pdf_file.close()

def extract_from_template(data_file):
    """ Extract from template """
    # Open file
    nlrb_doc = open(data_file, 'r')
    first_line = nlrb_doc.readline()

    # Template 1
    if first_line[0:6] == 'UNITED':
        return "Template found for" + data_file
    else:
        return "No Template Found for " + data_file
    
print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')

print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']

foo = 1
for entry in board_decisions_entries:
    doc_url = entry['links'][0]['href']
    file_name = 'sample' + str(foo) + '.pdf'
    txt_name = 'sample' + str(foo) + '.txt'
    print "Getting " + doc_url
    get_pdf_file(doc_url, file_name)
    print "Converting " + file_name + " to text"
    os.system('pdf2txt.py ' + file_name + ' > ' + txt_name)
    print "Checking for template: " + extract_from_template(txt_name)
    foo = foo + 1


