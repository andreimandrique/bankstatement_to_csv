import pdfplumber

def process(file_name):
    
    # process the pdf
    with pdfplumber.open(file_name) as pdf:
        
        # 1st page
        page = pdf.pages[0]

        page_height = page.height
        page_width = page.width

        bbox = (0,272, page_width, 740)
        cropped_page = page.crop(bbox)