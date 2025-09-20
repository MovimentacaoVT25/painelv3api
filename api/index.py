import sys
import os

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import app

# Esta é a função que o Vercel irá chamar
def handler(request):
    return app(request.environ, lambda status, headers: None)
