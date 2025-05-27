# Utility functions for the HTTP server

import time

'''
It provides the 404 page from the file 'page404.html'.
'''
def get_404_page():
    f = open('page404.html', 'r')
    page = f.read()
    f.close()
    return page

'''
It prints the message on console and writes it into the file 'log/server.log'.
'''
def print_and_log(message):
    print(message)
    with open('log/server.log', 'a') as log:
        log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': ')
        log.write(message + '\r\n')
