#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

import PyPDF2
# TODO: Request input for the type of approach I want (VOR, NDB, ILS, RNAV)
# TODO: Crawl the directory structure to look for signature patterns associated with the respective approaches (e.g. NDB has only one letter -- an N -- in the name; all other characters are numbers)
pdfFileObj = open('/Users/brwarn/Documents/Aviation/IAP/DDTPPD_201703/06598N34.PDF', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
pdftext = pageObj.extractText()
print(pdftext)
pdfFileObj.close()
# TODO: Present the candidate files, approach type, and name (or ICAO identifier if the name can't easily be determined.
# TODO: User selects the (menu choice) number for the desired approach.  Open the approach plate