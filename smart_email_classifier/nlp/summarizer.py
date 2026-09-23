import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

def summarize_email(text, num_sentences=2):
    """
    Extractive summarization based on word frequencies.
    """
    if not text or len(text.strip()) == 0:
        return "No text to summarize."
        
    try:
        sentences = sent_tokenize(text)
    except LookupError:
        # Fallback if punkt is not downloaded somehow
        nltk.download('punkt')
        try:
             # Punkt is now split in some NLTK versions, handle gracefully
             nltk.download('punkt_tab')
        except:
             pass
        sentences = sent_tokenize(text)

    # If email is very short, just return it
    if len(sentences) <= num_sentences:
        return text

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    
    # Calculate word frequencies
    freq_table = defaultdict(int)
    for word in words:
        if word.isalnum() and word not in stop_words:
            freq_table[word] += 1
            
    # Score sentences
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]
                
    # Get top sentences
    import heapq
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Reorder based on original position
    summary_sentences.sort(key=lambda x: sentences.index(x))
    
    return " ".join(summary_sentences)
