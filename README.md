# Extrator de E-mails

Este programa Python extrai endereços de e-mail de textos e arquivos .txt, utilizando expressões regulares para identificar padrões de e-mail válidos.

## Funcionalidades

- Extração de e-mails a partir de strings de texto
- Extração de e-mails a partir de arquivos .txt
- Detecção de diversos formatos de e-mail, incluindo:
  - E-mails com caracteres especiais (pontos, hifens, underscores)
  - E-mails com formato user+tag
  - E-mails com múltiplos subdomínios
  - Diversos TLDs (.com, .org, .net, .com.br, etc.)

## Requisitos

- Python 3.x

## Instalação

1. Clone este repositório ou baixe o arquivo `email_extractor.py`
2. Não há dependências externas além da biblioteca padrão do Python

## Uso

### Como módulo em seu código

```python
from email_extractor import extract_emails, extract_emails_from_file

# Extrair e-mails de uma string
texto = "Contato: user@example.com e outro.email@dominio.com.br"
emails = extract_emails(texto)
print(emails)  # Saída: "user@example.com outro.email@dominio.com.br"

# Extrair e-mails de um arquivo .txt
emails_do_arquivo = extract_emails_from_file('caminho/para/arquivo.txt')
print(emails_do_arquivo)
```

### Como programa standalone

```bash
python email_extractor.py
```

O programa executará os testes incluídos no código. Para utilizar com seus próprios arquivos, edite a seção principal do código (`if __name__ == "__main__":`) descomentando as linhas para leitura de arquivo.

## Exemplos

```python
# Exemplo 1: Texto simples
texto1 = "Favor enviar um e-mail para abc@hotmail.com com cópia para def@abc.com.br"
resultado1 = extract_emails(texto1)
# Resultado: "abc@hotmail.com def@abc.com.br"

# Exemplo 2: Texto com múltiplos e-mails
texto2 = "Contatos: suporte.tecnico@empresa.com.br, marketing@site.net e user_1234@provedor.org"
resultado2 = extract_emails(texto2)
# Resultado: "suporte.tecnico@empresa.com.br marketing@site.net user_1234@provedor.org"

# Exemplo 3: Leitura de arquivo
try:
    resultado3 = extract_emails_from_file('exemplo.txt')
    # Resultado: todos os e-mails encontrados no arquivo
except Exception as e:
    print(f"Erro: {str(e)}")
```

## Explicação da Expressão Regular

O padrão usado para identificar e-mails é:

```
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

Esta expressão regular:

1. `[a-zA-Z0-9._%+-]+` - Identifica o nome de usuário, permitindo letras, números e os caracteres especiais `._%+-`
2. `@` - O símbolo @ que separa usuário e domínio
3. `[a-zA-Z0-9.-]+` - O nome do domínio, permitindo letras, números, pontos e hifens
4. `\.` - Um ponto literal
5. `[a-zA-Z]{2,}` - A extensão do domínio com pelo menos duas letras

## Limitações

- Não valida completamente todos os formatos de e-mail segundo o RFC 5322
- Não verifica se o e-mail existe realmente
- Pode capturar strings que parecem e-mails válidos mas não são

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.