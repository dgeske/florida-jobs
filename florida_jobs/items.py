# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class FloridaJobsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    employer = Field()
    location = Field()
    position = Field()
    department = Field()
    hire_date = Field()
    # gender = Field()
    # race = Field()
    salary = Field()
    # base_rate = Field()
    # date_range = Field()
