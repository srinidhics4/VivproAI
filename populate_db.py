# Import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine

def main(file_path):
    songs_df = pd.read_json(file_path)

    # Create database engine
    engine = create_engine(
    'postgresql+psycopg2://postgres:password@127.0.0.1:5432/postgres')
    
    # Drop old table and create new empty table
    songs_df.to_sql('songs_temp', engine, if_exists='replace', index=False, schema='songs')

if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)