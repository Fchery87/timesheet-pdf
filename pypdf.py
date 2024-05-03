import fitz  # PyMuPDF
from datetime import datetime, timedelta

# Get the current date
start_date = datetime.now()

# Number of dates to generate
num_dates = 7

# List to store the dates
dates = []

# Add the starting date
dates.append(start_date.strftime('%m-%d-%Y'))

# Generate the subsequent dates
for i in range(1, num_dates):
    next_date = start_date + timedelta(days=i)
    dates.append(next_date.strftime('%m-%d-%Y'))

print("Generated dates:", dates)

# Open the existing PDF file
pdf_path = 'pdftoupdate.pdf'
doc = fitz.open(pdf_path)

# Iterate through the pages of the PDF
for page_num in range(len(doc)):
    page = doc.load_page(page_num)

    # Define the dates as a list
    
    # Define initial y-coordinate for text insertion
    y_coordinate = 155 
    x_coordinate = 380 
    # Iterate throughthe dates and add them as text to the page
    for date in dates:
        # Insert the text
        annot = page.insert_text((x_coordinate, y_coordinate), date, fontsize=10, rotate = 270)  # Adjust fontsize as needed
  
        # Decrement y-coordinate for the next text insertion
        x_coordinate -= 24  # Adjust this value as needed

annot = page.insert_text((461, 220), dates[6], fontsize=15, rotate = 270)  # Adjust fontsize as needed
annot = page.insert_text((84, 635), dates[6], fontsize=10, rotate = 270)  # Adjust fontsize as needed
  


# Save the changes to a new PDF file
doc.save(f"{dates[6]} CDPAP CHERY KIMBERLY.pdf")
doc.close()