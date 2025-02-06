# Comparador de Resultados de LLMs

Este projeto tem como objetivo comparar as respostas de dois modelos de linguagem (LLMs): o **ChatGPT** (da OpenAI) e o **Gemini** (da Google). Utilizando padrões de projeto Strategy, Factory, Observer e Command, o sistema determina qual resposta é a mais adequada para uma determinada pergunta.

## Funcionalidades
- Envio de perguntas para o ChatGPT e o Gemini.
- Avaliação das respostas utilizando estratégias baseadas em similaridade.
- Notificação sobre a melhor resposta escolhida.

## Como Rodar o Projeto

### 1. Clone o Repositório
```bash
 git clone https://github.com/lauracarolinem/teste_sinerji.git
 cd comparador-llms
```

### 2. Instale as Dependências
Certifique-se de ter o **Python 3.8+** instalado. Em seguida, instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:
```env
OPENAI_API_KEY=sua_chave_da_openai
GEMINI_API_KEY=sua_chave_do_gemini
```

**Importante:** O projeto não funcionará sem o `.env` configurado corretamente.

### 4. Execute o Projeto
```bash
python3 main.py
```

## Tecnologias Utilizadas
- **Python 3.8+**
- **APIs do ChatGPT e Gemini**
- **Padrões de Projeto:** Strategy, Factory, Observer e Command

