import feedparser
import re
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
    doc_lines = nlrb_doc.readlines()
    doc_text = ''.join(doc_lines)
    # Template 1
    if doc_lines[0][0:6] == 'UNITED':
        print "Template found. Parsing data..."
        case_no = find_case_no(doc_text)

        return_data =   {   'location'      : doc_lines[4].strip(),
                            'employer'      : doc_lines[6].strip(),
                            'petitioner'    : doc_lines[12].strip(),
                            'case_no'       : case_no,
                        }

        return return_data        
    else:
        return "No Template Found for " + data_file

def find_case_no(doc_text):
    case_num = re.findall('[0-9]{2}-[A-z]{2}-[0-9]{6}', doc_text)
    case_nums = []
    for num in case_num:
        case_nums.append(num)

    return case_nums

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
        print "Checking for template:"
        print extract_from_template(txt_name)
        foo = foo + 1
    
print "Grabbing NLRB Decisions Feed..."
board_decisions_feed = feedparser.parse('http://www.nlrb.gov/rss/rssBoardDecisions.xml')

print "\nParsing Entries..."
board_decisions_entries = board_decisions_feed['entries']

#print "Testing sample1.txt"
#print extract_from_template('sample1.txt')
get_all_samples(board_decisions_entries)
