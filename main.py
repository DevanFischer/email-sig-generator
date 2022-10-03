import csv

EMPLOYEE_FILE = "input/employees.csv"
TEMPLATE_FILE = "TEMPLATE.min.html"
OUTPUT_PATH = "output"
employees = []


def main():
    employee_array = read_csv_to_dictArray(EMPLOYEE_FILE)
    for employee in employee_array:
        template_string = read_template(TEMPLATE_FILE)
        formatted_string = replace_employee_data(employee, template_string)
        out_file_name = format_file_name(employee)
        write_html(out_file_name, formatted_string)
    # TODO: Zip output folder to email_signatures.zip


def read_csv_to_dictArray(file, array=[]):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            array.append(row)
    return array


def read_template(file, string=""):
    with open(file, "r") as f:
        string = f.read()
    return string


def replace_employee_data(employee, template):
    for record in employee:
        template = template.replace(record, employee[record])
    return template


def format_file_name(employee):
    first = employee["EMPLOYEE_FIRST_NAME"]
    last = employee["EMPLOYEE_LAST_NAME"]
    return f"{first}{last}_eSig.html"


def write_html(file_name, string):
    with open(f"{OUTPUT_PATH}/{file_name}", "w+") as file:
        file.write(string)


main()
