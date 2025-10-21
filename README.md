# GrandeBIAPI
GrandeBIAPI

```bash
# Clone this repository
$ git clone https://github.com/JoaoVLima/GrandeBIAPI.git

# Go into the repository
$ cd GrandeBIAPI

# Create a venv (Virtual Enviroment)
$ python3 -m venv venv

# Activate the venv
$ source venv/bin/activate  # (Unix)
$ .\venv\Scripts\activate   # (Windows)
    
# Install dependencies
$ pip install -r requirements.txt

# Generate a new Django Secret Key
$ python3 generate_secrets.py
    
# Generate a new Django Models and the sqlite database
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# Run the app
$ python3 manage.py runserver
```

python3 manage.py compilemessages
django-admin makemessages -a
django-admin makemessages -l pt-BR
django-admin makemessages -l en




Requisitos

BI
Carregamento rapido das paginas
Informação as realtime as possible

API jwt

Puxar dados do sistemas dos clientes
Linkar dados de sistemas diversos

Crontab
00:30 Calculo Mes atual
01/mes 00:45 Calculo Mes anterior
x:00 Calculo dia atual
00:15 Calculo dia anterior

Pagina do Grupo
	Mensal
	Diaria
Pagina da Empresa
	Mensal
	Diaria




Definir os dados que eu quero mostrar
* Mensal
    * Card top
        * Nome do grupo ou empresa
        * Mes
        * Quando a pagina foi calculada
            * Data e hora do primeiro e ultimo atendimento
    * Faturamento (Valor Real)
        * Comparar com o mes anterior
            * Usar a projeção de faturamento caso seja o mes atual
        * Comparar com o mesmo mes do ano passado
            * Usar a projeção de faturamento caso seja o mes atual
        * Média Diaria
        * Projeção de faturamento
        * Mostrar faturamento por dias e linha de tendencia
    * Ticket Médio (Valor Real)
        * Comparar com o mes anterior
        * Comparar com o mesmo mes do ano passado
    * Atendimentos (Valor Inteiro)
    * O.S. abertas por qual sistema (Valor Inteiro)
    * Empresas
        * Informacoes da Empresa (Valor String)
        * Faturamento (Valor Real)
        * QTDClientes (Valor Inteiro)
    * O.S. por Tipo de OS (Valor String)
    * Distribuição por Tipo de produto vendido (Valor Real)
    * Top 10 Produtos/Serviços mais vendidos
* Diario
    * Card top
        * Nome do grupo ou empresa
        * dia
        * Quando a pagina foi calculada
            * Hora do primeiro e ultimo atendimento
    * Faturamento (Valor Real)
        * Comparar com o dia anterior
            * Usar a projeção de faturamento caso seja o dia atual
        * Comparar com o mesmo dia do ano passado
            * Usar a projeção de faturamento caso seja o dia atual
        * Média Hora
        * Projeção de faturamento
        * Mostrar faturamento por dias e linha de tendencia
    * Ticket Médio (Valor Real)
        * Comparar com o dia anterior
        * Comparar com o mesmo dia do ano passado
    * Atendimentos (Valor Inteiro)
    * O.S. abertas por qual sistema (Valor Inteiro)
    * Funcionarios
        * Informacoes do funcionario (Valor String)
        * Faturamento (Valor Real)
        * Clientes (Valor Inteiro)
    * O.S. por Tipo de OS (Valor String)
    * Distribuição por Tipo de produto vendido (Valor Real)
    * Top 10 Produtos/Serviços mais vendidos
