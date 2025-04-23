# emotion_detector.py

def mock_emotion_detection(text):
    # Simulated emotion scores for demonstration
    if "hate" in text.lower() or "angry" in text.lower():
        return {
            'sadness': 0.45,
            'joy': 0.02,
            'fear': 0.10,
            'disgust': 0.30,
            'anger': 0.60
        }
    elif "happy" in text.lower() or "joy" in text.lower():
        return {
            'sadness': 0.05,
            'joy': 0.85,
            'fear': 0.05,
            'disgust': 0.02,
            'anger': 0.03
        }
    else:
        return {
            'sadness': 0.20,
            'joy': 0.25,
            'fear': 0.15,
            'disgust': 0.10,
            'anger': 0.30
        }

def format_output(emotions):
    print("\n--- Detected Emotions ---")
    print("Emotion    | Score")
    print("----------------------")
    for emotion, score in emotions.items():
        print(f"{emotion.capitalize():<10} | {score:.2f}")
    
    dominant = max(emotions, key=emotions.get)
    print(f"\n🔥 Dominant Emotion: {dominant.capitalize()}")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a sentence to detect emotions: ")
    emotions = mock_emotion_detection(user_input)
    format_output(emotions)
