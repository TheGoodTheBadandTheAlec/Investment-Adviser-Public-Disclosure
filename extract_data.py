import xml.etree.ElementTree as ET
import csv
import gzip
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    confidence = result['confidence']
    return encoding, confidence

def extract_info_from_xml(xml_file):
    encoding, confidence = detect_encoding(xml_file)
    with gzip.open(xml_file, 'rt', encoding=encoding) as file:
        tree = ET.parse(file)
        root = tree.getroot()

        data = []

        for firm in root.findall('.//Firm'):
            info = firm.find('./Info')
            main_addr = firm.find('./MainAddr')

            legal_name = info.get('LegalNm', '')
            business_name = info.get('BusNm', '')
            address = main_addr.get('Strt1', '')
            city = main_addr.get('City', '')
            state = main_addr.get('State', '')
            country = main_addr.get('Cntry', '')
            zipcode = main_addr.get('PostlCd', '')
            phone_number = main_addr.get('PhNb', '')

            website_elem = firm.find('.//WebAddr')
            website = website_elem.text if website_elem is not None else ''

            total_assets_elem = firm.find('.//Item5F')
            total_assets = total_assets_elem.get('Q5F2C', '') if total_assets_elem is not None else ''

            clients_elem = firm.find('.//Item5H')
            clients = clients_elem.get('Q5H', '') if clients_elem is not None else ''

            data.append([legal_name, business_name, address, city, state, country, zipcode, phone_number, website, total_assets, clients])

        return data

def main():
    xml_files = [
        r'C:\Users\alecj\python\Investment Adviser Public Disclosure\IA_FIRM_STATE_Feed_11_28_2023.xml.gz',
        r'C:\Users\alecj\python\Investment Adviser Public Disclosure\IA_FIRM_SEC_Feed_11_28_2023 (1).xml.gz'
    ]

    output_file = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\extract_data.csv'

    all_data = []

    for xml_file in xml_files:
        data = extract_info_from_xml(xml_file)
        all_data.extend(data)

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow(['LegalNm', 'BusNm', 'Address', 'City', 'State', 'Country', 'Zipcode', 'Phone_Number', 'Website', 'Total_Assets', 'Clients'])
        # Write data
        csv_writer.writerows(all_data)

if __name__ == "__main__":
    main()

import csv

input_file_path = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\extract_data.csv'
output_file_path = r'C:\Users\alecj\python\Investment Adviser Public Disclosure\extract_data.csv'
