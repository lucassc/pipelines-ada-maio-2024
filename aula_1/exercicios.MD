# Exercícios de fixação

## Exercício 1: Criando e Gerenciando Branches

**Objetivo:** Criar uma nova branch no repositório e fazer uma pequena alteração no código.

1. Acesse seu repositório no Azure DevOps.
2. Na aba "Repos", selecione "Branches".
3. Clique em "New Branch".
4. Dê um nome para a nova branch, por exemplo, `feature/exercicio1`.
5. Selecione a branch base, que geralmente é a `main` ou `master`.
6. Clique em "Create branch".
7. No seu editor de código local, faça checkout para a nova branch:
   ```bash
   git checkout feature/exercicio1
   ```
8. Faça uma pequena alteração em algum arquivo de código.
9. Adicione e comite a alteração:
   ```bash
   git add .
   git commit -m "Alteração para exercício 1"
   ```
10. Faça push da nova branch para o repositório remoto:
    ```bash
    git push origin feature/exercicio1
    ```

**Validação:** Verifique no Azure DevOps se a nova branch foi criada e se a alteração aparece corretamente.

## Exercício 2: Criando um Pull Request

**Objetivo:** Criar um pull request (PR) para mesclar a branch criada no exercício 1 com a branch principal.

1. No Azure DevOps, acesse "Repos" e depois "Pull Requests".
2. Clique em "New Pull Request".
3. Selecione a branch `feature/exercicio1` como a source e a `main` (ou `master`) como o target.
4. Adicione um título e uma descrição para o PR.
5. Selecione revisores, se necessário.
6. Clique em "Create".

**Validação:** O PR deve aparecer na lista de pull requests pendentes.

## Exercício 3: Revisando e Aprovando um Pull Request

**Objetivo:** Revisar, aprovar e completar um pull request.

1. Na seção de pull requests do Azure DevOps, selecione o PR criado no exercício 2.
2. Revise as alterações clicando em "Files" e verificando o diff.
3. Adicione comentários, se necessário.
4. Clique em "Approve" para aprovar o PR.
5. Após a aprovação, clique em "Complete" para mesclar a branch.
6. Confirme as opções de mesclagem e clique em "Complete merge".

**Validação:** A branch `feature/exercicio1` deve ser mesclada na branch principal e o PR deve estar fechado.
