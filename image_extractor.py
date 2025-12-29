from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor


#replace the website url here
url = 'https://www.annapurnaencounter.com/travel-guide/the-majestic-mountains-of-the-annapurna-range'
os.makedirs("Scraped_images", exist_ok=True)

def get_img_srcs(img, base_url):
    img_srcs = []
    #normal src
    src = img.get('src')
    if src:    
        img_srcs.append(src)
    
    #data-src
    data_src = img.get('data-src')
    if data_src:
        img_srcs.append(data_src)

    #srcset
    srcset = img.get('srcset')
    if srcset:
        candidates = srcset.split(',')           #seperates the srcset into list
        last = candidates[-1].strip().split()[0] #takes the last element, removes padding spaces
                                                 #again seperates the element using whitespace, and takes element[0]
        img_srcs.append(last)
    
    clean_src = []
    for s in img_srcs:
        if s.startswith("//"):
            s= "https:" + s
        s = urljoin(base_url, s)
        clean_src.append(s)
    return clean_src

HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }
def scrape_img(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"{len(soup.text)} characters scanned.")
        img_tags = soup.find_all('img')

        src_all =[]
        for img_tag in img_tags:
            print(f"Got {img_tag}")
            src_all.extend(get_img_srcs(img_tag, url))
                    

        #validate src_img that came from above extractor function
        src_valid = []
        for src in src_all:
            if src.lower().endswith(('.jpg', '.jpeg', '.png')): #add '.svg' here if needed
                src_valid.append(src)
                print(f"Cleaned Url: {src}")
            else:
                print(f"Rejected: {src}")
        print(f"Found {len(src_valid)} images. Downloading...")    

        with ThreadPoolExecutor(max_workers=10) as ex:  #for Multithreading while downloading
            ex.map(download, src_valid)

    except Exception:
        print(f"Couldn't scrape provided URL {url}: {Exception}")   

#download jpeg/png files
def download(src_valid):
    try:
        img_name = os.path.join("Scraped_images", os.path.basename(src_valid))
        img_data = requests.get(src_valid, headers=HEADERS, timeout=10).content
        with open(img_name, "wb") as f:
            print(f"Downloading image: {img_name}")
            f.write(img_data)
    except Exception:
        print(f"Couldn't download the image, {Exception}")
   
if __name__ == "__main__":
    scrape_img(url)
 
