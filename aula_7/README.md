# Aula 7

| Paginas                  |
| ------------------------ |
| [Links](./links_aula.md) |

## Conteúdo

Siga o passo a passo no material didático, [ADA: Jenkins](https://lms.ada.tech/student/topics/by-class-id/109466b6-f9c2-4aaa-861e-ba5c3edee4cb/by-module-id/7e4fa28a-be7b-4b00-95e1-2c8e2c8557f6), para rodar o seu Jenkins. Durante a aula utilizamos a instalação com Docker

### Docker

```bash
docker volume create jenkins_home

docker container run --name jenkins -d --restart=always -p 8080:8080 -p 50000:50000 -u 0 -v jenkins_home:/var/jenkins_home jenkins/jenkins

## Senha inicial

docker container exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Pipeline com código no GitHub

Para a criação de uma pipeline confira o PDF CreatePipelineJobforGitHubRepositoryinJenkins.pdf com o passo a passo.

### Comandos

Para ver mais comendas, confira a [página aqui](./jenkins-commands.md).
