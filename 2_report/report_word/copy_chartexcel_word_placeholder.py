import win32com.client as win32

def copy_chart_from_excel(excel_file, sheet_name, chart_name):
    # Open Excel and the specified workbook
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False  # Set to True for debugging

    wb = excel.Workbooks.Open(excel_file)
    ws = wb.Sheets(sheet_name)
    
    # Ensure the chart object exists and select it
    chart = ws.ChartObjects(chart_name)
    chart.Select()
    
    # Copy the chart to the clipboard
    excel.Selection.Copy()
    
    # Close the workbook and quit Excel
    wb.Close(SaveChanges=False)
    excel.Quit()

def paste_chart_into_word(word_file, placeholder):
    # Open Word and the specified document
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False  # Set to True for debugging
    
    doc = word.Documents.Open(word_file)
    
    # Replace placeholder with chart
    for para in doc.Paragraphs:
        if placeholder in para.Range.Text:
            # Remove placeholder text
            para.Range.Text = para.Range.Text.replace(placeholder, '')
            # Paste the chart from clipboard
            para.Range.Paste()  # This pastes the chart as an embedded object
            break  # Assuming there is only one placeholder of this type
    
    # # Replace placeholders in tables
    # for table in doc.Tables:
    #     for row in table.Rows:
    #         for cell in row.Cells:
    #             for para in cell.Paragraphs:
    #                 if placeholder in para.Range.Text:
    #                     # Remove placeholder text
    #                     para.Range.Text = para.Range.Text.replace(placeholder, '')
    #                     # Paste the chart from clipboard
    #                     para.Range.Paste()  # This pastes the chart as an embedded object
    #                     break  # Assuming there is only one placeholder of this type
    
    # Save and close the document
    doc.SaveAs(word_file.replace('.docx', '_with_chart.docx'))
    doc.Close(SaveChanges=True)
    word.Quit()

# Define paths and parameters
excel_file = r"D:\economics\repo_later\python_test2408\report_word\chart.xlsx"
sheet_name = 'Sheet1'  # Change to your sheet name
chart_name = 'Chart 1'  # Change to your chart name
word_file = r"D:\economics\repo_later\python_test2408\report_word\report.docx"
placeholder = '{{Figure1}}'

# Copy the chart from Excel
copy_chart_from_excel(excel_file, sheet_name, chart_name)

# Paste the chart into the Word document
paste_chart_into_word(word_file, placeholder)
