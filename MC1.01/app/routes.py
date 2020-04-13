from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import CompeticaoForm
from app.models import Competicao

@app.route('/')
@app.route('/index')
def index():
    competicao = {'competicao': 'Placard'}
    return render_template('index.html', title='Home', competicao=competicao)

@app.route('/competicao', methods=['GET', 'POST'])
def competicao():
    form = CompeticaoForm()
    if form.validate_on_submit():
        flash('Login requested for id = {}, nome = {}'.format(
            form.id.data, form.nome.data))
        
        competicao = Competicao(id=form.id.data, nome=form.nome.data)
        #FAZER UM IF para ver se id e nome existe na bd
        flash('Congratulations, you are now a registered competicao!')
        db.session.add(competicao)
        db.session.commit()
        
    return render_template('competicao.html', title='Gravar', form=form)


@app.route('/vercompeticao', methods=['GET', 'POST'])
def vercompeticao():
    return render_template('vercompeticao.html', title='Ver Competição', competicao=Competicao.query.all())