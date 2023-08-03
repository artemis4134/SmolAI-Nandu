```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.pipelines import JsonWriterPipeline
from web_scraper.items import RedditScraperItem

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings={
            'BOT_NAME': 'reddit_scraper',
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'DOWNLOAD_DELAY': 3,
            'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })

    def run_spider(self, subreddit):
        self.process.crawl(RedditSpider, subreddit=subreddit)
        self.process.start()  # the script will block here until the crawling is finished

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider('all')  # replace 'all' with the subreddit you want to scrape
```