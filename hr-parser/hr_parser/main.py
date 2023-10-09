from typing import Tuple

import requests


def url_reader():
    url = "https://s3.eu-west-2.amazonaws.com/interview.thanskben.com/backend/employees.json"
    content = requests.get(url)
    return content.json()


def parse_record(record: dict) -> Tuple[str, str]:
    email = record['email']
    first_name = record['first name']
    last_name = record['last name']
    concat_name = first_name + " " + last_name
    if len(concat_name) > 15:
        split_first_name = first_name.split(" ")
        first_name = split_first_name[0]
        concat_name = first_name + " " + last_name
    if len(concat_name) > 15:
        concat_name = first_name[0] + ". " + last_name
    return email, concat_name


def csv_writer(records: list) -> None:
    with open('output.csv', 'w') as f:
        f.write('Email;Short Full Name\n')
        for record in records:
            email, full_name = parse_record(record)
            f.write(f'{email};{full_name}\n')


def parse_hr_records():
    records = url_reader()
    csv_writer(records)


if __name__ == "__main__":
    parse_hr_records()
