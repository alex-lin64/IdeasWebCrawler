from urllib.request import urlopen
from link_finder import LinkFinder


def gather_links(homepage_url:str, page_url:str) -> set():
    html_str = ""
    try:
        response = urlopen(page_url)
        if (response.getheader("Content-Type") == "text/html"):
            html_bytes = response.read()
            html_str = html_bytes.decode("utf-8")
        finder = LinkFinder(homepage_url, page_url)
        finder.feed(html_str)
    except:
        print("Error: " + page_url + " can't be crawled")
        return set()
    return finder.get_page_links()


test_set = gather_links("https://math.stackexchange.com/", "https://math.stackexchange.com/questions/4052482/residual-vectors-and-range?noredirect=1&lq=1")
for item in test_set:
    print(item)
finder = LinkFinder("https://math.stackexchange.com/", "https://math.stackexchange.com/questions/4052482/residual-vectors-and-range?noredirect=1&lq=1")
print(finder.feed("<a href=https://www.python.org/ class=nav-logo><img src=../_static/py.svg alt=Logo></a>"))