from html.parser import HTMLParser
from typing import overload
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, homepage_url:str, page_url:str) -> None:
        super().__init__()
        self.homepage_url = homepage_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag:str, attrs) -> None:
        if tag == 'a':
            print("tag a")
            for (attr, value) in attrs:
                print("attr: " + attr + " | " + "value: " + value)
                if (attr == "href"):
                    url = parse.urljoin(self.homepage_url, value)
                    self.links.add(url)

    def get_page_links(self) -> set:
        return self.links

    def error(self, message) -> None:
        pass
