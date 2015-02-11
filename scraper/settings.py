SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
ITEM_PIPELINES = {'scraper.pipelines.CsvWriterPipeline': 100}
EXPORT_FIELDS = [
    'name',
    'link',
    'industry'
]
FEED_FORMAT = 'csv'
DEFAULT_ITEM_CLASS = 'scraper.items.Startup'
