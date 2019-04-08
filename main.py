# Description: Program to search PDFs for text
# Author: Ruben Krueger


import PyPDF2
import sys
import re

# Returns pdf object from a pdf found at path
def readpdf(path):
    f = open(path, 'rb')

    pdf_file = PyPDF2.PdfFileReader(f)
    return pdf_file


# Returns all occurrences of text between start and stop
# file_path  = file_path to search for pdf
# start= string literal to begin return value
# start = string literal to end return value
def search(file_path, start, stop):

    matches = []

    pdf_file = readpdf(file_path)

    for i in range(pdf_file.numPages):
        page = pdf_file.getPage(i)

        text = page.extractText()

        regex = re.escape(start) + r'.*' + re.escape(stop)

        match = re.findall(regex, text)

        if len(match) != 0:
            matches.append(match)

    return matches


# output all text data in the pdf at file_path to output_file
def dump(file_path, output_file):
    out = open(output_file, 'w+')

    pdf_file = readpdf(file_path)

    for i in range(pdf_file.numPages):
        page = pdf_file.getPage(i)
        out.write(page.extractText())


if __name__ == '__main__':

    if len(sys.argv) < 3:
        sys.exit("Error: less than 3 args provided")

    file_path = sys.argv[1]
    start = sys.argv[2]
    stop = sys.argv[3]

    matches = search(file_path, start, stop)

    for match in matches:
        print(match)











