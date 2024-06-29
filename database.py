from sqlalchemy import create_engine, text
import pandas as pd


class ConnPostgres:
    def __init__(self) -> None:
        self.db = 'trhone_and_liberty'
        self.host = 'monorail.proxy.rlwy.net'
        self.user = 'postgres'
        self.pwd = 'yAXIOkyKLBJOZKtTKOIOXLQsuxXwNuRH'
        self.port = '30165'

    def conn(self):

        engine = create_engine(f'postgresql://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.db}')

        return engine
    
    def insert_data(self, df):

        df.to_sql('tb_membros_guild_fury_form',con=self.conn(), if_exists='append', index=False)

    def query_email(self):
        # SQL query
        query = """
            SELECT email, nickname
            FROM tb_controle_membros_armada
            ORDER BY data_cadastro DESC LIMIT 1;
        """
        
        # Connect to the database
        engine = self.conn()
        
        # Execute the query and fetch results into a DataFrame
        df = pd.read_sql_query(query, con=engine)
        
        return df
    
    

    
    

    
    