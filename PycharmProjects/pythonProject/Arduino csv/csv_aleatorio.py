import csv
import random
import time

x_value = 0
y1 = 1000
y2 = 1000
y3 = 1000

fieldnames = ["x_value", "y1", "y2", "y3"]


with open('data1.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:

    with open('data1.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "y1": y1,
            "y2": y2,
            "y3": y3
        }

        csv_writer.writerow(info)
        print(x_value, y1, y2, y3)

        x_value += 1
        y1 += random.randint(-6, 8)
        y2 += random.randint(-6, 8)
        y3 += random.randint(-6, 9)

    time.sleep(1)