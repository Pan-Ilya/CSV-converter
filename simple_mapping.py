import csv
import re


class SimpleCSVMapper:

    @staticmethod
    def read_csv_file(filename: str) -> list:
        """Читаю CSV документ с именем filename."""

        with open(filename) as f:
            reader = csv.reader(f)
            return list(reader)

    @staticmethod
    def write_csv_file(data: list, filename: str) -> None:
        """Записываю данные data в новый документ с именем filename."""

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

    @staticmethod
    def string_to_slug(data: str):
        """Пример преобразования входящей строки в слаг."""

        data = data.lower().strip()
        data = re.sub(r'[^\w\s-]', '', data)
        data = re.sub(r'[\s_-]+', '-', data)
        data = re.sub(r'^-+|-+$', '', data)
        return data

    @staticmethod
    def increase_price(price: str, percent: int) -> float:
        """Пример преобразования цены, увеличение стоимости на указанный процент."""

        return int(price) + int(price) * percent * 0.01


# Пример использования. Читаю данные из документа -> Выполняю преобразования -> Сохраняю в новый документ.

# 1) Читаю данные:
data_from_file = SimpleCSVMapper.read_csv_file('example.csv')
for el in data_from_file:
    print(el)

# 2) Преобразую данные:
header = data_from_file[0]
new_data = list()

for row in data_from_file[1:]:
    row[0] = SimpleCSVMapper.string_to_slug(row[0])
    row[2] = SimpleCSVMapper.increase_price(row[2], 20)
    new_data.append(row)

result = new_data.insert(0, header)

# 3) Записываю данные:
SimpleCSVMapper.write_csv_file(new_data, 'result.csv')
