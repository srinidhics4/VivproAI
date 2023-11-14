import sys
import pandas as pd
from sqlalchemy import create_engine

def main(file_path):
    songs_df = pd.read_json(file_path)
    engine = create_engine(
    'postgresql+psycopg2://postgres:password@127.0.0.1:5432/postgres')
    
    # Drop old table and create new empty table
    # engine.execute
    songs_df.to_sql('songs', engine, if_exists='replace', index=False, schema='songs')

if __name__ == '__main__':
    file_path = "playlist.json" #sys.argv[1]
    main(file_path)