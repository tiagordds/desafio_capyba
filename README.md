# Desafio Capyba

  Este projeto foi desenvolvido para o desafio da Capyba

# Intruções

  1. Instale o python 3.11.2, no link: https://www.python.org/downloads/release/python-3112/. Versões superiores devem funcionar, mas não foram testadas
  2. Clone e extraia este repositório
  3. Abra a pasta do repositório com a IDE de sua preferência
  4. Execute os seguintes comandos:
     
     Para a criação de um ambiente virtual:
     ```
     python -m venv venv
     ```

     Instale os pacotes necessários:
     ```
     pip install -r requirements.txt
     ```

     Em seguida, execute:
     ```
     python manage.py makemigrations
     python manage.py migrate
     python manage.py runserver
     ```
     O projeto pode ser acessado por meio de seu localhost (localhost:8000).
     Para a criação de um usuário com acesso à área administrativa do django, execute o comando:
     ```
     python manage.py createsuperuser
     ```
     Siga as instruções e use as credencias para ter acesso à área administrativa, onde você poderá criar posts, pages e setups para o blog.

# Funcionalidades

  Criação de posts, com acesso ao django summernote e code view, podendo inserir HTML diretamente no corpo do post, imagens para cover
  e também imagens dentro do post.
  
  Edição de layouts com páginas estáticas e novos links para acesso.
  
  Slugs e URLs dinâmicas.
  
  Uma pesquisa simples que procura o input em toda a base da dados de posts, tags, categorias e autores.

  Através do link (localhost:8000/register) você pode criar usuários para testes da API.

# Layout

  A branch de test deste repositório contém uma versão simplificada do projeto, mas com textos gerados pelo https://loripsum.net , 
  com o objetivo de mostrar o layout final do blog. Exemplos: 
  
  ![layout_completo](https://github.com/tiagordds/desafio_capyba/assets/132831208/cba48dc8-6f6f-42a6-b88a-4510417d44a1)

  ![layout_completo2](https://github.com/tiagordds/desafio_capyba/assets/132831208/65c761e0-7e31-42f2-aeb1-5160cc3458ca)

# API

  As funcionalidades da API não estão totalmente desenvolvidas e integradas até o momento. A API recebe as informações de usuários 
  e é possível realizar testes para verificação das informações, tais como usário, senha e token de autorização. Os testes foram desenvolvidos
  no VSCode com uso da extensão do Rest Client e estão disponibilizados no módulo test.rest. Ressalta-se que é necessária a utilização
  de uma extensão compatível.
 
  


  
  
