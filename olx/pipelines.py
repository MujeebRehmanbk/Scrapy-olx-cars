# # -*- coding: utf-8 -*-

# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# import csv
# class OlxPipeline(object):

#     def __init__(self):
#         self.csvwriter = csv.writer(open("olllx3.csv", "w",newline='')
#         self.csvwriter.writerow(["title","description","display_date","Picture_link","Location","On_road","Price"])

#     def process_item(self, item, spider):
#         row = []
#         row.append(item["title"])
#         row.append(item["description"])
#         row.append(item["display_date"])
#         row.append(item["Picture_link"])
#         row.append(item["Location"])
#         row.append(item["On_road"])
#         row.append(item["Price"])
#         # row.append(item["distributor"])
#         # row.append(item["opening_revenue"])
#         self.csvwriter.writerow(row) 

        
#         return item




