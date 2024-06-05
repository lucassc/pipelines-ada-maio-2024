# Projeto Final: Pipelines de CI/CD para Detecção de Fraudes Bancárias

## Contexto

Continuando a evolução do nosso sistema de detecção de fraudes bancárias, agora é essencial focar na automação dos processos de desenvolvimento e operação. O objetivo é implementar um pipeline robusto de integração contínua (CI) e entrega contínua (CD) para automatizar testes, builds e deploys, garantindo assim um ciclo de vida de desenvolvimento ágil e seguro.

## Objetivo

Implementar um pipeline de CI/CD utilizando a ferramenta que você preferir para automatizar o processo de integração, teste, build e deployment da aplicação de detecção de fraudes bancárias.

## Requisitos

1. **Integração e Entrega Contínua**:

- Configurar as pipelines que execute testes automáticos, build da imagem Docker e push para um registro de containers.
- Implementar gatilhos de build baseados em mudanças no repositório Git.
- Implantar a aplicação no ambiente (Kubernetes, AWS, Azure, Container Apps. Você pode escolher onde o deploy será realizado).
- Configurar as pipelines que execute validações e deploy da infraestrutura.

2. **Documentação**:

- Preparar uma documentação explicando cada parte do pipeline.
- Incluir instruções detalhadas sobre como configurar e executar os pipelines em ambientes de desenvolvimento e produção.

## Opcional

- Bloquear deploy até que seja aprovado. O aprovador pode ser você mesmo.
- Enviar notificação para alguma ferramenta (Teams, Slack, WhatsApp, ...) quando um deploy finalizar, com falha ou sucesso.
- Deploy para mais de um ambiente
- Integrar SonarQube no pipeline para análise contínua da qualidade do código.

## Entrega

Os alunos deverão fornecer o código fonte no GitHub com todos os arquivos de configuração do CI/CD, além de uma documentação detalhada do projeto.
