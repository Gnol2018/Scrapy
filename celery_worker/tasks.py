# tasks.py
from celery import Celery
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Import your Scrapy spider from the correct path
from scrapy_worker.price_crawler.spiders.gpu_spider import GpuSpider

app = Celery('tasks', broker='amqp://guest:guest@localhost//', backend='rpc://')

@app.task
def run_spider():
    # Load Scrapy settings
    scrapy_settings = get_project_settings()

    # Create a crawler process with provided settings
    process = CrawlerProcess(settings=scrapy_settings)

    # Add your spider to the process
    process.crawl(GpuSpider)

    # Start the crawling process
    process.start()
