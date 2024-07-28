# Boston Data Pipeline AWS Project

Bem-vindo ao projeto de Pipeline de Dados de Boston! Este projeto utiliza uma série de ferramentas da AWS para processar e analisar dados de solicitações de serviço da cidade de Boston. O objetivo é criar um pipeline de dados eficiente que extrai, transforma e carrega (ETL) os dados em um formato pronto para análise, ajudando a entender melhor as tendências e padrões das solicitações de serviço na cidade.

## Descrição do Projeto

Este projeto foi desenvolvido para analisar o conjunto de dados de solicitações de serviço 311 de Boston, disponível [aqui](https://data.boston.gov/dataset/311-service-requests). Os dados incluem informações sobre vários tipos de serviços solicitados pelos cidadãos, como problemas com iluminação pública, coleta de lixo e muito mais. O pipeline de dados permite que esses dados sejam coletados, transformados e analisados de forma eficiente, proporcionando insights valiosos para melhorar os serviços públicos.

## Arquitetura do Projeto

A arquitetura do projeto é composta pelos seguintes componentes:

https://github.com/user-attachments/assets/00fe7ddc-4dd4-4417-b39b-7078184ce1d0

1. **S3 Camada Bronze**: Armazena os dados brutos extraídos da API de dados de Boston.
2. **S3 Camada Silver**: Armazena os dados transformados e limpos.
3. **S3 Camada Gold**: Armazena os dados finais prontos para análise.
4. **Glue Crawler**: Descobre automaticamente o esquema dos dados e cria o catálogo de dados.
5. **Glue Catalog**: Armazena metadados sobre as tabelas de dados.
6. **Glue ETL Jobs**: Realiza a transformação dos dados brutos e os move para a S3 Camada Silver.
8. **Glue Data Quality**: Verifica a qualidade dos dados após a transformação.
9. **Glue Data Brew**: Ferramenta para preparar e limpar os dados de forma interativa.
10. **Amazon QuickSight**: Ferramenta de visualização de dados para criar dashboards e relatórios.
11. **AWS Lake Formation**: Utilizado para gerenciar e proteger o acesso aos dados.
12. **Security Group**: Configuração de segurança para controlar o acesso aos recursos.

## Ferramentas Utilizadas

### AWS S3
- **O que é?**: Um serviço de armazenamento de objetos da AWS.
- **Como usamos?**: Armazenamos tanto os dados brutos (Camada Bronze) quanto os dados processados (Camadas Silver e Gold) aqui, servindo como um ponto central de armazenamento.

### AWS Glue
- **O que é?**: Um serviço de ETL (Extração, Transformação e Carregamento) da AWS.
- **Como usamos?**: Utilizamos o Glue para catalogar os dados (Glue Catalog), descobrir esquemas (Glue Crawler), e realizar transformações de dados (Glue ETL Jobs).

### Amazon Redshift (opcional)
- **O que é?**: Um armazém de dados em nuvem que facilita a análise de grandes volumes de dados.
- **Como usamos?**: Embora não seja mostrado na arquitetura, o Redshift pode ser usado para consultas rápidas e análises profundas dos dados transformados.


### AWS IAM
- **O que é?**: Um serviço de gerenciamento de identidade e acesso.
- **Como usamos?**: Configuramos permissões para garantir que apenas usuários autorizados possam acessar os recursos do projeto.

### Amazon CloudWatch
- **O que é?**: Um serviço de monitoramento que coleta dados e insights de aplicações e recursos da AWS.
- **Como usamos?**: Monitoramos o desempenho do pipeline e configuramos alertas para identificar rapidamente quaisquer problemas.

### Amazon QuickSight
- **O que é?**: Um serviço de visualização de dados.
- **Como usamos?**: Criamos dashboards e relatórios para visualizar insights dos dados.

### AWS Lake Formation
- **O que é?**: Um serviço para gerenciar e proteger dados armazenados no Data Lake.
- **Como usamos?**: Gerenciamos permissões e acesso aos dados armazenados no S3.

## Estrutura do Projeto

- `data/`
  - `raw/`: Onde armazenamos os dados brutos.
  - `processed/`: Onde armazenamos os dados transformados prontos para análise.
- `scripts/`
  - `etl.py`: Script principal que executa o pipeline de ETL.
  - `config.py`: Contém as configurações e credenciais necessárias para acessar os serviços da AWS.
- `docs/`
  - `architecture.png`: Diagrama que representa a arquitetura do projeto.
- `README.md`: Este documento de documentação do projeto.

## Configuração e Execução

### Pré-requisitos

- Uma conta AWS com permissões para S3, Glue, QuickSight e Lake Formation.
- Python 3.8 ou superior instalado.

### Instalação

1. Clone este repositório para sua máquina local:

```bash
git clone https://github.com/usuario/boston-data-pipeline.git
cd boston-data-pipeline
