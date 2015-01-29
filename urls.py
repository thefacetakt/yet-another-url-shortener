DATA_FILE = "urls.txt"

DATA_ENCODING = "utf-8"

def load_urls():
    data_file =  open(DATA_FILE, 'r', encoding=DATA_ENCODING)
    return eval(data_file.read())

urls, reverse_urls = load_urls()

def add_url(url):
    url = str(url)
    if (not (url in urls)):
        print("url", url)
        shortened_url = str(urls['next_url'])
        urls['next_url'] += 1
        urls[url] = shortened_url
        reverse_urls[shortened_url] = url
        save_urls()
    return urls[url]

def get_url(id):
    return reverse_urls[str(id)]

def save_urls():
    data_file =  open(DATA_FILE, 'w', encoding=DATA_ENCODING)
    print(repr((urls, reverse_urls)), file=data_file)
    data_file.close()