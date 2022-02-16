from types import NoneType
from urllib.parse import quote

class URIs:
    baseurl = 'https://1lib.in/'
    search = baseurl + 's/'
    download = baseurl + 'dl/'
    book = baseurl + 'book/'
    reader = baseurl + 'reader/'
    
    def search_url(self, query):
        return self.search + quote(query)
    
    def book_url(self, id1, id2):
        # I havent figured out what each id1 and id2 represent. but both seem to be unique for each book
        return self.book + id1 + '/' + id2 + '/'
    
    def download_url(self, id1, id2):
        return self.download + id1 + '/' + id2 + '/'
    
def cleanup_dict(dict_):
    return {k: cleanup_value(v) for k, v in dict_.items()}

def cleanup_value(val):
    if isinstance(val, str):
        out = val.replace('\n', '').replace('\r', '').strip()
    elif isinstance(val, list):
        out = [cleanup_value(v) for v in val]
    elif isinstance(val, dict):
        out = cleanup_dict(val)
    else: 
        out = val
        
    if isconvertable(int, out):
        out = int(out)

    if isconvertable(float, out):
        out = float(out)
        
    return out

def isconvertable(type_, val):
    if isinstance(val, (dict, NoneType)):
        return False
    try:
        type_(val)
        return True
    except ValueError:
        return False