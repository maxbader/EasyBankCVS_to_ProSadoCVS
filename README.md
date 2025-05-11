# EasyBankCVS_to_ProSadoCVS
This Python script converts a CSV extracted form Austrian / Österreich the Easy Bank App to a ProSado readable CSV. 
It will most likey also work with the BAWAG Bank

## Usage
1. Open your easybank account
1. Make a 'Umsatzsuche' over the time/date to extract
1. Download a CSV file from https://ebanking.easybank.at/ 
1. Run the Python script with the following arguments; the first should be your extracted CSV
```
./easybank_csv_to_prosaldo_csv.py input.csv output.csv
```
1. Open your 'ProSaldo' account
1. select 'Bank & Buchen'
1. select 'CSV-/TXT-Import'
1. Upload your `output.csv`
1. Establish a correct and useful relation.

## Code 
The code was generated using the LLM ChatGPT with the following prompt:
```
Can you help me to create a simple python script. It should process a CSV file with  semicolons as a delimiter and output a new CSV file. The input file is ISO-8859-1 encoded, while the output should be UTF-8. The input file name and the output filename are arguments to the script. The input CSV has no header row.
The script should always add two entries on each row: the IBAN and a company name.
The IBAN is found in the string of the second column. If there is more than one IBAN in the string, the last appearance should be used.
The company name can be found after the IBAN if there is a space or pipe character, and it ends with the entry or another pipe character.

There are some bank IBANs as an example.
LU89751000135102200E
DE79590500000020025855
AT113293900005511726
```
