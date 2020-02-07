DATA_DIR = 'raw-data/'

filenames = {
    2020: 'nyc_pluto_20v1_csv/pluto_20v1.csv',
    2017: 'Borofiles_CSV/MN2017V1.csv',
    2014: 'nyc_pluto_14v1/MN.csv',
    2011: 'nyc_pluto_11v1/MN11v1.txt',
}

def extract_columbia(f, year):
    output = [ f'{next(f).strip()},Year\n' ]

    for line in f:
        if 'trustees of columbia' in line.lower():
            output.append(f'{line.strip()},{year}\n')
            print(len(output), end='\r')
    print()
    return output

if __name__ == '__main__':
    rows = []
    for y in filenames.keys():
        print('Year', y, '=' * 5)
        with open(DATA_DIR + filenames[y]) as fr:
            rows += extract_columbia(fr, y)
    with open(f'aggregate.csv', 'w') as fw:
        fw.write(''.join(rows))
