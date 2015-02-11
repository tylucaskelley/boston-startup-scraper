from scrapy.item import Item, Field

class Startup(Item):
    name = Field()
    link = Field()
    industry = Field()
