import os
import csv
from collections import defaultdict
from datetime import datetime as dt
from .settings import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_dict = defaultdict(int)

    def process_item(self, item, spider):

        self.status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        save_time = dt.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{save_time}.csv'
        folder = BASE_DIR / 'results'
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, filename)
        self.status_dict['Total'] = sum(self.status_dict.values())

        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(
                {'Статус': key, 'Количество': value} for key, value in
                self.status_dict.items()
            )
