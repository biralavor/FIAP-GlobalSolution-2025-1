import csv

def csv_loader(path: str) -> list:
    data = []
    if path.endswith('.csv'):
        with open(path, 'r', encoding='utf-8') as file:
            entire_file = csv.reader(file)
            for row in entire_file:
                data.append(row)
    return data

def csv_parser(data: list) -> dict:
    parsed_data = {}
    for row in data[1:]:
        district = row[2]
        name = row[5]
        if district not in parsed_data:
            parsed_data[district] = []
        parsed_data[district].append(name)
    # print(f"Neighborhoods in the database: {parsed_data}\n\n")
    return parsed_data

def neighborhood_list_loader(parsed_data: dict) -> dict:
    neighborhood_list = {}
    for districts in parsed_data.items():
        for neighborhood in districts[1]:
            if neighborhood not in neighborhood_list:
                neighborhood_list[neighborhood] = []
    return neighborhood_list
