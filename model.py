import psycopg2
import json
from datetime import datetime, timezone


class ModelClock:
    def __init__(self):
        self.conn = None
        self.table = 'queries'
        self.kernel = 'kernel.json'
        self.kernelRaw = 'kernel-raw.json'
        self.isDocker = False
        self.checkTable()

    # faz a conexão com o banco de dados
    def connect(self):
        config = self.getConfig()

        self.conn = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password'],
            port=config['port']
        )

    # Adicionar valor
    def insert(self, hour, minute, angle):
        self.connect()
        cursor = self.conn.cursor()  # cursor para manipular a conexão

        # obtenha a hora agora e formate AAAA-MM-DD
        now = datetime.now(timezone.utc)
        date = psycopg2.Date(now.year, now.month, now.day)

        # consulta
        sql = f"INSERT INTO {self.table} (hour, minutes, angle, dates) VALUES ({hour}, {minute}, {angle}, {date});"

        cursor.execute(sql)  # insira a consulta
        self.conn.commit()  # salvar a alteração
        self.conn.close()  # fechar conexão

    def select(self, sql, arg=None):
        self.connect()
        cursor = self.conn.cursor()

        if arg:
            cursor.execute(sql, arg)
        else:
            cursor.execute(sql)

        row = cursor.fetchall()  # extrair resultado

        self.conn.close()  # fechar conexão

        return row

    # verifica se a tabela 'queries' existe, caso não exista irá criá-la
    def checkTable(self):
        self.connect()
        cursor = self.conn.cursor()
        config = self.getConfig()
        sql = """
		SELECT EXISTS(SELECT 1 FROM information_schema.tables 
              WHERE table_catalog=%s AND 
                    table_schema='public' AND 
                    table_name='queries');
		"""
        cursor.execute(sql, (config['database'],))
        tableExist = cursor.fetchone()[0]

        if not tableExist:
            sql = """
			CREATE TABLE queries(
			id SERIAL,
			hour INT,
			minutes INT,
			angle INT,
			dates DATE
			)
			"""
            cursor.execute(sql)
            self.conn.commit()

        self.conn.close()

    # obtenha informações de configuração e retorne o dict com valores
    def getConfig(self):
        file = ''
        if self.isDocker:
            file = open(self.kernel, 'r')
        else:
            file = open(self.kernelRaw, 'r')
        return json.loads(file.read())

