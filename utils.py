def get_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        file_data = f.read()
        print(file_data)

get_data()
