
# Atualiza licenças

Este é um projeto exemplo que demonstra como criar um ambiente virtual Python (`venv`) e instalar as dependências listadas em um arquivo `requirements.txt`.

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

### 5. Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

## Resumo dos Comandos

1. Clonar o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Criar e ativar o ambiente virtual:

    - Windows:

        ```bash
        python3 -m venv venv
        venv\Scripts\activate
        ```

    - MacOS/Linux:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Instalar as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Desativar o ambiente virtual:

    ```bash
    deactivate
    ```

## Notas Adicionais

- Certifique-se de que o `requirements.txt` contenha todas as dependências necessárias para o seu projeto.
- Caso precise adicionar mais pacotes ao seu projeto, lembre-se de atualizá-lo com:

    ```bash
    pip freeze > requirements.txt
    ```

Isso garantirá que todos os pacotes usados no seu ambiente de desenvolvimento estejam listados.

