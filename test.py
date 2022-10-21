from urllib.request import Request
from urllib.request import urlopen
from link_finder import LinkFinder



homepage_url = "https://www.indeed.com/"
page_url = ""
links = set()
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = Request(homepage_url, headers=header)


try:
    response = urlopen(req)
    if (response.getheader("Content-Type") == "text/html"):
        html_bytes = response.read()
        html_str = html_bytes.decode("utf-8")
    finder = LinkFinder(homepage_url, page_url)
    finder.feed(html_str)
    links = finder.get_page_links
except Exception as e:
    print(e)
    print("Error: " + page_url + " can't be crawled")
