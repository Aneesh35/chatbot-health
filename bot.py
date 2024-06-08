import nltk
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
import re
import random
import string

f = open('symptom.txt', 'r', errors='ignore')
m = open('pincodes.txt', 'r', errors='ignore')
checkpoint = "./chatbot_weights.ckpt"

raw = f.read()
rawone = m.read()

raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)  # converts to list of sentences
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["Myself  Medibot or your chatbot for health"]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi,are you suffering from any health issues?(Yes or No)", "hey,are you having any health issues?(Yes or No)",
                      "hii there,are you having any health issues?(Yes or No)",
                      "hi there,are you having any health issues?(Yes or No)", "hello,are you having any health issues?(Yes or No)",
                      "I am glad! You are talking to me,are you having any health issues?(Yes or No)"]
Basic_Questions= ("yes", "y", "ya")
Basic_Reply = "okay,tell me about your symptoms"
Basic_Om = ("no", "n", "na")
Basic_AnsM = "thank you visit again"
fev = ("iam suffering from fever", "i affected with fever", "i have fever", "fever")
feve_r = ("which type of fever you have? and please mention your symptoms then we try to calculate your disease.")

# Checking for greetings
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Questions
def basic(sentence):
    for word in Basic_Questions:
        if sentence.lower() == word:
            return Basic_Reply

def fever(sentence):
    for word in fev:
        if sentence.lower() == word:
            return feve_r

# Checking for Basic_QM
def basicM(sentence):
    for word in Basic_Om:
        if sentence.lower() == word:
            return Basic_AnsM

# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response for symptoms
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Generating response for picode
def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokensone[idx]
        return robo_response

def chat(user_response):
    user_response = user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "
    if user_response != 'bye':
        if user_response == 'thank you':
            return "I am glad that I was helpful to you! Do you have anything else to say? (Yes or No)"
        elif basicM(user_response) is not None:
            return basicM(user_response)
        else:
            if is_pincode(user_response):
                doctor_info = fetch_doctor_info_from_pincode(user_response)
                if doctor_info:
                    return f"Here are the available doctors for pincode {user_response}:\n\n{doctor_info}"
                else:
                    return f"Sorry, no doctor information found for pincode {user_response}."
            elif user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1:
                return responseone(user_response)
            elif greeting(user_response) is not None:
                return greeting(user_response)
            elif any(sub in user_response for sub in ["your name", "what are you", "your name ", " your name "]):
                return IntroduceMe(user_response)
            elif basic(user_response) is not None:
                return basic(user_response)
            elif fever(user_response) is not None:
                return fever(user_response)
            else:
                return response(user_response)
    else:
        return "Bye! take care.."

def is_pincode(input_str):
    pincode_pattern = r'^\d{6}$'
    return bool(re.match(pincode_pattern, input_str))

def fetch_doctor_info_from_pincode(pincode):
    with open('pincodes.txt', 'r', errors='ignore') as f:
        content = f.read()
        pincode_pattern = re.compile(fr'\b{re.escape(pincode)}-->(.*?)\b\d{{6}}-->', re.DOTALL)
        match = pincode_pattern.search(content)
        if match:
            return match.group(1).strip()
    return None
