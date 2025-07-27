# src/summarizer.py

from transformers import pipeline, AutoTokenizer
import textstat

# Load the model and tokenizer once when the module is imported
print("Loading summarization model and tokenizer for the first time...")
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Model and tokenizer loaded successfully.")


def summarize_text(article_text):
    """
    Summarizes text using a chunking strategy for long articles.
    """
    # --- 1. Split text into chunks ---
    # We use the model's tokenizer to split the text into chunks that fit the model's max input size.
    max_chunk_length = 1000 # The model's max is 1024, so we leave a small buffer.
    inputs = tokenizer(article_text, return_tensors='pt')
    
    # Manually split the tokens into chunks
    num_tokens = inputs['input_ids'].shape[1]
    chunk_start = 0
    chunks = []
    while chunk_start < num_tokens:
        chunk_end = chunk_start + max_chunk_length
        chunk_ids = inputs['input_ids'][0, chunk_start:chunk_end]
        # Decode the chunk of tokens back to text
        chunk_text = tokenizer.decode(chunk_ids, skip_special_tokens=True)
        chunks.append(chunk_text)
        chunk_start = chunk_end

    # --- 2. Summarize each chunk ---
    print(f"Text split into {len(chunks)} chunks. Generating summaries for each...")
    individual_summaries = summarizer(chunks, max_length=150, min_length=30, do_sample=False)
    
    # --- 3. Join summaries and calculate stats ---
    final_summary = ' '.join([summ['summary_text'] for summ in individual_summaries])
    
    original_wc = len(article_text.split())
    summary_wc = len(final_summary.split())
    readability_score = textstat.flesch_reading_ease(final_summary)

    results = {
        'summary_text': final_summary,
        'original_wc': original_wc,
        'summary_wc': summary_wc,
        'readability_score': readability_score
    }
    
    return results