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

        df.to_sql('tb_membros_guild_fury_form_v2',con=self.conn(), if_exists='append', index=False)

    def query_email(self):
        # SQL query
        query = """
            SELECT email, nickname, classe
            FROM tb_membros_guild_fury_form_v2
            ORDER BY data_cadastro DESC LIMIT 1;
        """
        
        # Connect to the database
        engine = self.conn()
        
        # Execute the query and fetch results into a DataFrame
        df = pd.read_sql_query(query, con=engine)
        
        return df
    
    def query_truncate_table(self):
        query = text("""
        TRUNCATE TABLE tb_membros_guild_fury_form_v2;
        """)
        
        # Obter o engine da conexão
        engine = self.conn()
        
        # Usar o engine para obter uma conexão
        with engine.connect() as connection:
            # Iniciar uma transação
            with connection.begin() as transaction:
                try:
                    connection.execute(query)
                    transaction.commit()  # Confirma a transação
                except Exception as e:
                    transaction.rollback()  # Desfaz a transação em caso de erro
                    print(f"Erro ao truncar a tabela: {e}")
    
    

    
    

    
    