from funcoes_telefone import alterar_user, cadastrar_user, pesquisar_user
from banco_dados import carregar_contatos

print("-------------------------------------------")
print("---------------LISTA TELEFONICA------------")
print("-------------------------------------------")

#depois concertar.
comando = 'continue'

while comando != "sair":
   try:
      comando = input("\033[36mdigite sua opção: CADASTRAR, PESQUISAR, ALTERAR(PARA SAIR, DIGITE SAIR): \033[m").lower().strip()
   
   except KeyboardInterrupt:
      print('-- ATÉ LOGO! --')
      break
   else:
      if comando == "cadastrar":
         try:
            cadastrar_user()
         except KeyboardInterrupt:
            print('-- ATÉ LOGO!  --')
            break

      if comando == 'pesquisar':
         lista_contatos = carregar_contatos() #LISTAR -> ponteiro que contem os dados do arquivo na memoria
         pesquisar_user(lista_contatos) #função que lista todos os usuarios.
      
      if comando == "alterar":
         try:
            lista_contatos = carregar_contatos() #LISTAR -> ponteiro que contem os dados do arquivo na memoria
            alterar_user(lista_contatos) #função para alterar dados do usuario.
         except KeyboardInterrupt:
            print('-- ATÉ LOGO!  --')
            break