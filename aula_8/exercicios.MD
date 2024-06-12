# Exercícios de fixação

## Exercício 1: Configuração do Projeto no SonarCloud

1. Crie uma conta no [SonarCloud](https://www.sonarsource.com/products/sonarcloud/signup/).
2. Adicione um novo projeto no SonarCloud utilizando o repositório fornecido no arquivo `README.md`.

3. Configure o arquivo `sonar-project.properties` com as seguintes informações:
   - `sonar.projectKey`
   - `sonar.organization`
   - `sonar.projectName`
   - `sonar.sources`
   - `sonar.python.coverage.reportPaths`
   - `sonar.python.xunit.reportPath`

## Exercício 2: Integração do SonarCloud com GitHub Actions

1. Utilize o arquivo `ci-python.yaml` para configurar uma pipeline de CI no GitHub Actions.
2. Certifique-se de que a pipeline inclua um passo para executar a análise de código com o SonarCloud.
3. Modifique a pipeline para garantir que os testes definidos no arquivo `test_app.py` sejam executados antes da análise do SonarCloud.
4. Documente os passos realizados e explique como a integração contínua com SonarCloud pode melhorar a qualidade do código.

## Exercício 3: Análise de Resultados no SonarCloud

1. Após configurar a pipeline e executar a análise, acesse o SonarCloud e verifique os resultados da análise do seu projeto.
2. Liste pelo menos três tipos de problemas ou alertas que o SonarCloud pode identificar em seu código.
3. Utilize o arquivo `app.py` para identificar potenciais problemas que poderiam ser reportados pelo SonarCloud.
4. Descreva as ações corretivas que você tomaria para resolver cada um dos problemas identificados.
