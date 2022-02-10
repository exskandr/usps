import csv
from rqst import status_check_address


def csv_to_json(csv_file):
    """convert csv to json"""
    json_array = []
    with open(csv_file, encoding='utf-8') as csv_f:      # read csv file
        csv_reader = csv.DictReader(csv_f)               # load csv file data using csv library's dictionary reader
        for row in csv_reader:                           # convert each csv row into dict
            json_array.append(row)                       # add this python dict to json array
    return json_array


def data_for_request(data):
    """preparation of json-data for the request"""
    request = {}
    request["companyName"] = data['Company']
    request["address1"] = data['Street']
    request["address2"] = ''
    request["city"] = data['City']
    request["state"] = data['St']
    request["urbanCode"] = ''
    request["zip"] = data['ZIPCode']
    return request


def list_status(response):
    """create response list """
    list = []
    for i in range(len(response)):
        status = response[i]
        address_req = data_for_request(status)
        s = status_check_address(address_req)
        list.append(s)
    return list


def write_output_file(input_file, output_file):
    # read csv file
    with open(input_file, 'r') as f_input:
        # create source file for writing
        with open(output_file, 'w') as f_output:
            writer = csv.writer(f_output, lineterminator='\n')
            reader = csv.reader(f_input)
            out_data = []
            row = next(reader)
            row.append('AddressVerification')         # add column to outfile
            out_data.append(row)                      # add row
            json_string = csv_to_json(input_file)     # convert input file to json
            result_status = list_status(json_string)  # create a status response list
            i = 0
            for row in reader:
                row.append(result_status[i])          # add response status to output file
                out_data.append(row)
                i += 1
            writer.writerows(out_data)


if __name__ == "__main__":
    csv_input_file = r'quiz_input.csv'
    csv_output_file = r'quiz_output.csv'
    write_output_file(csv_input_file, csv_output_file)
