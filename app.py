from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<marquee>Aluno Helio do MBA data engeneering da IMPACTA, LAB DEVOPS</marquee>"

if __name__ == '__main__':
    app.run()