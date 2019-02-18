# Ajeita a postura

[![Python 3.6](https://img.shields.io/badge/Python-3.5+-blue.svg)](https://www.python.org/downloads/release/python-360/)

Esse bot é feito pra te ajudar a ajeitar a sua postaura enquanto joga ou passa um tempo no discord.

- Pode ser chamado via comando no chat
- Pode rodar um audio aleatorio a cada x minutos

## Vamos lá!
Nas instruções abaixo você vai encontra como configurar e deployar no Heroku

### Requisitos

- [Heroku account](http://heroku.com)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### Configurações
##### Codigo
- Para rodar o bot, primero você tem que [criar um bot](https://discordpy.readthedocs.io/en/rewrite/discord.html) e pegar seu respectivo TOKEN.
- Para aplicar seu token no codigo, abra o arquivo `config.py` e preencha a variavel `TOKEN`.
- A variavel `ENABLEAUTOMESSAGE` vai determinar se o bot vai entrar a cada x minutos e tocar uma mensagem. Use `True` para habilitar e `False` para desabilitar.
- As variaveis `INTERVALMIN` e `INTERVALMAX` vão determinar um intervalo que será usado pra escolher um tempo aleatório que será usado pelo bot pra escolher quando passar pelas salas.

```python
TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ENABLEAUTOMESSAGE=True
INTERVALMIN=1800
INTERVALMAX=3600
```
##### Vozes
Para adicionar as vozes crie uma pasta chamada `audios` dentro da pasta do projeto e adicione seus arquivos `.mp3` la dentro.
O nome do arquivo será usado como parametro para chamar a voz e **não pode conter espaços**.

### Como fazer o deploy
Após baixar o código e alterar tudo o que for necessário e instalar o heroku CLI na sua maquina, rode os seguintes comandos.

##### Inicialize o repositório e crie o projeto no Heroku setando o buildpack. Isso instalará todas as dependencias do sistema 

```sh
$ git init
$ heroku create --buildpack heroku/python
$ heroku buildpacks:add https://github.com/git-yuka/heroku-libopus.git
$ heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
```

##### Envie o código para o heroku para fazer o deploy
```sh 
$ git add .
$ git commit -m "first deploy"
$ git push heroku master
```
##### Coloque o script pra rodar e acompanhe os logs
```
$ heroku ps:scale worker=1
$ heroku logs --tail
```

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

