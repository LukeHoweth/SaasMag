import requests
import csv


def create_dictionary():
    """
    1)  Replicates the same AJAX call that 'https://www.saasmag.com/saas-1000-2018/' posts
        to retrive data shown in table.
    2)  Pulls the necessary data from URL and stores it in a dictionary named 'company_dict'.
    3)  Returns dictionary.
        Output -> { rank : {Company info : value} }
    """
    url = r"https://www.saasmag.com/wp-admin/admin-ajax.php?action=companydatatable_action&year=2018"
    session = requests.Session()
    session.get("https://www.saasmag.com/saas-1000-2018")

    formdata = {
        'draw': ['1'],  
        'columns[0][data]': ['0'],
        'columns[0][name]': '',
        'columns[0][searchable]': ['true'],
        'columns[0][orderable]': ['false'],
        'columns[0][search][value]': '',
        'columns[0][search][regex]': ['false'],
        'columns[1][data]': ['1'],
        'columns[1][name]': '',
        'columns[1][searchable]': ['true'],
        'columns[1][orderable]': ['false'],
        'columns[1][search][value]': '',
        'columns[1][search][regex]': ['false'],
        'columns[2][data]': ['2'],
        'columns[2][name]': '',
        'columns[2][searchable]': ['true'],
        'columns[2][orderable]': ['false'],
        'columns[2][search][value]': '',
        'columns[2][search][regex]': ['false'],
        'columns[3][data]': ['3'],
        'columns[3][name]': '',
        'columns[3][searchable]': ['true'],
        'columns[3][orderable]': ['false'],
        'columns[3][search][value]': '',
        'columns[3][search][regex]': ['false'],
        'columns[4][data]': ['4'],
        'columns[4][name]': '',
        'columns[4][searchable]': ['true'],
        'columns[4][orderable]': ['false'],
        'columns[4][search][value]': '',
        'columns[4][search][regex]': ['false'],
        'columns[5][data]': ['5'],
        'columns[5][name]': '',
        'columns[5][searchable]': ['true'],
        'columns[5][orderable]': ['false'],
        'columns[5][search][value]': '',
        'columns[5][search][regex]': ['false'],
        'columns[6][data]': ['6'],
        'columns[6][name]': '',
        'columns[6][searchable]': ['true'],
        'columns[6][orderable]': ['false'],
        'columns[6][search][value]': '',
        'columns[6][search][regex]': ['false'],
        'columns[7][data]': ['7'],
        'columns[7][name]': '',
        'columns[7][searchable]': ['true'],
        'columns[7][orderable]': ['false'],
        'columns[7][search][value]': '',
        'columns[7][search][regex]': ['false'],
        'columns[8][data]': ['8'],
        'columns[8][name]': '',
        'columns[8][searchable]': ['true'],
        'columns[8][orderable]': ['false'],
        'columns[8][search][value]': '',
        'columns[8][search][regex]': ['false'],
        'columns[9][data]': ['9'],
        'columns[9][name]': '',
        'columns[9][searchable]': ['true'],
        'columns[9][orderable]': ['false'],
        'columns[9][search][value]': '',
        'columns[9][search][regex]': ['false'],
        'columns[10][data]': ['10'],
        'columns[10][name]': '',
        'columns[10][searchable]': ['true'],
        'columns[10][orderable]': ['false'],
        'columns[10][search][value]': '',
        'columns[10][search][regex]': ['false'],
        'columns[11][data]': ['11'],
        'columns[11][name]': '',
        'columns[11][searchable]': ['false'],
        'columns[11][orderable]': ['false'],
        'columns[11][search][value]': '',
        'columns[11][search][regex]': ['false'],
        'order[0][column]': ['11'],
        'order[0][dir]': ['asc'],
        'start': ['0'],
        'length': ['1994'],
        'search[value]': '',
        'search[regex]': ['false']}
    headers = {
        "Content-Type"      :   "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept"            :   "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding"   :   "gzip, deflate, br",
        "User-Agent"        :   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:60.0) Gecko/20100101 Firefox/60.0"}
    
    response = session.post(url, headers=headers, data=formdata).json() # Converts json file.
    
    company_data = response['data']
    company_dict = {}                           # Empty dictionary created.
    for company in company_data:
        company_dict[company[0]] = {
            'Rank'      :   company[0],
            'Name'      :   company[1],         # Grabs relevant data for every company from 
            'City'      :   company[4],         # json file & adds it to our previously 
            'State'     :   company[5],         # created dictionary.
            'Employees' :   company[8],
            'Growth (%)'    :   company[9],
            'Accelerator/Investor'  :   company[10],
            'Website'   :   company[2],
            'LinkedIn'  :   company[3]}
    return company_dict                         # Returns dictionary that we can now write to CSV.

def write_to_csv():
    """
    1) Calls 'create_dictionary()' to return business data dictionary.
    2) Writes returned dictionary into a CSV file named '2018 SAAS 1000.csv'.
    """
    dictionary = create_dictionary()            # Calls 'create_dictionary()' to return business data.
    with open('2018 SAAS 1000.csv', 'w') as fp:
        writer = csv.DictWriter(fp, fieldnames=['Rank', 'Name', 'City', 'State', 'Employees', 'Growth (%)', 'Accelerator/Investor', 'Website', 'LinkedIn'])
        writer.writeheader()
        for value in dictionary.values():                    
            writer.writerow((value))                                      
    print("\nData exported to CSV.\n")


write_to_csv()          # Finally, we call the write_to_csv()
                        # function which scrapes the data, 
                        # then writes it to a CSV.