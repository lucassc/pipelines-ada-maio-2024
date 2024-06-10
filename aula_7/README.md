# Aula 7

| Paginas                  |
| ------------------------ |
| [Links](./links_aula.md) |

## Comandos

No Jenkins, especialmente quando você está definindo pipelines usando um `Jenkinsfile`, há uma variedade de comandos que você pode usar. Aqui estão alguns dos comandos mais comuns:

### Comandos Básicos

1. **sh**:

   - Executa comandos de shell. É usado principalmente para executar scripts ou comandos do sistema operacional.

   ```groovy
   sh 'echo "Hello, World!"'
   ```

2. **echo**:
   - Imprime uma mensagem no console de saída.
   ```groovy
   echo 'Hello, World!'
   ```

### Comandos para Controle de Fluxo

3. **input**:

   - Pausa o pipeline e espera por uma entrada manual.

   ```groovy
   input 'Aprovar deploy?'
   ```

4. **timeout**:
   - Define um limite de tempo para uma etapa ou bloco.
   ```groovy
   timeout(time: 5, unit: 'MINUTES') {
       sh 'sleep 10'
   }
   ```

### Comandos para Manipulação de Arquivos e Ambientes

5. **readFile**:

   - Lê o conteúdo de um arquivo.

   ```groovy
   def content = readFile 'myfile.txt'
   ```

6. **writeFile**:
   - Escreve o conteúdo em um arquivo.
   ```groovy
   writeFile(file: 'myfile.txt', text: 'Hello, World!')
   ```

### Comandos para Gerenciamento de Etapas e Stages

7. **stage**:

   - Define uma nova etapa no pipeline.

   ```groovy
   stage('Build') {
       sh 'mvn clean install'
   }
   ```

8. **parallel**:
   - Executa várias etapas em paralelo.
   ```groovy
   parallel(
       firstBranch: {
           sh 'echo "First branch"'
       },
       secondBranch: {
           sh 'echo "Second branch"'
       }
   )
   ```

### Comandos para Manipulação de Jobs e Pipelines

9. **build**:

   - Dispara outro job ou pipeline.

   ```groovy
   build job: 'another-job'
   ```

10. **catchError**:
    - Captura erros de uma etapa específica.
    ```groovy
    catchError {
        sh 'exit 1'
    }
    ```

### Comandos para Publicação e Relatórios

11. **junit**:

    - Publica resultados de testes JUnit.

    ```groovy
    junit 'target/surefire-reports/*.xml'
    ```

12. **archiveArtifacts**:

    - Arquiva artefatos para serem usados posteriormente.

    ```groovy
    archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
    ```

13. **publishHTML**:
    - Publica relatórios HTML.
    ```groovy
    publishHTML([reportDir: 'reports', reportFiles: 'index.html', reportName: 'HTML Report'])
    ```
