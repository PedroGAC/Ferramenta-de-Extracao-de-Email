import re
import os

def extract_emails(text):
    """
    Função que extrai todos os endereços de e-mail de um texto.
    
    Args:
        text (str): O texto a ser analisado.
        
    Returns:
        str: Uma string contendo todos os e-mails encontrados, separados por espaço.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(email_pattern, text)
    
    return ' '.join(emails)


def extract_emails_from_file(file_path):
    """
    Função que extrai todos os endereços de e-mail de um arquivo de texto.
    
    Args:
        file_path (str): Caminho para o arquivo .txt a ser analisado.
        
    Returns:
        str: Uma string contendo todos os e-mails encontrados, separados por espaço.
        
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        ValueError: Se o arquivo não for um .txt.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo '{file_path}' não foi encontrado.")
    
    if not file_path.lower().endswith('.txt'):
        raise ValueError(f"O arquivo '{file_path}' não é um arquivo .txt.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        return extract_emails(text)
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo: {str(e)}")


if __name__ == "__main__":
    test_text = "Favor enviar um e-mail para abc@hotmail.com com cópia para def@abc.com.br"
    result = extract_emails(test_text)
    print("Teste 1 - Texto direto:")
    print(result)
    
    test_text2 = "Contatos: suporte.tecnico@empresa.com.br, marketing@site.net e user_1234@provedor.org"
    result2 = extract_emails(test_text2)
    print("\nTeste 2 - Texto direto:")
    print(result2)  
    
    print("\nTeste 3 - Arquivo de texto:")
    try:
        file_result = extract_emails_from_file('teste.txt')
        print(file_result)
    except Exception as e:
        print(f"Erro: {str(e)}")