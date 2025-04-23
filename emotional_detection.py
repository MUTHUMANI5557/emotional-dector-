# Install required package if not already installed
# pip install ibm-watson

from ibm_watson import Natural LanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

# Replace with your IBM Watson NLU API key and URL
API_KEY = 'YOUR_IBM_WATSON_API_KEY'
URL = 'YOUR_IBM_WATSON_SERVICE_URL'

# Authenticate and initialize service
authenticator = IAMAuthenticator(API_KEY)
nlu = Natural LanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
nlu.set_service_url(URL)

# Input text for emotion detection
text_to_analyze = input("Enter the text to analyze emotions: ")

# Analyze emotions in the text
response = nlu.analyze(
    text=text_to_analyze,
    features=Features(emotion=EmotionOptions())
).get_result()

# Extract and display the emotion scores
print("\n--- Detected Emotions ---")
emotions = response['emotion']['document']['emotion']
for emotion, score in emotions.items():
    print(f"{emotion.capitalize()}: {score:.2f}")
