# main entry point for our project
import pickle
from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Flask app = startmh point of our project
app = Flask(__name__)

nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()


def transform_text(message):
    text=message.lower()
    text=nltk.word_tokenize(text)

    y=[]

    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


    return 


def predict_spam(message):
    #preprocess the message 
    transform_sms=transform_text(message)

    # VECTORIZE THE SMS
    vector_input=tfidf.transform([transform_sms])

    #predict
    result=model.predict(vector_input)[0]

    return result

@app.route('/')# homepage 
def home():
    return render_template('index.html')




@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        input_sms = request.form['message']
        result=predict_spam(input_sms)
        return render_template('index.html',result= result)



if __name__=='__main__':
    tfidf = pickle.load(open('vectorizer.pkl','rb'))
    model=pickle.load(open('model.pkl','rb'))
    app.run(host='0.0.0.0')

