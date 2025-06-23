#CSV file
import csv 
data = [['Name','address','mobile','email'],
        ['AKon','Texas','123456','akon@mail'],
        ['Bkon','New York','234653','bkon@mail'],
        ['Ckon','California','345678','ckon@gmail'],
        ['Dkon','Texas','234567','dkon@gmail']
]
with open('address_book.csv','w') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

