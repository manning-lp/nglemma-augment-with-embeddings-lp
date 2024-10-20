from bs4 import BeautifulSoup
import tiktoken

def extract_text_from_html(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        text = soup.get_text()

        clean_text = ' '.join(text.split())

        return clean_text

    except Exception as e:
        return f"Error occured while processing the file:{str(e)}"
  
def segment_text_by_tokens(text, max_tokens, encoding_name='gpt-3.5-turbo'):
   
    encoding = tiktoken.encoding_for_model(encoding_name)

    words = text.split()

    chunks = []
    current_chunk = []
    current_chunk_tokens = 0

    for word in words:

      word_tokens = len(encoding.encode(word))

      if current_chunk_tokens + word_tokens > max_tokens:
        chunks.append(' '.join(current_chunk))
        current_chunk = [word]
        current_chunk_tokens = word_tokens
      else:
        current_chunk.append(word)
        current_chunk_tokens += word_tokens
        
    if current_chunk:
      chunks.append(' '.join(current_chunk))

    return chunks

def extract_and_segment_html(file_path, max_tokens, encoding_name='gpt-3.5-turbo'):
  
    try:
       
       with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
          html_content = file.read()

       soup = BeautifulSoup(html_content, 'html.parser')

       for script_or_style in soup(['script', 'style']):
          script_or_style.decompose()

       text = soup.get_text()
       clean_text = ' '.join(text.split())

       encoding = tiktoken.encoding_for_model(encoding_name)
       words = clean_text.split()

       chunks = []
       current_chunk = []
       current_chunk_tokens = 0

       for word in words:
            word_tokens = len(encoding.encode(word))

            if current_chunk_tokens + word_tokens > max_tokens:
                
                    chunks.append(' '.join(current_chunk))
                    current_chunk = [word]
                    current_chunk_tokens = word_tokens

            else:
                
                current_chunk.append(word)
                current_chunk_tokens += word_tokens

       if current_chunk:

            chunks.append(' '.join(current_chunk))

       return chunks
    
    except Exception as e:
       return f"Error occured:{str(e)}"



