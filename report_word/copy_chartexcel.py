# pip install pywin32


import win32com.client as win32

# Open Excel and Word
excel = win32.gencache.EnsureDispatch('Excel.Application')
word = win32.gencache.EnsureDispatch('Word.Application')

# Make Excel and Word visible (optional)
excel.Visible = False
word.Visible = False

dir = 'report_word/'

# Open the Excel workbook and select the worksheet
wb = excel.Workbooks.Open(r'D:\economics\repo_later\python_test2408\report_word\chart.xlsx')
ws = wb.Sheets('Sheet1')  # Change to your sheet name

# Copy the chart
chart = ws.ChartObjects('Chart 1')  # Change to your chart name
chart.Select()  # Select the chart
chart.Chart.ChartArea.Select()  # Select the chart area to ensure it is properly selected

# Copy the chart as an Excel object
excel.Selection.Copy() 

# Open a new Word document
doc = word.Documents.Add()

# Paste the chart into the Word document
selection = word.Selection
selection.Paste() 
# Save the Word document
doc.SaveAs(r'D:\economics\repo_later\python_test2408\report_word\chart.docx')

# Close the documents and applications
doc.Close()
wb.Close()
excel.Quit()
word.Quit()
