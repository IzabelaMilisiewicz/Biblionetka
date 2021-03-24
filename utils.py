from pkgutil import get_data
from struct import unpack
from faker import Faker
import openpyxl
import os
import unittest
import csv
from ddt import ddt, data, unpack


class MyUtils():
    fake = Faker("es_ES")
    simple_profile = fake.simple_profile()
    username = simple_profile["username"]

    os.chdir("/home/tester/PycharmProjects/Biblionetka/")
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

    @ddt
    class MojTestDDT(unittest.TestCase):
        """
        Testy oparte na danych: DDT

        Dane pobierane z pliku .csv
        """

        @data(*get_data("excel_data.csv"))
        @unpack
        def test_using_ddt(self, email, password):
            print("POCZĄTEK TESTU")
            print(email)
            print(password)
            print("KONIEC TESTU\n")

    if __name__ == "__main__":
        unittest.main(verbosity=2)