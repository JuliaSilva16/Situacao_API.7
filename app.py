from flask import Flask, jsonify, render_template
# importe para documentacao
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [flask routes] para listar rotas da api

# criar variavel para receber a classe Flask
app = Flask(__name__)

#   documentacao OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/validade_X/<validade_q>/<validade_d_m_a>', methods=['GET'])
def validade_X(validade_q, validade_d_m_a):
    """
    :param validade_q:quantidade de tempo que será calculado (número colocado)
    :param validade_d_m_a:  validade dita em dia,mês e ano
    :return: ele vai retornar  o dia do cadastro(dia atual),a quantidade,se está em dia,mês ou ano, e qual é a validade
    do produto
    """

    try:
        prazo = int(validade_q)
        meses = datetime.today() + relativedelta(months=prazo)
        anos = datetime.today() + relativedelta(years=prazo)
        semanas = datetime.today() + relativedelta(weeks=prazo)
        dias = datetime.today() + relativedelta(days=prazo)
        data_validade = ""

        if validade_d_m_a == 'anos' or validade_d_m_a == 'ano':
            data_validade = anos
        elif validade_d_m_a == 'meses' or validade_d_m_a == 'mes':
            data_validade = meses
        elif validade_d_m_a == 'semanas' or validade_d_m_a == 'semana':
            data_validade = semanas
        elif validade_d_m_a == 'dias' or validade_d_m_a == 'dias':
            data_validade = dias
        else:
            return jsonify({
                'Error': "Erro,coloque apenas dias,semanas,meses,anos"
            })

        return jsonify({
            "Cadastro ": datetime.today().strftime("%d/%m/%Y"),
            "Quantidade de tempo": int(validade_q),
            "Tipo(dia,semana,mes ou ano)": validade_d_m_a,
            "Validade": data_validade.strftime("%d/%m/%Y"),
        })

    except ValueError:
        return jsonify({
            'Error': "Erro"
        })


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)
