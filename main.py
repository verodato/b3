import subprocess
from request_b3 import RequestB3
from datetime import datetime
from b3_xml2table import xml2table



def main():
    # Let's pass today's date to the method that will download the file
    _request_data = datetime.today().strftime('%y%m%d')
    #_request_data = '220523'  # Test
    
    # download, unzip etc 
    RequestB3(_request_data).start()
    
    # extract selected info from xlm file into a table and save results in the tsv directory
    xml2table()
    

if __name__ == '__main__':
    main()
