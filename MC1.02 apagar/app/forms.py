from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.models import Competicao

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