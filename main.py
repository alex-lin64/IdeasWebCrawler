import threading
from queue import Queue
from spider import Spider
from domain import *
from common import *


PROJECT_DIR = "thenewboston"
HOMEPAGE = "https://thenewboston.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_DIR + "/queue.txt"
CRAWLED_FILE = PROJECT_DIR + "/crawled.txt"
NUMBER_OF_THREADS = 2

thrd_queue = Queue()
Spider(PROJECT_DIR, HOMEPAGE, DOMAIN_NAME)

