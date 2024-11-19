### **README: Projeto - Agenda Pessoal**

---

## **Descrição do Projeto**

O projeto é uma aplicação de gerenciamento de tarefas desenvolvida com **Flask**, **SQLite** e **Bootstrap**, projetada para facilitar a organização pessoal. A aplicação permite adicionar, editar, excluir e categorizar tarefas em **Pendentes**, **Concluídas** e **Canceladas**, com ordenação baseada na prioridade. Além disso, inclui funcionalidades de limpeza da agenda com confirmação e um design responsivo e intuitivo.

---
## **Desenvolvido por:**

Lucas Rodor - Estudante do 2º semestre de Ciência de Dados e Inteligência Artificial | IBMEC - DF
E-mail: lucasgomessr10@gmail.com
Linkedin: [Lucas Rodor](linkedin.com/in/lucasrodor)
Github: [Lucas Rodor](github.com/lucasrodor)

## **Funcionalidades**

1. **Gerenciamento de Tarefas:**
   - Adicionar novas tarefas com nome, descrição, prioridade, data e horário de execução.
   - Editar informações das tarefas existentes, incluindo mudança de status.
   - Excluir tarefas individualmente com confirmação via modal.

2. **Separação por Status:**
   - **Pendentes**: Tarefas ainda a serem realizadas.
   - **Concluídas**: Tarefas finalizadas.
   - **Canceladas**: Tarefas descartadas.

3. **Ordenação por Prioridade:**
   - Alta prioridade (primeiro), seguida de média e baixa.

4. **Limpeza de Agenda:**
   - Limpar todas as tarefas de uma vez com confirmação via modal.

5. **Design Intuitivo:**
   - Interface responsiva com Bootstrap.
   - Ícones para status das tarefas:
     - **Pendente**: Relógio ⏰.
     - **Concluída**: Check ✅.
     - **Cancelada**: X ❌.

---

## **Tecnologias Utilizadas**

### **Backend:**
- **Python** com Flask.
- Banco de dados **SQLite** para armazenamento de tarefas.

### **Frontend:**
- **Bootstrap 5** para estilização e responsividade.
- **Bootstrap Icons** para ícones visuais.

### **Outras Tecnologias:**
- **HTML5** e **CSS3**.
- **Jinja2** para templates dinâmicos.

---

## **Requisitos do Sistema**

- **Python 3.8+**
- **Pip** para gerenciamento de pacotes.
- **SQLite** embutido no Python.

---

## **Instalação e Configuração**

### **Passo 1: Clonar o Repositório**

```bash
git clone https://github.com/lucasrodor/agenda_pessoal.git
cd repositorio_desejado
```

### **Passo 2: Criar o Ambiente Virtual**

```bash
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

### **Passo 3: Instalar Dependências**

```bash
pip install -r requirements.txt
```

### **Passo 4: Inicializar o Banco de Dados**

```bash
python -c "from tarefas_db import init_db; init_db()"
```

---

## **Uso**

### **Executar o Servidor**

Inicie a aplicação localmente:

```bash
python app.py
```

O servidor estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Navegação no Sistema**

### **Página Inicial**
- Exibe as tarefas separadas por **Pendentes**, **Concluídas** e **Canceladas**.
- Ordena as tarefas por prioridade dentro de cada grupo.

### **Adicionar Tarefas**
- Acesse o botão "Adicionar Nova Tarefa".
- Preencha os campos obrigatórios:
  - Nome
  - Descrição
  - Prioridade
  - Data e horário de execução.

### **Editar Tarefas**
- Clique no botão "Editar" em uma tarefa.
- Atualize os dados ou altere o status da tarefa.

### **Excluir Tarefas**
- Clique no botão "Excluir" em uma tarefa.
- Confirme a exclusão no modal.

### **Limpar Agenda**
- Clique no botão "Limpar Agenda".
- Confirme a limpeza para remover todas as tarefas.

---

## **Customização**

### **Estilos**
- Modifique o arquivo `static/styles.css` para alterar cores, margens ou layout.

### **Banco de Dados**
- O banco de dados (`tarefas.db`) pode ser exportado ou importado para uso em outros sistemas SQLite.

---

## **Possíveis Problemas e Soluções**

1. **O botão "Limpar Agenda" não funciona**:
   - Verifique se os scripts do Bootstrap estão corretamente incluídos no `layout.html`.

2. **O modal de confirmação não abre**:
   - Certifique-se de que o atributo `data-bs-target` aponta para o ID correto do modal.

3. **O banco de dados está vazio**:
   - Execute `python -c "from tarefas_db import init_db; init_db()"` para inicializá-lo.

---

## **Contribuições**

Sinta-se à vontade para contribuir! Crie um pull request ou abra uma issue no repositório.

---

## **Licença**

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo.

---

Agora a **Sua agenda personalizada** está configurado e pronto para ser usado como sua ferramenta de organização diária! 🚀 Se tiver dúvidas ou sugestões, entre em contato! 😊