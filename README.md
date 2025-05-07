# AWS Glue, Athena e Terraform - Data Lake

Este repositório contém a implementação de um Data Lake usando AWS Glue e Athena, com o auxílio de Terraform para automação de infraestrutura.

**⚠️ Importante:** A automação usando Terraform **ainda não foi testada**. O código foi preparado para criar os recursos necessários na AWS, mas pode ser necessário fazer ajustes dependendo do ambiente e das permissões da sua conta AWS.

## 🚀 Objetivo

- **Automação de infraestrutura**: Usando Terraform para criar os recursos necessários no AWS.
- **Processamento de dados**: Usando AWS Glue para transformar dados e armazená-los no S3 em formato Parquet.
- **Consultas no Data Lake**: Usando Athena para consultar os dados transformados.

## 📂 Estrutura do Repositório

- **`docs/`**: Documentação detalhada do projeto, incluindo explicações e exemplos.
- **`terraform/`**: Arquivos Terraform para criar recursos na AWS.
- **`scripts/`**: Scripts do Glue para transformar dados.
- **`datasets/`**: Conjunto de arquivos CSV usados no processo ETL.
- **`imgs/`**: Imagens para ilustrar a arquitetura e o fluxo de dados.

## ⚙️ Como Usar

1. **Executar Terraform**: 
    - Suba os arquivos `.tf` para sua conta AWS.
    - Execute `terraform init` para inicializar e `terraform apply` para criar os recursos.
    - **Atenção**: Não testamos a execução do Terraform. Certifique-se de revisar o código antes de rodar no seu ambiente.
   
2. **Executar AWS Glue**:
    - Acesse o AWS Glue Console e execute os Jobs definidos nos scripts Python.
   
3. **Consultar com Athena**:
    - Utilize o Athena para executar consultas SQL nos dados armazenados no S3.

## 📚 Documentação

Para mais detalhes, consulte a documentação em `docs/`.

- [Visão geral](docs/overview.md)
- [Arquitetura](docs/architecture.md)
- [Configuração e execução](docs/setup.md)
- [Exemplos de consultas Athena](docs/examples/athena-queries.md)
- [Exemplo de script de Glue Job](docs/examples/glue-job-script.md)

## 🛠️ Requisitos

- Terraform 1.x
- AWS CLI configurado
- Conta AWS com permissões para criar recursos do Glue, S3 e IAM

## 📄 Licença

Este repositório está sob a MIT LICENSE