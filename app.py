from flask import Flask, render_template, request, redirect, flash
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)
app.config['SECRET_KEY'] = 'safe1222345semicodewq'

uri = "mongodb+srv://SemiAkindipeCluster:Semicoding2011@cluster0.wqfphzp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db=client.ContactManager

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        contacts = db.Contacts.find()
        return render_template('index.html',contacts = contacts)
    if request.method=='POST':
        print(request.form)
        if len(request.form['name'])>2:
            if len(request.form['number'])>9 and request.form['number'].isnumeric()==True:
                document = {}
                document['name'] = request.form['name']
                document['number'] = request.form['number']
                db.Contacts.insert_one(document)
                flash('Contact successfully added.')
                return redirect('/')
            else:
                flash('Phone number is invalid.')
                return redirect('/')
        else:
            flash('Name must be more than three letters.')
            return redirect('/')
    return render_template('index.html')
@app.route('/delete/<contact_id>')
def delete(contact_id):
    db.Contacts.delete_one({'_id':ObjectId(contact_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=8000)