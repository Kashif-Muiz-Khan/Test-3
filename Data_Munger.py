import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"


with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)


    header = ["sales", "date", "region"]
    writer.writerow(header)


    for file_name in os.listdir(DATA_DIRECTORY):
        # open the csv file for reading
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)

            row_index = 0
            for input_row in reader:
                # if this row is not the csv header, process it
                if row_index > 0:
                    # collect data from row
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # if this is a pink morsel transaction, process it
                    if product == "pink morsel":
                        # finish formatting data
                        price = float(raw_price[1:])
                        sale = price * int(quantity)

                        # write the row to output file
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1