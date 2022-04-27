#!/usr/bin/python

# Author:   Jacky Sze

import json
import sys
import getopt
from PyPDF2 import PdfFileReader, PdfFileWriter


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, 'i:o:p:', ['input=', 'output=', 'pages='])
    except getopt.GetoptError as err:
        print(err)
        print('pdf-splitter.py -i <input-file> -o <output-file> -p <page-number-array>')
        sys.exit(-9000)

    input_file = None
    output_file = None
    page_numbers = None
    for opt, arg in opts:
        if opt in ('-i', '--input'):
            input_file = arg
        elif opt in ('-o', '--output'):
            output_file = arg
        elif opt in ('-p', '--pages'):
            page_numbers = json.loads(arg)
            if not isinstance(page_numbers, list):
                print(
                    'error: JSON array is expected in the page number command line argument')
                sys.exit(-9001)

    pdf = PdfFileReader(input_file)
    pdf_writer = PdfFileWriter()
    for page_number in page_numbers:
        # zero based page index
        page_index = page_number - 1
        pdf_writer.addPage(pdf.getPage(page_index))
    with open(output_file, 'wb') as file:
        pdf_writer.write(file)
        file.close()


if __name__ == '__main__':
    main(sys.argv[1:])
