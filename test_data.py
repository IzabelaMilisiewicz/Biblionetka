from faker import Faker
import openpyxl
import os
import unittest
import csv

class TestData(unittest.TestCase):
    fake = Faker("es_ES")
    simple_profile = fake.simple_profile()
    username = simple_profile["username"]

    os.chdir("/home/tester/Dokumenty/Biblionetka/")
    workbook = openpyxl.load_workbook("accounts.xlsx")
    sheet = workbook["Arkusz1"]
    password = sheet["B2"].value

    valid_password = "qwerty123"
    valid_email = "iza@wp.pl"
    invalid_email = "qwerty.pl"

    def get_data(file_name):
        rows = []
        data_file = open(file_name, 'rt')
        reader = csv.reader(data_file)
        # Pomijam pierwszy wiersz
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows

