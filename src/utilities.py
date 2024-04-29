if __name__ == 'main':
    main()

import pandas as pd
import chardet

def clean_and_format_data(filepath):
    # Identify the encoding type (as data set is in German and therefore contains characters that go beyond the UTF-8 encoding) 
    with open(filepath, 'rb') as file:
        content = file.read(100000)
        result = chardet.detect(content)
    print("Detected encoding:", result['encoding'])

    # Clean up file structure
    df = pd.read_csv(filepath, encoding=result['encoding'], sep=';')
    df = df.drop([0, 1])
    df = df.reset_index(drop=True)
    df = df.rename(columns={'Unnamed: 0': 'Art des Gutes'})
    df.set_index('Art des Gutes', inplace=True)

    new_columns = []
    year = 2014  # Starting year in this case
    for col in df.columns:
        if '.1' not in col:
            new_columns.append((year, 'Import'))
        else:
            new_columns.append((year, 'Export'))
            year += 1
    
    # Convert all columns to numeric, setting errors to 'coerce' (-> converts non-convertible values to NaN)
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    df.fillna(0, inplace=True) # Fill NaN values with zero
    df = df.astype(int)  

    df.columns = pd.MultiIndex.from_tuples(new_columns)
    return df