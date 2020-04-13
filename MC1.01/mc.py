from app import app, db
from app.models import Jogador, Equipa, Jogo, Competicao

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Jogador': Jogador, 'Equipa': Equipa, 'Competicao': Competicao, 'Jogo': Jogo}