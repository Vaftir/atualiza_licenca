# Projeto Exemplo

Este é um projeto exemplo que demonstra como criar um ambiente virtual Python (`venv`), instalar as dependências listadas em um arquivo `requirements.txt` e compilar a aplicação utilizando o PyInstaller.

## Pré-requisitos

- Python 3.x instalado em seu sistema
- `pip` (gerenciador de pacotes do Python) instalado

## Passos para Configuração

### 1. Clonar o Repositório

Primeiro, clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar um Ambiente Virtual

Crie um ambiente virtual em Python utilizando o módulo `venv`:

```bash
python3 -m venv venv
```

Isso criará um diretório chamado `venv` (ou o nome que você escolher) que conterá o ambiente virtual.

### 3. Ativar o Ambiente Virtual

Ative o ambiente virtual. O método de ativação depende do seu sistema operacional:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **MacOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Você saberá que o ambiente virtual está ativado porque o nome do ambiente (`venv`) aparecerá no início da linha de comando.

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isso instalará todos os pacotes necessários para o projeto.

### 5. Configurar o Arquivo de Configuração

Crie um arquivo de configuração chamado `config.json` no diretório `config` (ou o diretório apropriado conforme seu projeto). O conteúdo do arquivo deve ser conforme o exemplo abaixo:

```json
{
    "Descrição": "Arquivo de produção",
    "zantus_user": {
        "username": "seu login no site",
        "password": "sua senha"
    },
    "url_manager": {
        "description": "Site Zanthus",
        "title": "Zantus Manager <homolog ou prod>",
        "url": "url- destino"
    },
    "banco de dados": {
        "host": "endereço do banco",
        "user": "usuário do banco",
        "password": "senha do banco",
        "database": "nome do banco"
    }
}
```

Certifique-se de substituir os valores com as informações reais do seu ambiente.

### 6. Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

### 7. Compilar a Aplicação com PyInstaller

Para compilar sua aplicação em um executável utilizando o PyInstaller, siga os passos abaixo:

#### Instalar o PyInstaller

Com o ambiente virtual ativado, instale o PyInstaller utilizando o `pip`:

```bash
pip install pyinstaller
```

#### Compilar a Aplicação

Utilize o comando do PyInstaller para compilar sua aplicação. Substitua `seu_script.py` pelo nome do arquivo principal do seu projeto:

```bash
pyinstaller --onefile seu_script.py
```

Este comando cria um executável único da sua aplicação. Você pode encontrar o executável gerado na pasta `dist`, dentro do diretório do seu projeto.

#### Configurações Adicionais

O PyInstaller oferece várias opções de configuração que podem ser úteis. Por exemplo, você pode especificar um ícone para o executável com a opção `--icon`:

```bash
pyinstaller --onefile --icon=seu_icone.ico seu_script.py
```

Além disso, é possível criar um arquivo de especificação (`.spec`) para personalizar ainda mais a compilação. Este arquivo é gerado automaticamente na primeira vez que você executa o PyInstaller, e pode ser editado para incluir configurações específicas.

### Exemplo de Arquivo .spec

Aqui está um exemplo básico de um arquivo `.spec` que pode ser gerado:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['seu_script.py'],
    pathex=['/caminho/para/seu_projeto'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='seu_executavel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='seu_executavel'
)
```

### Finalizando

Após compilar a aplicação, você pode distribuir o executável gerado sem a necessidade de instalar o Python ou qualquer dependência adicional no sistema do usuário final.

Para mais informações sobre as opções e configurações do PyInstaller, consulte a [documentação oficial do PyInstaller](https://pyinstaller.readthedocs.io/en/stable/).

## Resumo dos Comandos

1. Clonar o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Criar e ativar o ambiente virtual:

    - **Windows**:

        ```bash
        python3 -m venv venv
        venv\Scripts\activate
        ```

    - **MacOS/Linux**:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Instalar as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configurar o arquivo de configuração (`config.json`):

    ```json
    {
        "Descrição": "Arquivo de produção",
        "zantus_user": {
            "username": "seu login no site",
            "password": "sua senha"
        },
        "url_manager": {
            "description": "Site Zanthus",
            "title": "Zantus Manager <homolog ou prod>",
            "url": "url- destino"
        },
        "banco de dados": {
            "host": "endereço do banco",
            "user": "usuário do banco",
            "password": "senha do banco",
            "database": "nome do banco"
        }
    }
    ```

5. Desativar o ambiente virtual:

    ```bash
    deactivate
    ```

6. Instalar o PyInstaller:

    ```bash
    pip install pyinstaller
    ```

7. Compilar a aplicação:

    ```bash
    pyinstaller --onefile seu_script.py
    ```

8. (Opcional) Compilar a aplicação com um ícone:

    ```bash
    pyinstaller --onefile --icon=seu_icone.ico seu_script.py
    ```

## Notas Adicionais

- Certifique-se de que o `requirements.txt` contenha todas as dependências necessárias para o seu projeto.
- Caso precise adicionar mais pacotes ao seu projeto, lembre-se de atualizá-lo com:

    ```bash
    pip freeze > requirements.txt
    ```

Isso garantirá que todos os pacotes usados no seu ambiente de desenvolvimento estejam listados.

---

Com esses passos, você estará pronto para configurar e utilizar um ambiente virtual Python para gerenciar as dependências do seu projeto de forma isolada e organizada, além de compilar sua aplicação em um executável para fácil distribuição. Se precisar de mais alguma ajuda, sinta-se à vontade para perguntar!
