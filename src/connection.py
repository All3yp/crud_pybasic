import psycopg2

class Connection:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print('Connection successful')
        except Exception as e:
            print(f'An error has occurred while connecting to the database.')
            print(f'Error: {e}')
    
    def disconnect(self):
        try:
            self.connection.close()
            print('Connection closed')
        except Exception as e:
            print(f'An error has occurred while disconnecting to the database.')
            print(f'Error: {e}')
    
    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Query executed successfully')
        except Exception as e:
            print(f'An error has occurred while executing the query.')
            print(f'Error: {e}')
    
    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except Exception as e:
            print(f'An error has occurred while fetching the data.')
            print(f'Error: {e}')
