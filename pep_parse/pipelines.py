import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime as dt

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    status_dict = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):

        self.status_dict[item['status']] += 1
        return item

    def close_spider(self, spider):
        save_time = dt.now().strftime('%Y-%m-%dT%H-%M-%S')
        filename = f'status_summary_{save_time}.csv'
        folder = BASE_DIR / 'results'
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, filename)

        with open(file_path, mode='w', encoding='utf-8') as f:

            f.write('Статус,Количество\n')
            for key, value in self.status_dict.items():
                f.write(f'{key},{value}\n')

            f.write(f'Total,{sum(self.status_dict.values())}\n')
