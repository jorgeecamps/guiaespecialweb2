from flask import Flask, render_template


app = Flask(__name__)


# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/onde_ir')
def onde_ir():
    chave_api = "AIzaSyCq23NPS113f_FeDOsuI8MDbQR4qQZS8B8"  # Substitua "SUA_CHAVE_DE_API" pela sua chave real
    return render_template('onde_ir.html')



@app.route('/certificacao_guiaespecial')
def certificacao_guiaespecial():
    return render_template('certificacao_guiaespecial.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/exibir_mensagem')
def exibir_mensagem():
    mensagem = "Enviado com sucesso!"
    return render_template('contato.html', mensagem=mensagem)


# Executando a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)



