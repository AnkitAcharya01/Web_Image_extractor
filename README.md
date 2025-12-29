# Image Scraper with Threading

A Python tool to scrape images from a webpage, supporting multiple image sources (`src`, `data-src`, `srcset`) and downloading them concurrently using threads.

## Features

- Extracts image URLs from HTML `<img>` tags.  
- Supports standard `src`, lazy-loaded `data-src`, and `srcset` attributes.  
- Downloads images with `.jpg`, `.jpeg`, or `.png` extensions.  
- Uses `ThreadPoolExecutor` for faster concurrent downloads.  
- Filters invalid URLs and logs rejected images.  
- Saves images in a dedicated directory with unique filenames.

## My Objetives

- Download images from a webpage for offline viewing  
- Learn how web scraping works using BeautifulSoup  
- Understand practical usage of multithreading with network I/O  
- Experiment with HTML parsing and URL normalization  
- Build a base for more advanced crawlers or dataset collection tools

## Requirements

- Python 3.8+  
- Install dependencies from `requirements.txt`:
- Run: (pip install -r requirements.txt) in the terminal

## Usage (direct standalone running)
- Clone the repository
- Create a virtual environment:

    - Windows:
    python -m venv myvenv
    myvenv\Scripts\activate

    - Linux/Mac:
    source myvenv/bin/activate

- Install required packages
pip install -r requirements.txt

- Run the project
python image_extractor.py

## Usage (Integration on a project)

- Place the scraper script in your project folder.
- Run the script:

import image_extractor as scrape


url = "https://example.com/page-with-images"
scrape.scrape_img(url)


- Images are saved automatically in a folder named Scraped_images.



## Notes

- The scraper downloads only `.jpg`, `.jpeg` and `.png` images.  
- Thread count can be adjusted to control speed and server load.
- Always respect the website’s terms of service and robots.txt.

## License

MIT License — free to use and modify.