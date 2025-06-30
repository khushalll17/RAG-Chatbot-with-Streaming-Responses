from bs4 import BeautifulSoup
import re
def clean_text(text):

    text = BeautifulSoup(text, "html.parser").get_text()

    text = text.replace('\xa0', ' ').replace('\n', ' ').replace('\r', ' ')

    text = re.sub(r'[-–—]{2,}', ' ', text)      
    text = re.sub(r'[.]{2,}', ' ', text)        

    text = re.sub(r'\s{2,}', ' ', text)
    text = text.strip()

    text = re.sub(r'(User Agreement|eBay Inc\.|Page \d+ of \d+)', '', text, flags=re.IGNORECASE)

    text = re.sub(r'https?://\S+', '', text)

    return text