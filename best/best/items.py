# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BestItem(scrapy.Item):
    # define the fields for your item here like:
    bNumero = scrapy.Field()
    cCodice_fiscale = scrapy.Field()
    dPEC = scrapy.Field()
    eStatus = scrapy.Field()
    aNome = scrapy.Field()
    fIndirizzo = scrapy.Field()  # Via C. Pomo
    gCitta_provincia = scrapy.Field()  # Milano
