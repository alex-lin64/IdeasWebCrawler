from urllib.parse import urlparse


# gets the domain name -- only last two, xxxx.xxxx.xxxx.domain.xxx
def get_domain_name(url:str) -> str:
    try:
        return urlparse(url).netloc
    except:
        return ""

# parse and extracts last two sub-domain name
def extract_sub_domain(url:str) -> str:
    try:
        sub_domains = get_domain_name(url).split('.')
        return sub_domains[-2] + "." + sub_domains[-1]
    except:
        return ""
