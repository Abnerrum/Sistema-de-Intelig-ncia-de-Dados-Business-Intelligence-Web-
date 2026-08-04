# Sistema de Inteligência de Dados — BI Web

Aplicação web que transforma planilhas Excel em dados organizados, indicadores e dashboards para apoiar a tomada de decisão em pequenas e médias empresas.

## Problema abordado

Muitas empresas mantêm controles importantes em planilhas isoladas. Isso dificulta a padronização, a análise histórica e o acompanhamento dos principais indicadores. O projeto centraliza esse fluxo em uma aplicação web baseada em ETL.

```text
Excel → Pandas → ETL → MySQL → Flask → Dashboard
```

## Funcionalidades

- Upload e processamento de planilhas Excel;
- Limpeza e transformação dos dados;
- Armazenamento em MySQL;
- Dashboard com gráficos e KPIs;
- Filtros por período;
- Autenticação de usuários;
- Exportação de relatórios;
- Interface responsiva e modo escuro.

## Indicadores

- Volume financeiro;
- Quantidade de vendas;
- Ticket médio;
- Produto mais vendido;
- Evolução das vendas;
- Distribuição por produto.

## Tecnologias

- **Backend:** Python, Flask e Jinja2;
- **Dados:** Pandas, OpenPyXL e Plotly;
- **Banco:** MySQL;
- **Frontend:** HTML5, CSS3, Bootstrap 5 e Font Awesome.

## Como executar

```bash
git clone https://github.com/Abnerrum/Sistema-de-Intelig-ncia-de-Dados-Business-Intelligence-Web-.git
cd Sistema-de-Intelig-ncia-de-Dados-Business-Intelligence-Web-
python -m venv .venv
```

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

No Linux ou macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Configure a conexão com o MySQL conforme as variáveis esperadas pela aplicação antes de iniciar o servidor.

## O que o projeto demonstra

- Construção de pipelines ETL;
- Tratamento de dados com Python;
- Integração entre backend, banco de dados e frontend;
- Criação de dashboards e indicadores empresariais;
- Organização de uma aplicação Flask.

## Autor

Desenvolvido por [Abner Luiz](https://github.com/Abnerrum).
