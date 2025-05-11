import csv
import re
import sys

# Regular expression to match IBANs (basic pattern for EU IBANs: 2 letters + digits)
IBAN_REGEX = r'\b[A-Z]{2}[0-9A-Z]{13,34}\b'

def extract_iban_and_company(text):
    matches = list(re.finditer(IBAN_REGEX, text))
    if not matches:
        return '', ''
    
    last_match = matches[-1]
    iban = last_match.group()

    # Start looking after the IBAN
    start = last_match.end()
    rest = text[start:].lstrip(' |')
    company = re.split(r'\|', rest)[0].strip()

    return iban, company

def process_csv(input_file, output_file):
    with open(input_file, encoding='iso-8859-1', newline='') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        for row in reader:
            if len(row) < 2:
                writer.writerow(row + ['', ''])
                continue
            iban, company = extract_iban_and_company(row[1])
            writer.writerow(row + [iban, company])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    process_csv(input_csv, output_csv)
