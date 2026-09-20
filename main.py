import csv
import pdfplumber

with pdfplumber.open("bdo.pdf") as pdf:

    page = pdf.pages[0]
    page_height = page.height
    page_width = page.width

    bbox = (0,272, page_width, 740)
    img = page.to_image()
    img.draw_rect(bbox)
    img.save("debug_crop.png")

    cropped_page = page.crop(bbox)

    table = cropped_page.extract_table({
        "vertical_strategy": "text",
        "horizontal_strategy": "text",
    })

    clean_table = []
    for row in table:
        if any(cell.strip() for cell in row if cell):
            clean_table.append(row)

    final_table = []
    for row in clean_table:
        description = " ".join(row[1:4]).strip()

        col4 = row[4].lstrip('P')
        col5 = row[5].lstrip('P')
        col6 = row[6].lstrip('P')

        new_row = [row[0], description, col4, col5, col6]
        final_table.append(new_row)

    for i, r in enumerate(final_table, start=1):
        print(f"{i}: {r}")

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(final_table)
