import scrapy
import pickle
import sys
from scrapy.crawler import CrawlerProcess


class FkartLaptopsSpider(scrapy.Spider):
    page_number = 2
    name = 'fkart_laptops'
    start_urls = [
        'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker'
        '=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT'
        '&as-searchtext=loptop&page=1']
    no_of_laptops = sys.argv[1]  ##total number of laptops to be scrapped
    no_of_laptops = eval(no_of_laptops) ###to convert to integer
    no_of_loops = no_of_laptops // 24  ##there are 24 laptops in 1 page
    no_of_items_in_loop = no_of_laptops % 24
    loop_count = 0 
    items_count=0
    all_laptop_details=[]  ###List containing the details of laptop stored in form of dictionaries 
    max_page_number=30 ##30 pages in laptop category
'''
Since there are 24 laptops in 1 page, we divide the total no. of laptops by 24, the integer part (loop_count) of the result will tell us how many time 
the loop will run (each loop corresponds to 24 laptops) and the remainder (%24) (items_count) gives the no. of times the last loop will run.
'''
    pickle_directory=sys.argv[2]

    def parse(self, response):
        title = response.css('._3wU53n::text').extract()
        price = response.css('._2rQ-NK::text').extract()
        rating = response.css('.hGSR34::text').extract()
        items = {}
        if self.loop_count == self.no_of_loops:
            self.items_count = self.no_of_items_in_loop
            self.max_page_number=self.page_number
        else:
            self.items_count = 24

        for i in range(self.items_count):
            items.setdefault('title', []).append(title[i])
            items.setdefault('rating', []).append(rating[i])
            items.setdefault('price', []).append(price[i])
        self.all_laptop_details.append(items)
        yield items

        next_page = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker' \
                    '=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as' \
                    '-type=RECENT&as-searchtext=loptop&page=' + str(FkartLaptopsSpider.page_number)
        if FkartLaptopsSpider.page_number < self.max_page_number:
            FkartLaptopsSpider.page_number += 1
            self.loop_count += 1
            yield scrapy.Request(url=next_page, callback=self.parse)

        with open(str(self.pickle_directory)+'//dict.pickle','wb') as f:
            pickle.dump(self.all_laptop_details,f)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(FkartLaptopsSpider)
    process.start()
