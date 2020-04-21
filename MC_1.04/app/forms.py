from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import Competicao, Equipa, Jogador, Jogo

#FORMULÁRIO COMPETIÇÃO

class CompeticaoForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def validate_id(self, id):
        competicao = Competicao.query.filter_by(id=id.data).first()
        if competicao is not None:
            raise ValidationError('Please use a different id.')
    
    def validate_nome(self, nome):
        competicao = Competicao.query.filter_by(nome=nome.data).first()
        if competicao is not None:
            raise ValidationError('Please use a different nome.')

#FIM FORMULÁRIO COMPETIÇÃO

#FORMULÁRIO EQUIPA

class EquipaForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    modalidade = StringField('Modalidade', validators=[DataRequired()])
    local = StringField('Local', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def validate_id(self, id):
        equipa = Equipa.query.filter_by(id=id.data).first()
        if equipa is not None:
            raise ValidationError('Please use a different id.')
    
    def validate_nome(self, nome):
        equipa = Equipa.query.filter_by(nome=nome.data).first()
        if equipa is not None:
            raise ValidationError('Please use a different nome.')
    
    def validate_modalidade(self, modalidade):
        modalidade = Equipa.query.filter_by(modalidade=modalidade.data).first()
        if modalidade is not None:
            raise ValidationError('Please use a different modalidade.')

    def validate_local(self, local):
        equipa = Equipa.query.filter_by(local=local.data).first()
        if equipa is not None:
            raise ValidationError('Please use a different local.')

#FIM FORMULÁRIO EQUIPA


#FORMULÁRIO JOGADOR

class JogadorForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    data_nascimento = StringField('DataNascimento', validators=[DataRequired()])
    nacionalidade = StringField('Nacionalidade', validators=[DataRequired()])
    equipa = StringField('Equipa', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def validate_id(self, id):
        jogador = Jogador.query.filter_by(id=id.data).first()
        if jogador is not None:
            raise ValidationError('Please use a different id.')
    
    def validate_nome(self, nome):
        jogador = Jogador.query.filter_by(nome=nome.data).first()
        if jogador is not None:
            raise ValidationError('Please use a different nome.')

    def validate_data_nascimento(self, data_nascimento):
        jogador = Jogador.query.filter_by(data_nascimento=data_nascimento.data).first()
        if jogador is not None:
            raise ValidationError('Please use a different data nascimento.')
    
    def validate_nacionalidade(self, nacionalidade):
        jogador = Jogador.query.filter_by(nacionalidade=nacionalidade.data).first()
        if jogador is not None:
            raise ValidationError('Please use a different data nascimento.')

    def validate_equipa(self, equipa):
        jogador = Jogador.query.filter_by(equipa=equipa.data).first()
        if jogador is not None:
            raise ValidationError('Please use a different equipa.')

#FIM FORMULÁRIO JOGADOR


#FORMULÁRIO JOGO
class JogoForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    equipa_casa = StringField('Equipa Casa', validators=[DataRequired()])
    equipa_fora = StringField('Equipa Fora', validators=[DataRequired()])
    data = StringField('Data', validators=[DataRequired()])
    hora = StringField('Hora', validators=[DataRequired()])
    local = StringField('Local', validators=[DataRequired()])
    submit = SubmitField('Gravar')

    def validate_id(self, id):
        jogo = Jogo.query.filter_by(id=id.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different id.')
    
    def validate_equipa_casa(self, equipa_casa):
        jogo = Jogo.query.filter_by(equipa_casa=equipa_casa.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different equipa_casa.')

    def validate_equipa_fora(self, equipa_fora):
        jogo = Jogo.query.filter_by(equipa_fora=equipa_fora.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different equipa_fora.')
    
    def validate_data(self, data):
        jogo = Jogo.query.filter_by(data=data.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different data.')

    def validate_hora(self, hora):
        jogo = Jogo.query.filter_by(hora=hora.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different hora.')

    def validate_local(self, local):
        jogo = Jogo.query.filter_by(local=local.data).first()
        if jogo is not None:
            raise ValidationError('Please use a different local.')
    

#FIM FORMULÁRIO JOGO

#EDIT COMPETIÇÃO
class EditCompeticaoForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Submit')

#FIM EDIT COMPETIÇÃO

#DELETE COMPETIÇÃO
class DeleteCompeticaoForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    submit = SubmitField('Submit')

#FIM DELETE COMPETIÇÃO