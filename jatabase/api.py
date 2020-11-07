import os
from pprint import pprint as pp
import toml
import psycopg2 as PSQL

SECRETS = toml.load(os.path.join(os.path.dirname(__file__), "config", "secrets.toml"))["general"]
CONFIG = toml.load(os.path.join(os.path.dirname(__file__), "config", "config.toml"))["general"]

class Jatabase:
    def __init__(self):
        self.conn = PSQL.connect(
            database=CONFIG["database"],
            user=SECRETS["user"],
            password=SECRETS["password"],
            host=CONFIG["host"],
            port=CONFIG["port"]
        )
    
    def getVersion(self):
        COMMAND = 'SELECT version()'
        return self._run_command(COMMAND)
    
    
    def close(self):
        self.conn.close()
        print("Exited cleanly")
    

    def _run_command(self, command):
        try:
            cur = self.conn.cursor()
            cur.execute(command)
            value = cur.fetchone()
            cur.close()
        except Exception as e:
            print(e)
        
        return value

if __name__ == "__main__":
    db = Jatabase()
    print(db.getVersion())
    db.close()