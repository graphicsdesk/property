DATA_DIR = 'raw-data/'

filenames = {
    20: 'nyc_pluto_20v1_csv/pluto_20v1.csv',
    17: 'Borofiles_CSV/MN2017V1.csv',
    14: 'nyc_pluto_14v1/MN.csv',
    11: 'nyc_pluto_11v1/MN11v1.txt',
}

def extract_columbia(f):
    output = [ next(f) ]

    for line in f:
        if 'trustees of columbia' in line.lower():
            output.append(line)
            print(len(output), end='\r')
    return output

if __name__ == '__main__':
    for y in filenames.keys():
        print('Year', y, '=' * 5)
        with open(DATA_DIR + filenames[y]) as f:
            rows = extract_columbia(f)
            print(len(rows))
        with open(f'out-{y}.csv', 'w') as f:
            f.write(''.join(rows))
            print('wrote', y)
