# Exercícios de fixação

## Exercício 1: Criando um Pipeline de Build

**Objetivo:** Criar um pipeline de build simples para um projeto de código.

1. Acesse seu projeto no Azure DevOps.
2. Vá para a aba "Pipelines" e clique em "New pipeline".
3. Escolha o local do seu repositório (por exemplo, Azure Repos Git).
4. Selecione o repositório onde está seu código.
5. Escolha a opção "Starter pipeline" para iniciar com um pipeline básico.
6. Edite o arquivo `azure-pipelines.yml` para incluir um job simples. Por exemplo:

```yaml
trigger:
  - main

pool:
  vmImage: "ubuntu-latest"

steps:
  - checkout: none
  - script: echo Hello, World!
    displayName: "Run a one-line script"
```

7. Clique em "Save and run".
8. Confirme as mudanças e aguarde o pipeline executar.

**Validação:** O pipeline deve concluir com sucesso e a saída "Hello, World!" deve aparecer nos logs.

## Exercício 2: Adicionando Testes Automatizados ao Pipeline

**Objetivo:** Adicionar uma etapa de testes ao pipeline de build.

1. Abra o pipeline criado no Exercício 1.
2. Edite o arquivo `azure-pipelines.yml` para adicionar uma etapa de testes. Supondo que você esteja usando testes em Python com `pytest` ([test_app.py](./app/test_app.py)), o arquivo pode ser modificado assim:

```yaml
pool:
  vmImage: "ubuntu-latest"

steps:
  - checkout: self
  - script: |
      pip install -r requirements.txt
      pip install pytest
      pytest
    displayName: "Run tests"
```
