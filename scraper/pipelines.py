import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), '../info.csv')

def write_to_csv(item):
    writer = csv.writer(open(csv_path, 'a'))
    writer.writerow([item[key] for key in item.keys()])

class CsvWriterPipeline(object):
    def process_item(self, item, spider):
        write_to_csv(item)
        return item
