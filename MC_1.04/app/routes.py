from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import CompeticaoForm, EquipaForm, JogadorForm, JogoForm, EditCompeticaoForm, DeleteCompeticaoForm
from app.models import Competicao, Equipa, Jogador, Jogo


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
        
    return render_template('competicao.html', title='Grava Competição', form=form)


@app.route('/vercompeticao', methods=['GET', 'POST'])
def vercompeticao():
    return render_template('vercompeticao.html', title='Ver Competição', competicao=Competicao.query.all())


@app.route('/equipa', methods=['GET', 'POST'])
def equipa():
    form = EquipaForm()
    if form.validate_on_submit():
        flash('Login requested for id = {}, nome = {}'.format(
            form.id.data, form.nome.data, form.modalidade.data, form.local.data))
        
        equipa = Equipa(id=form.id.data, nome=form.nome.data, modalidade=form.local.data, local=form.local.data)
        #FAZER UM IF para ver se id e nome existe na bd
        flash('Congratulations, you are now a registered equipa!')
        db.session.add(equipa)
        db.session.commit()
        
    return render_template('equipa.html', title='Grava Equipa', form=form)

@app.route('/verequipa', methods=['GET', 'POST'])
def verequipa():
    return render_template('verequipa.html', title='Ver Equipa', equipa=Equipa.query.all())

@app.route('/jogador', methods=['GET', 'POST'])
def jogador():
    form = JogadorForm()
    if form.validate_on_submit():
        flash('Login requested for id = {}, nome = {}'.format(
            form.id.data, form.nome.data, form.data_nascimento.data, form.nacionalidade.data, form.equipa.data))
        
        jogador = Jogador(id=form.id.data, nome=form.nome.data, data_nascimento=form.data_nascimento.data, nacionalidade=form.nacionalidade.data, equipa=form.equipa.data)
        #FAZER UM IF para ver se id e nome existe na bd
        flash('Congratulations, you are now a registered Jogador!')
        db.session.add(jogador)
        db.session.commit()
        
    return render_template('jogador.html', title='Grava Jogador', form=form)

@app.route('/verjogador', methods=['GET', 'POST'])
def verjogador():
    return render_template('verjogador.html', title='Ver Jogador', jogador=Jogador.query.all())


@app.route('/jogo', methods=['GET', 'POST'])
def jogo():
    form = JogoForm()
    if form.validate_on_submit():
        flash('Login requested for id = {}, nome = {}'.format(
            form.id.data, form.equipa_casa.data, form.equipa_fora.data, form.data.data, form.hora.data, form.local.data))
        
        jogo = Jogo( id=form.id.data, equipa_casa=form.equipa_casa.data, equipa_fora=form.equipa_fora.data, data=form.data.data, hora=form.hora.data, local=form.local.data)
        #FAZER UM IF para ver se id e nome existe na bd
        flash('Congratulations, you are now a registered Jogador!')
        db.session.add(jogo)
        db.session.commit()
        
    return render_template('jogo.html', title='Grava Jogo', form=form)

@app.route('/verjogo', methods=['GET', 'POST'])
def verjogo():
    return render_template('verjogo.html', title='Ver Jogo', jogo=Jogo.query.all())



@app.route('/edit_competicao', methods=['GET', 'POST'])
def edit_competicao():
    form = EditCompeticaoForm()
    if form.validate_on_submit():
        competicao = Competicao.query.get(form.id.data)
        competicao.nome = form.nome.data

        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_competicao'))
    return render_template('edit_competicao.html', title='Edit Competição',form=form)

@app.route('/delete_competicao', methods=['GET', 'POST'])
def delete_competicao():
    form = DeleteCompeticaoForm()
    if form.validate_on_submit():
        competicao = Competicao.query.get(form.id.data)
        db.session.delete(competicao)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('delete_competicao'))
    return render_template('delete_competicao.html', title='Delete Competição',form=form)