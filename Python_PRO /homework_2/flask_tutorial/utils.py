import random
import string
from faker import Faker
import requests


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    result = ""
    # breakpoint()
    for _ in range(length):
        result += random.choice(chars)
    return result

def open_file() -> str:
    with open('requirements.txt', 'r') as file:
        content = file.read()
    return content

def generator() -> dict:
    fake = Faker()
    Faker.seed(0)
    generated_data = ''
    final_dict = {}

    for _ in range(100):
        name = fake.name()
        email = fake.ascii_email()
        generated_data += "f{name}: {email}: \n"
        final_dict[name] = email

    with open('generated_names+emails_list_2.txt', 'w') as file1:
        for name, email in final_dict.items():
            file1.write(f"{name} : {email} \n")

    return final_dict

def finder() -> str:

    request = requests.get('http://api.open-notify.org/astros.json')
    data = request.json()
    number_value = data["number"]
    return number_value