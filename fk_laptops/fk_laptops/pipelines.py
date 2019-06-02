# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import PickleItemExporter


class FkLaptopsPipeline(object):
    # def open_spider(self,spider):
    #   pickle_out=open("dict.pickle","wb")
    #   self.file_handle = pickle_out
    #   self.exporter=PickleItemExporter(pickle_out)
    #   self.exporter.start_exporting()
    # def close_spider(self,spider):
    #   self.exporter.finish_exporting()
    #   self.file_handle.close()
    # def process_item(self, item, spider):
    #   self.exporter.export_item(item)
    return item
