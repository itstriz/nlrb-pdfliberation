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
    doc_lines = []
    for i, line in enumerate(nlrb_doc):
        doc_lines.append(line)

    # Template 1
    if doc_lines[0][0:6] == 'UNITED':
        print "Template found. Parsing data..."
        return_data =   {   'location'      : doc_lines[4].strip(),
                            'employer'      : doc_lines[6].strip(),
                            'petitioner'    : doc_lines[12].strip(),
                            'case_no'       : doc_lines[16][5:].strip(),
                        }

        return return_data        
    else:
        return "No Template Found for " + data_file

def get_all_samples(board_decisions_entries):
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
    
print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')

print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']

print "Testing sample1.txt"
print extract_from_template('sample1.txt')
