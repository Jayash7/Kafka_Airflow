import psycopg2
#import logging as log
from datetime import datetime 


#log_file_path = f'F:/JD/Docker/kafka_docker_helloworld-master/logs/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# Set up basic logging configuration
'''log.basicConfig(
    level=log.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the format of log messages
    filename=log_file_path#,  # Specify the file to which logs will be written
    #filemode='w'  # Set the file mode to 'w' to overwrite the file if it exists
)'''


class pg_database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname='airflow',  # Default database name
                user='airflow',
                password='airflow',
                #host='172.30.0.2',
                host = 'postgres',
                port='5432'
            )
            self.cur = None
            #log.info("Instance created")
        except Exception as e:
            print("Error connecting to PostgreSQL:", e)
            self.conn = None  # Set self.conn to None if connection fails
            self.cur = None

    # Execute a query
    def instance(self, query):
        #cur = None  # Define cur with a default value
        if self.conn is None:
            print("connection is faild")
        else:
            try:
                self.cur = self.conn.cursor()
                print("___________________________created_____________________________")
                #log.info("___________________________created_____________________________")
                self.cur.execute(query)
                #self.cur.execute("INSERT INTO test (id) VALUES (10)")
                self.conn.commit()
            except Exception as e:
                print("Error executing query:", e)
                #log.info(f"Instance creation faild {e}")
            finally:
                if self.cur is not None:
                    self.cur.close()
                if self.conn is not None:
                    self.conn.close()
                #log.shutdown()
                print("connection closed ")
