from traceback import print_tb


class TaErrradoError(Exception):
    pass


def testar():
    raise TaErrradoError('errado!')


try:
    testar()
except TaErrradoError as error:
    print(f'Erro: {error}')