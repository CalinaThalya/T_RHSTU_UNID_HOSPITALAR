[quinta-feira 23:07] Calina Thalya Santana da Silva
import datetime
from multiprocessing import connection
import random
import oracledb
 
complementos = ["predio 101", " Predio Verde ", " cobertura", "Fundos", "Bloco A", "Bloco c", " Bloco B"]
pontos_referencia = ["Próximo à escola", "Perto da praça", "Ao lado do hospital", "Em frente à igreja", "Na esquina"]
 
db = oracledb.connect(user='rm552539', password='130701', dsn='oracle.fiap.com.br/orcl')
cursor = db.cursor()
 
for i in range(1, 1001):
    # Consulta de inserção
    
    ID_UNID_HOSPITAL = 1
NM_UNID_HOSPITALAR = "Rede de Hospitais Somos Todos UM"
NM_RAZAO_SOCIAL_UNID_HOSP = "Somos Todos Um"
DT_FUNDACAO = datetime.date(2022, 1, 1)
NR_LOGRADOURO = random.randint(1, 1000)
DS_COMPLEMENTO_NUMERO = random.choice(complementos)
DS_PONTO_REFERENCIA = random.choice(pontos_referencia)
DT_INICIO = datetime.date(2022, 1, 1)
DT_TERMINO = datetime.date(2023, 8, 31)
DT_CADASTRO = oracledb.Date.today()
NM_USUARIO = "USER"
 
insert_query = '''
    INSERT INTO T_RHSTU_UNID_HOSPITALAR (
        ID_UNID_HOSPITAL,
        NM_UNID_HOSPITALAR,
        NM_RAZAO_SOCIAL_UNID_HOSP,
        DT_FUNDACAO,
        NR_LOGRADOURO,
        DS_COMPLEMENTO_NUMERO,
        DS_PONTO_REFERENCIA,
        DT_INICIO,
        DT_TERMINO,
        DT_CADASTRO,
        NM_USUARIO
    ) VALUES (
        :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11
    )
'''
 
values = (
        ID_UNID_HOSPITAL,
        NM_UNID_HOSPITALAR,
        NM_RAZAO_SOCIAL_UNID_HOSP,
        DT_FUNDACAO,
        NR_LOGRADOURO,
        DS_COMPLEMENTO_NUMERO,
        DS_PONTO_REFERENCIA,
        DT_INICIO,
        DT_TERMINO,
        DT_CADASTRO,
        NM_USUARIO,
    )
 
    # Execute a consulta SQL
cursor.execute(insert_query, values)
 
db.commit()
cursor.close()
db.close()
print("Inserção de dados concluída.")