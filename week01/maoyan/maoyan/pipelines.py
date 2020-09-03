# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        return item


# import csv
# import os

# class MaoyanmoviePipeline:
#     def __init__(self):
#         store_file = os.path.dirname(__file__) + '/maoyan_movies.csv'

#         self.file = open(store_file, 'a+', encoding="utf-8", newline='')

#         self.writer = csv.writer(self.file, dialect="excel")

#     def process_item(self, item, spider):
#         if item['movie_name']:
#             self.writer.writerow([item['movie_name'], item['catagories'], item['release_date']])
#         return item

#     def close_spider(self, spider):
#         self.file.close()