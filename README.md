# Circulares USP - Crawler
Aplicação para extrair e gerar dados filtrados e acessíveis da API de circulares da USP, disponível [neste link](https://uspdigital.usp.br/mobile/servicos/sptrans/posicoes).

## Instalação
Para instalar o programa, basta possuir uma chave SSH no GitHub e executar o comando de clone abaixo:
```bash
$ git clone git@github.com:Circulares-USP/Crawler.git
```
Após isso, gere uma cópia do .env.sample em um arquivo .env e o edite para os parâmetros de seu interesse:
```bash
$ cp .env.sample .env
```

## Dependências
O programa utiliza algumas dependências do Python em sua execução. Tais dependências estão listadas no arquivo requirements.txt, que é automaticamente carregado na execução da imagem gerada com o Docker.

## Execução
O programa oferece suporte para dois tipos de execução: o de extração de dados e o de recuperação e exibição das informações registradas. Para facilitar o uso dos comandos, utilizamos o plugin `docker compose` do Docker. Os parâmetros de execução estão disponíveis no arquivo .env definido no momento da instalação.

### Crawl
O primeiro modo do programa se refere à extração e registro dos dados da API dos circulares da USP. Seu funcionamento é baseado no perfil `crawl` do docker compose. Para utilizar esse modo, basta executar:
```bash
$ docker compose --profile crawl up
```

### Plot
O segundo modo se refere à exibição das informações registradas localmente por meio de gráficos. Seu funcionamento é baseado no perfil `plot` do docker compose. Para utilizá-lo, basta executar:
```bash
$ docker compose --profile plot up
```

### Notebooks
O programa possui, ainda, um modo de prototipação e experimentação rápida das funções que o compõem a partir de um notebook do Jupyter. Seu intuito é oferecer um modo de apresentação rápida da aplicação e da geração de dados de forma interativa. O funcionamento do programa é baseado no perfil `notebook` do docker compose. Para utilizá-lo, basta executar:
```bash
$ docker compose --profile notebook up
```

## Testes

A aplicação possui alguns testes de unidade de suas principais funções, baseados na biblioteca [PyTest](https://pytest.org). Para testá-la, basta executar o perfil de testes do docker compose, da seguinte forma:
```bash
$ docker compose --profile test up
```

## Contribuições
Para contribuir com esta aplicação, basta gerar um _fork_ dela, adicionar as modificações feitas em uma _branch_ e solicitar um _pull-request_ para o repositório principal. Caso a integridade dos testes não seja afetada e as modificações contribuam positivamente para o projeto, realizaremos um _merge_ das novas funcionalidades.

## Informações

Este projeto foi desenvolvido na disciplina Laboratório de Métodos Ágeis (MAC0472) do IME-USP no segundo semestre do ano de 2022 e não possui quaisquer fins lucrativos.
