from flask import Flask, render_template, request
from defin import qwe
import psycopg2

app = Flask(__name__, template_folder="./templates")

#res = qwe()

def connection():
    conn = psycopg2.connect(dbname = 'postgres', user = 'postgres', password = 'vipjan15', host = 'localhost')
    return conn


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("hh.html")

@app.route('/upload', methods=["POST"])
def upload():
    fs = request.files.get('snap')
    fs.save('image.jpg')
    #res = qwe()
    #print(res)
    if qwe()=='' :
      return 'Not read number'
        #name = flask.request.form['result']

    try:          
        base = []    
        connec = connection()
        cursor = connec.cursor()    
        cursor.execute('''
                                    select id_ as INVENT, first_name as Familia,
                                    last_name as Imia
                                    from invent 
                                    where id_ = %s''', [qwe()]
                                    )
        
        for row in cursor.fetchall():
            base.append({"INVENT":row[0], "Familia": row[1], "Imia": row[2]})
            return str(base)
        
        connec.close()
        if base == True:
           return str(base)
        else:
           return e 
    except Exception as e:
        return ('Not in'+ ' ' + qwe())
        
    return "Not invent in database or Snap again!" + ' '+ res

@app.route('/give', methods=["GET","POST"])
def give():
    name = request.form["text"]
    #print(name)
    if name == '':
        return "Not number inside the text"
    
    try:
        base = []    
        connec = connection()
        cursor = connec.cursor()    
        cursor.execute('''
                                    select id_ as INVENT, first_name as Familia,
                                    last_name as Imia
                                    from invent 
                                    where id_ = %s''', [name]
                                    )
        
        for row in cursor.fetchall():
            base.append({"INVENT":row[0], "Familia": row[1], "Imia": row[2]})
            return str(base)
        
        connec.close()
        if base == True:
               return str(base)
        else:
           return e 
    except Exception as e:
        return ('Not in'+ ' ' + name)
        
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
