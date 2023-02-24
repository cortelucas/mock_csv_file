import csv
from faker import Faker

fake = Faker("pt_BR")

number_of_records: int = int(input("Insira o número de registros que quer gerar: "))

with open("data/records.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["id", "name"])

    for i in range(1, number_of_records + 1):
        id = i
        name = fake.first_name()

        writer.writerow([id, name])
