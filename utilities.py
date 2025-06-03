# Utility functions for the HTTP server
import time
import mimetypes as mt

'''
It provides the 404 page from the file 'page404.html'.
'''
def get_404_page():
    f = open('page404.html', 'r')
    page = f.read()
    f.close()
    return page

'''
It prints the message on console and writes it into the file 'server.log'.
'''
def print_and_log(message):
    print(message)
    with open('server.log', 'a') as log:
        log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': ')
        log.write(message + '\n')

'''
It uses the mimetypes library to determine the MIME type of a file based on its extension.
If the MIME type cannot be determined, it returns 'application/octet-stream', which is the default type for binary files.
'''
def get_mime_type(file_path):
    print_and_log("Determining MIME type for file: " + file_path)
    mime_type, _ = mt.guess_type(file_path)
    return mime_type if mime_type else 'application/octet-stream'
