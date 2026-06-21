"""
CSV Storage Module

Stores health data into CSV file.
"""


import csv

import os



DATA_FILE = "data/health_data.csv"



HEADERS = [

    "timestamp",

    "battery",

    "heart_rate",

    "steps",

    "spo2"

]



def save_health_data(data):


    file_exists = os.path.isfile(
        DATA_FILE
    )


    with open(
        DATA_FILE,
        mode="a",
        newline=""
    ) as file:


        writer = csv.DictWriter(
            file,
            fieldnames=HEADERS
        )


        if not file_exists:

            writer.writeheader()


        writer.writerow(
            data
        )