import pandas as pd
import argparse
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://localhost/rishik')
conn=engine.connect()
# Create the parser
my_parser = argparse.ArgumentParser(description='Parse data file')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

csv_file=input_path;
df_from_csv = pd.read_csv(csv_file, sep='\t', on_bad_lines='skip')
df_from_csv.info()
print(df_from_csv['nr_cnpj'])
df_from_csv.to_sql("altana-db",conn,if_exists= 'replace',index=False,chunksize=100)
