# Time to angle
> Uma API para obter os ângulos entre os dois ponteiros do relógio.


O objetivo desta API é sobre o desafio de demonstrar minha experiência e conhecimento como
desenvolvedor de back-end. Fornecendo dois argumentos (1: hora; 2: minutos), o programa retornará o ângulo entre os dois ponteiros.


## instalação

Windows & Linux:

```sh
git clone https://github.com/DevVans/ApiAnguloRelogio
```

### executar o arquivo "model.py"

```
### Executar

- precisa instalar python
- precisa instalar o postgresql
- edite o arquivo kernel-raw.json e coloque seu Usuario, Password, Host e Databse que você usará no seu postgresql
```sh
cd src
python -m venv envi
envi\\Scripts\\activate
pip install -r requeriments.txt
python app.py

```

## Exemplo de uso

```sh
curl http://localhost:5000/rest/relogio/{hour}/{minutes=0}
```
Ver todas as solicitações
```sh
curl http://localhost:[port]/queries
```

## Resultado

```sh
{"angle":int angle}
```



