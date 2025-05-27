# Utility functions for the HTTP server
def get_404_page():
    f = open('page404.html', 'r')
    page = f.read()
    f.close()
    return page
