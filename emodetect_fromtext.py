from transformers import pipeline


# Load Hugging Face Emotion Model
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def get_text_emotion(text):
    """
    Detect the emotion of the given text using a pre-trained transformer model.
    Returns the label with highest confidence and its score.
    """
    results = emotion_model(text)[0]  
    top_emotion = max(results, key=lambda x: x['score'])
    return top_emotion['label'], round(top_emotion['score'], 2)
