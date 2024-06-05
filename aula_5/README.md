# Aula 5

| Paginas                                  |
| ---------------------------------------- |
| [Links](./links_aula.md)                 |
| [Exercícios de fixação](./exercicios.MD) |

## Conteúdo

- [Github Actions](https://docs.github.com/pt/actions)

## Problema

Pedro trabalha no time chamado "Crédito" e precisa de um novo repositório no Azure DevOps. Daniel que trabalha no time de Plataforma será quem irá criar o repositório no padrão correto, com o esqueleto do projeto e pipelines configuradas. Daniel quando for trabalhar no ticket do Pedro irá criar o repositório pela interface do Azure DevOps.

Problemas dessa abordagem:

- O tempo até a criação do repositório é muito grande, por volta de 4 dias.
- A criação e configuração é manual.
- Em caso de erros, o prazo sobre para 7 dias (1 semana e meia).

Pontos importantes:

- O time de plataformas usa GitHub
- O time de plataformas é composto por 7 pessoas que trabalham nos mesmos repositórios do GitHub.

O time de plataformas já está trabalhando em melhorias desse processo. Para evitar erros, eles criaram um código terraform para a criação do repositório. Daniel quando for trabalhar na solicitação precisa rodar o código terraform da sua maquina, assim ele precisa ter acesso ao token do Azure DevOps todas as vezes que for executar.

#### Pontos a serem implementados:

Automação em si:

- Uma pipeline onde Pedro informa o `nome do projeto`, `nome do repositório` e o `grupo` para solicitar a criação de um novo repositório
- A pipeline que roda o código terraform que cria e configura o novo repositório precisa ser aprovada antes da execução

Mantendo o código terraform e a pipeline:

- Como o time tem 7 engenheiros, o repositório no GitHub também precisa de PR para adicionar uma mudança e pipeline de CI

## O que é necessário aprender

### Workflows

- Toda pipeline precisa estar dentro de `.github/workflows`
- [Github Actions: Events that trigger workflows](https://docs.github.com/pt/actions/using-workflows/events-that-trigger-workflows)
- Para ser possível rodar uma pipeline manualmente [workflow_dispatch](https://docs.github.com/pt/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)
- [GitHub Actions: Input types for manual workflows](https://github.blog/changelog/2021-11-10-github-actions-input-types-for-manual-workflows/)

### Github Environment

- Para que o time de plataforma possa aprovar, a pipeline precisa rodar em um `environment`.
- `Environments`, caso nao existam, são criados automaticamente
- É possível definir reviews para um `environment`
- `Secrets` (ex: AZDO_PERSONAL_ACCESS_TOKEN) precisam estar em um `environment` para garantir que ela só será acessada após aprovação
- [Github Actions: Using an environment](https://docs.github.com/pt/actions/deployment/targeting-different-environments/using-environments-for-deployment#using-an-environment)
- Environments são configurados na aba `Settings`

### Azure DevOps Token

- [Azure DevOps Provider: Authenticating using the Personal Access Token](https://registry.terraform.io/providers/microsoft/azuredevops/latest/docs/guides/authenticating_using_the_personal_access_token)

### Código base

Tente implementar os requisitos usando os exemplos abaixo no seu repositório

- [aula_5/terraform](./terraform)
- [aula_5/create-repository.yaml](./create-repository.yaml)
- [aula_5/terraform-ci.yaml](./terraform-ci.yaml)
