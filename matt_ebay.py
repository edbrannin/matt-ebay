import csv
import sys

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

HTML_FIELDNAME = "HTML"

def main(csv_filename, template_filename):
    template = env.get_template(template_filename)
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(sys.stdout, reader.fieldnames + [HTML_FIELDNAME])
        writer.writeheader()
        for row in reader:
            html = template.render(**row)
            if len(html) > 32766:
                raise Exception("Result is too long for row {}: ".format(row, html))
            row[HTML_FIELDNAME] = html.replace("\n", "")
            writer.writerow(row)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "USAGE: {} CSV_FILENAME TEMPLATE_FILENAME".format(sys.argv[0])
        print "(The result will be written to stdout)"
    else:
        main(*sys.argv[1:])
