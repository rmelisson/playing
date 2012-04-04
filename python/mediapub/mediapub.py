from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar
from pdfminer.converter import PDFPageAggregator

# Open a PDF file.
fp = open('test.pdf', 'rb')
# # Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# # Create a PDF document object that stores the document structure.
doc = PDFDocument()
# # Connect the parser and document objects.
parser.set_document(doc)
doc.set_parser(parser)
# Supply the password for initialization.
# # (If no password is set, give an empty string.)
# doc.initialize(password)
# # Check if the document allows text extraction. If not, abort.
#if not doc.is_extractable:
#     raise PDFTextExtractionNotAllowed
#     # Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
#     # Create a PDF device object.
#device = PDFDevice(rsrcmgr)
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#     # Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
#     # Process each page contained in the document.
text_content = []
for page in doc.get_pages():
    interpreter.process_page(page)
    lt_objs = device.get_result()
    for lt_obj in lt_objs:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            #page_text = update_page_text_hash(page_text, lt_obj)
            print lt_obj.get_text()
            print "\n \n new =================="
