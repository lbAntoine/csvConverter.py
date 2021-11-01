import pandas as pd
import re


csv_format = '.csv'
regex = r"(?P<rpath>.*?)(?P<rfile_name>[^\\]+)(?P<extension>=?.json)"


def json_to_csv():


    print(f'Starting converter...')
    
    input_from = input(r'What\'s the path of the file you want to convert: ')
    
    cf = pd.read_json(input_from) # Passe le fichier (avec path pour le regex)
    
    print(cf)

    reg_input = re.match(regex, input_from) #split le path pour automatiser la nomination du csv et son path
    
    print(f'Getting json file...')
    print(f'Converting to csv file...')
    
    fpath = reg_input.group(1)
    print(f' - File path: {fpath}')
    file_name = reg_input.group(2)
    print(f' - File name: {file_name}')
    
    
    cf.to_csv(fpath+file_name+csv_format, sep=';')

    print(f'Done!')

json_to_csv()