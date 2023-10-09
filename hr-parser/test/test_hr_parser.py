from hr_parser.main import parse_record

big_fixture = [
    {
        "first name": "Emily",
        "last name": "Johnson",
        "email": "emily.johnson@example.com",
        "date of birth": "1985-07-12",
    },
    {
        "first name": "Michael",
        "last name": "Smith",
        "email": "michael.smith@example.com",
        "date of birth": "1992-09-05",
    },
    {
        "first name": "Emma",
        "last name": "Williams",
        "email": "emma.williams@example.com",
        "date of birth": "1988-12-19",
    },
    {
        "first name": "Christopher",
        "last name": "Jones",
        "email": "christopher.jones@example.com",
        "date of birth": "1979-03-28",
    },
    {
        "first name": "Olivia",
        "last name": "Brown",
        "email": "olivia.brown@example.com",
        "date of birth": "1996-06-04",
    },
    {
        "first name": "William",
        "last name": "Taylor",
        "email": "william.taylor@example.com",
        "date of birth": "1982-10-17",
    },
]

normal_fixture = {
    "first name": "Emily",
    "last name": "Johnson",
    "email": "emily.johnson@example.com",
    "date of birth": "1985-07-12",
}

long_name_fixture = {
    "first name": "Christopher",
    "last name": "Jones",
    "email": "christopher.jones@example.com",
    "date of birth": "1979-03-28",
}

fixture_middle_name = {
    "first name": "William Fitzgerald",
    "last name": "Taylor",
    "email": "william.taylor@example.com",
    "date of birth": "1982-10-17",
}

def test_parse_normal_record():
    assert parse_record(normal_fixture) == (
        "emily.johnson@example.com",
        "Emily Johnson",
    )


def test_parse_long_name_record():
    assert parse_record(long_name_fixture) == (
        "christopher.jones@example.com",
        "C. Jones",
    )


def test_parse_name_with_middle():
    assert parse_record(fixture_middle_name) == (
        "william.taylor@example.com",
        "William Taylor",
    )
