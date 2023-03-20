#importing flask
from flask import Flask, render_template,request
#Importing the summarizer
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer
# from sentence_transformers import SentenceTransformer

# Using an instance of SBERT to create the model
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
# model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')
# model = Summarizer()

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template('index.html')

@app.route("/summarize", methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    result = model(body, num_sentences=2)
    return render_template('summary.html',result=result)

if __name__ =="__main__":
    app.run(debug=True,port=8000)