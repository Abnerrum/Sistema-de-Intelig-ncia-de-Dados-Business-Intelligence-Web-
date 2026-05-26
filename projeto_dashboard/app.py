import os
import pandas as pd
import json
import plotly
import plotly.express as px
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from database import get_db_connection

app = Flask(__name__)
app.secret_key = 'chave_secreta_dashboard'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Garantir que a pasta de upload existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        session['user'] = user['username']
        return redirect(url_for('dashboard'))
    else:
        flash('Usuário ou senha incorretos!', 'danger')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))

    dia = request.args.get('dia')
    mes = request.args.get('mes')
    ano = request.args.get('ano')

    conn = get_db_connection()
    query = "SELECT * FROM vendas WHERE 1=1"
    params = []

    if dia: query += " AND DAY(data_venda) = %s"; params.append(dia)
    if mes: query += " AND MONTH(data_venda) = %s"; params.append(mes)
    if ano: query += " AND YEAR(data_venda) = %s"; params.append(ano)

    df = pd.read_sql(query, conn, params=params)
    conn.close()

    if not df.empty:
        total_vendas = f"R$ {df['valor'].sum():,.2f}"
        qtd_registros = len(df)
        media = f"R$ {df['valor'].mean():,.2f}"
        top_prod = df['produto'].mode()[0]
        
        # Gráficos
        fig_vendas = px.line(df.groupby('data_venda')['valor'].sum().reset_index(), 
                             x='data_venda', y='valor', title='Vendas por Período')
        graph_json = json.dumps(fig_vendas, cls=plotly.utils.PlotlyJSONEncoder)
        
        fig_pizza = px.pie(df, names='produto', values='valor', title='Vendas por Produto')
        pizza_json = json.dumps(fig_pizza, cls=plotly.utils.PlotlyJSONEncoder)
    else:
        total_vendas = "R$ 0,00"; qtd_registros = 0; media = "R$ 0,00"; top_prod = "N/A"
        graph_json = None; pizza_json = None

    return render_template('dashboard.html', 
                           total_vendas=total_vendas, qtd_registros=qtd_registros,
                           media=media, top_prod=top_prod,
                           graph_json=graph_json, pizza_json=pizza_json,
                           dados=df.to_dict(orient='records'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        df = pd.read_excel(filepath)
        conn = get_db_connection()
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute("INSERT INTO vendas (produto, valor, data_venda) VALUES (%s, %s, %s)",
                           (row['produto'], row['valor'], row['data_venda']))
        conn.commit()
        conn.close()
        flash('Dados importados com sucesso!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/exportar')
def exportar():
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM vendas", conn)
    conn.close()
    path = os.path.join(app.config['UPLOAD_FOLDER'], 'relatorio.xlsx')
    df.to_excel(path, index=False)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)