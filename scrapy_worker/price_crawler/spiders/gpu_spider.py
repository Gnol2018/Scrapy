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
        print("working here")
        gpu_items = response.xpath("//div[@class='product-item']")
        for item in gpu_items:
            gpu_link = item.xpath(".//h3/a/@href").get()
            gpu_name = item.xpath(".//h3/a/text()").get()
            gpu_price = item.xpath(".//p[@class='pdPrice']/span/text()").get()
            print(f"{gpu_name}: {gpu_price} - Link: {gpu_link}")

