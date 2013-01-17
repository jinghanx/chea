# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    category_1 = Field()
    category_2 = Field()
    name_english = Field()
    name_chinese = Field()
    address = Field()
    city = Field()
    number = Field()

class ZipcodeItem(Item):
    number = Field()
    zipcode = Field()
