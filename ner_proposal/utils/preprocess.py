import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
nltk.download('stopwords', quiet=True)

def preprocess_text(text):
    """
    Preprocess text for NER tasks
    
    Args:
        text (str): Input text to be preprocessed
        
    Returns:
        str: Preprocessed text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Convert to lowercase
    text = text.lower()
    
    return text

def clean_text(text):
    """Membersihkan teks dari karakter tidak penting, tanda baca, dan normalisasi"""
    if text is None:
        return ""
        
    text = re.sub(r'\s+', ' ', text)             # Hilangkan spasi ganda
    text = re.sub(r'[^A-Za-z0-9.,:;/\-()\s]', '', text)  # Hilangkan simbol aneh
    text = text.lower()

    # Hapus stopwords bahasa Indonesia
    stop_words = set(stopwords.words('indonesian'))
    tokens = [word for word in text.split() if word not in stop_words]

    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed = [stemmer.stem(word) for word in tokens]

    return ' '.join(stemmed)
