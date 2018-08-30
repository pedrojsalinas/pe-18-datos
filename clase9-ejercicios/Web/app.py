from flask import Flask,render_template,request
from wtforms import Form, SelectField, StringField, PasswordField, validators
import pandas as pd
import sqlite3

app = Flask(__name__)


class BuscadorForm(Form):
    query = StringField('', validators=[validators.required()])

@app.route('/',methods=['POST', 'GET'])
def index():
    data = None
    lng = None
    form = BuscadorForm(request.form)
    if request.method == 'POST':
        query=request.form['query']
        if form.validate():
            print("Query:", query)
            conn = sqlite3.connect("instituciones.db")
            df = pd.read_sql("SELECT * FROM educativas", conn)
            data = df[(df['Codigo-AMIE'].str.contains(query.upper(),na=False))][['Nombre-Institucion','Provincia','Tipo-Educacion','Etnia','Numero-estudiantes','Numero-docentes']]
            data = data.to_dict(orient="records")
            lng=len(data)
    return render_template('index.html',form=form,data=data,lng=lng )
