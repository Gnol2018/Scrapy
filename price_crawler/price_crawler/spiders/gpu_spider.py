from pathlib import Path
import scrapy

class GpuSpider(scrapy.Spider):
    name = "gpu_spider"

    def start_requests(self):
        urls = [
            "https://tinhocngoisao.com/collections/vga-nvidia-cu",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        gpu_items = response.xpath("//div[@class='product-item']")
        
        print(f"len(gpu_items): {len(gpu_items)}")
        for item in gpu_items:
            test = item.xpath(".//h3").get()
            print(f"test here: {test}")
        filename = "gpu_titles_and_prices.html"
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{gpu_items}")


        # self.log(f"Saved file {filename}")
