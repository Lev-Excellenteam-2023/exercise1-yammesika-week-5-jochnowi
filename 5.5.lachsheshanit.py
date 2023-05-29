import re


def extract_messages(path, expression):
    with open(path, 'rb') as reader:
        result = []
        for line in reader.readlines():
            result += re.findall(expression, str(line))
        for message in result:
            print(message)


regex = '[a-x]{5,20}!'
extract_messages("logo.jpg", regex)