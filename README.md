Sistema de Gerenciamento de Segurança das Indústrias Wayne
Visão Geral
Este projeto é um Sistema de Gerenciamento de Segurança desenvolvido para as Indústrias Wayne. Ele permite o controle de acesso a áreas restritas das instalações, o gerenciamento de recursos internos, como equipamentos e veículos, e a visualização de dados relevantes em um painel (dashboard). O sistema implementa autenticação e autorização de usuários para diferentes tipos de perfis, garantindo que apenas pessoas autorizadas possam acessar áreas específicas e gerenciar recursos.

Funcionalidades
Autenticação e Autorização de Usuários

Login seguro de usuários por e-mail e senha.
Três perfis de usuário: Funcionários, Gerentes e Administradores de Segurança.
Cada perfil tem permissões específicas para acessar funcionalidades de gerenciamento de recursos e visualização de dados.
Gerenciamento de Recursos

Interface para gerenciar recursos da empresa, como equipamentos, veículos e dispositivos de segurança.
Recursos possuem os campos nome, tipo, quantidade e descrição.
Painel de Controle Visual (Dashboard)

Exibe dados visuais sobre os recursos disponíveis nas Indústrias Wayne.
Interface para visualizar recursos e gerenciar recursos de forma clara e acessível.

Estrutura do Projeto
├── app.py                    # Aplicação principal Flask
├── users.db                  # Banco de dados SQLite para usuários e recursos
├── templates/
│   ├── base.html 
│   ├── dashboard.html         # Página principal do dashboard         
│   ├── login.htm              # Página de login
│   ├── manage_resources.html  # Gerenciar os recursos
│   ├── resources.html         # Página de gerenciamento de recursos
│   ├── register.html          # pagina para gerenciar os registros  
│   ├── resource_chart.html    # Página para visualização de gráficos de recursos
├── static/
│   ├── style.css              # Estilos customizados para o aplicativo
│   ├── script.js              # JavaScript para interações dinâmicas
└── README.md                  # Este arquivo


Instalação e Execução
Pré-requisitos:
Python 3.x
Biblioteca Flask
SQLite (para o banco de dados)
Como rodar o projeto:
Clone o repositório.

Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows


Instale as dependências:
pip install Flask

Execute o arquivo app.py:
python app.py


Acesse o sistema em http://127.0.0.1:5000/.
