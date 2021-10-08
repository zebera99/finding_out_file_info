import os
import datetime

filenames = ['service_contract.hwp', 'christmas_report.pptx',
             'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']    #assuming there are those files in same directory

for filename in filenames:
    mtimestamp = os.path.getmtime(filename)
    mtime = datetime.datetime.fromtimestamp(mtimestamp)
    size = os.path.getsize(filename)
    file_info = {}
    file_info["filename"] = filename
    file_info["mtime"] = str(mtime)
    file_info["size"] = size

    print(file_info)
