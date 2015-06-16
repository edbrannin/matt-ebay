import csv
import sys

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

def main(csv_filename, template_filename):
    template = env.get_template(template_filename)
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print template.render(**row)
            break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "USAGE: {} CSV_FILENAME TEMPLATE_FILENAME".format(sys.argv[0])
    else:
        main(*sys.argv[1:])
