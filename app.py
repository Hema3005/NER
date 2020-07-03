from flask import Flask,render_template,url_for,request
import pos_tagger  #create module 
import json


app = Flask(__name__,template_folder="template")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return "<h1>Name entity Recognition using spacy"

def get_entity_namelist(json_data):
    results=[]
    for items in json_data:
      results.append({items.get("Entity"):items.get("Name")})
    return results



@app.route("/process",methods =['POST', 'GET'])
def process():
    if request.method == 'POST':
        url = request.form['url']
        json_data=pos_tagger.send(url)         
        results=get_entity_namelist(json_data)  
        print("running succesfully!!!")  
        return render_template("index.html",results=results)

if __name__ == '__main__':
	app.run(debug=True,port=5003)
    


    