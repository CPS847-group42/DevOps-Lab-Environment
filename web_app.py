#!flask/bin/python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
textbooks = [
    {
        'title': u"Introduction to Algorithms" ,
        'id': 1,
        'authors': [u"Thomas H. Cormen", u"Charles E. Leiserson", u"Ronald L. Rivest", u"Clifford Stein" ],
        'ISBN': 9780262033848,
        'edition': 3 

    },

    {
        'title': u"Computer Networking: A Top-down Approach" ,
        'id': 2,
        'authors': [u"James F. Kurose", u"Kieth W. Ross"],
        'ISBN': 9780133594140,
        'edition': 7 

    },
    
]

@app.route('/io', methods=['GET'])
def get_textbooks():

    local_time = datetime.now()
    today8am = local_time.replace(hour=8, minute=0, second=0, microsecond=0)
    today4pm = local_time.replace(hour=16, minute=0, second=0, microsecond=0)
    if local_time < today4pm and local_time > today8am:
        print('Accessed during school time')
    else:
        print('Accessed after school time')
        

    return jsonify({'textbooks': textbooks})

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)