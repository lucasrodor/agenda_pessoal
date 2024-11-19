from flask import Flask, render_template, request, redirect, url_for, flash
from tarefas_db import init_db, get_db

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Inicializa o banco de dados
init_db()

@app.route('/')
@app.route('/')
def index():
    """Página inicial que lista as tarefas separadas por status."""
    conn = get_db()
    cur = conn.cursor()

    # Seleciona e organiza as tarefas por status e prioridade
    cur.execute("""
        SELECT * FROM tarefas 
        WHERE status = 'Pendente'
        ORDER BY 
            CASE prioridade 
                WHEN 'Alta' THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
            END
    """)
    pendentes = cur.fetchall()

    cur.execute("""
        SELECT * FROM tarefas 
        WHERE status = 'Concluída'
        ORDER BY 
            CASE prioridade 
                WHEN 'Alta' THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
            END
    """)
    concluidas = cur.fetchall()

    cur.execute("""
        SELECT * FROM tarefas 
        WHERE status = 'Cancelada'
        ORDER BY 
            CASE prioridade 
                WHEN 'Alta' THEN 1
                WHEN 'Média' THEN 2
                WHEN 'Baixa' THEN 3
            END
    """)
    canceladas = cur.fetchall()

    conn.close()
    return render_template('index.html', pendentes=pendentes, concluidas=concluidas, canceladas=canceladas)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    """Adiciona uma nova tarefa."""
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prioridade = request.form.get('prioridade')
        data_execucao = request.form.get('data_execucao')
        horario_execucao = request.form.get('horario_execucao')

        # Validação dos campos obrigatórios
        if not nome or not prioridade or not data_execucao or not horario_execucao:
            flash('Nome, Prioridade, Data e Horário de Execução são obrigatórios!', 'danger')
            return redirect(url_for('adicionar'))

        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO tarefas (nome, descricao, prioridade, data_execucao, horario_execucao)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, descricao, prioridade, data_execucao, horario_execucao))
        conn.commit()
        conn.close()

        flash('Tarefa adicionada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Edita uma tarefa existente."""
    conn = get_db()
    cur = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']
        data_execucao = request.form['data_execucao']
        horario_execucao = request.form['horario_execucao']
        status = request.form['status']
        data_conclusao = None if status != 'Concluída' else "Concluído"

        # Validação dos campos obrigatórios
        if not nome or not prioridade or not data_execucao or not horario_execucao:
            flash('Nome, Prioridade, Data e Horário de Execução são obrigatórios!', 'danger')
            return redirect(url_for('editar', id=id))

        cur.execute("""
            UPDATE tarefas
            SET nome = ?, descricao = ?, prioridade = ?, data_execucao = ?, horario_execucao = ?, status = ?, data_conclusao = ?
            WHERE id = ?
        """, (nome, descricao, prioridade, data_execucao, horario_execucao, status, data_conclusao, id))
        conn.commit()
        conn.close()

        flash('Tarefa atualizada com sucesso!', 'success')
        return redirect(url_for('index'))

    cur.execute("SELECT * FROM tarefas WHERE id = ?", (id,))
    tarefa = cur.fetchone()
    conn.close()

    if tarefa:
        return render_template('editar.html', tarefa=tarefa)

    flash('Tarefa não encontrada!', 'danger')
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    """Exclui uma tarefa."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    flash('Tarefa excluída com sucesso!', 'danger')
    return redirect(url_for('index'))

@app.route('/limpar', methods=['POST'])
def limpar_agenda():
    """Limpa todas as tarefas da agenda."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tarefas")
    conn.commit()
    conn.close()

    flash('Agenda limpa com sucesso!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
