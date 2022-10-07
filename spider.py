from urllib.request import urlopen
from link_finder import LinkFinder
from common import all

class Spider:

    dir_path = ''
    homepage_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, dir_path:str, homepage_url:str, domain_name:str) -> None:
        Spider.dir_path = dir_path
        Spider.homepage_url = homepage_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.dir_path + '/queue.txt'
        Spider.crawled_file = Spider.dir_path + '/crawled.txt'
        self.boot()
        self.crawl_page("init_spider", Spider.homepage_url)

    def boot(self):
        pass

    def crawl_page(self):
        pass

