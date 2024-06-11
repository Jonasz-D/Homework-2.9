import json
from seeds import load_data_to_db
from scrap_data import scrap_authors, scrap_quotes


URL = 'https://quotes.toscrape.com'
   
def create_json_files(data, file_name):
    with open(f'./data/{file_name}', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=len(data))

def parse_to_json(data):
    json_data = json.dumps(data)
    return json_data

if __name__ == '__main__':
    quores = scrap_quotes(URL)
    authors = scrap_authors(URL)
    
    create_json_files(quores, 'quotes.json')
    create_json_files(authors, 'authors.json')
    load_data_to_db()
