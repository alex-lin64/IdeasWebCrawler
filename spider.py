from urllib.request import urlopen
from link_finder import LinkFinder
from common import all, create_data_files, create_project_dir, file_to_set


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

    @staticmethod
    def boot() -> None:
        create_project_dir(Spider.dir_path)
        create_data_files(Spider.dir_path, Spider.homepage_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name:str, page_url:str) -> None:
        if (page_url in Spider.crawled):
            return
        print(thread_name + ": " + page_url)
        print('queue: ' + str(len(Spider.queue)) + " | " + "crawled: " + str(len(Spider.crawled)))
        Spider.add_links_queue(Spider.gather_links(page_url))
        Spider.queue.remove(page_url)
        Spider.crawled.add(page_url)
        Spider.update_files()

    def add_links_queue(self, links_to_add: set) -> None:
        for url in links_to_add:
            pass

    @staticmethod
    def gather_links(page_url:str) -> set():
        html_str = ""
        try:
            response = urlopen(page_url)
            if (response.getheader("Content-Type") == "text/html"):
                html_bytes = response.read()
                html_str = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.homepage_url, page_url)
            finder.feed(html_str)
        except:
            print("Error: " + page_url + " can't be crawled")
            return set()
        return finder.get_page_links()
        
    @staticmethod
    def update_files():
        pass
