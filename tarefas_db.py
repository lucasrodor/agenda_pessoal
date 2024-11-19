import sqlite3 as sql

DB_NAME = 'tarefas.db'

def get_db():
    """Retorna uma conexão com o banco de dados."""
    conn = sql.connect(DB_NAME)
    conn.row_factory = sql.Row
    return conn

def init_db():
    """Cria o banco de dados e a tabela se ainda não existirem."""
    conn = get_db()
    cur = conn.cursor()

    # Cria a tabela somente se não existir
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        prioridade TEXT CHECK(prioridade IN ('Baixa', 'Média', 'Alta')) NOT NULL,
        data_execucao TEXT NOT NULL,
        horario_execucao TEXT NOT NULL,
        status TEXT CHECK(status IN ('Pendente', 'Concluída', 'Cancelada')) DEFAULT 'Pendente',
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        data_conclusao TEXT
    )
    ''')
    conn.commit()
    conn.close()
