from flask import Flask, request ,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/affine_en', methods=['GET', 'POST'])
def affine_en():
    if request.method == 'POST':

        pt = request.form['pt']
        a = int(request.form['key1'])
        b = int(request.form['key2'])
        mi = 0
        for i in range(1,27):
            if (a*i)%26 == 1:
                mi = i
                break
        if mi == 0:
            return '''<h4>No multiplicative inverse for {}
                    '''.format(a)

        en = ""
        for i in range(0,len(pt)):
            if(ord(pt[i])>=65 and ord(pt[i])<=91):
                en += chr((a*(ord(pt[i])-65)+b)%26+65)
            else:
                en += chr((a*(ord(pt[i])-97)+b)%26+97)

        return '''<h3>Encrypted Text : {} </h3>'''.format(str(en))
    else:

        return '''<body bgcolor="gold"><h3>Affine Encryption</h3><br><br>
        Sample values A=3 and B=9 <br><br>
              <form method="POST">
                  Enter the Text : <input type="text" name="pt"><br>
                  Enter key A: <input type="number" name="key1"><br>
                  Enter key B: <input type="number" name="key2"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

@app.route('/affine_de', methods=['GET', 'POST'])
def affine_de():
    if request.method == 'POST':

        en = request.form['en']
        a = int(request.form['key1'])
        b = int(request.form['key2'])
        mi = 0

        for i in range(1,27):
            if (a*i)%26 == 1:
                mi = i
                break
        if mi == 0:
            return '''<h4>No multiplicative inverse for {}
                    '''.format(a)

        pt = ""

        for i in range(0,len(en)):
            if(ord(en[i])>=65 and ord(en[i])<=91):
                pt += chr((((ord(en[i])-65)+ (-b +26)) * mi)%26+65)
            else:
                pt += chr((((ord(en[i])-97)+ (-b +26)) * mi)%26+97)

        return '''<h3>Decrypted Text : {} </h3>'''.format(str(pt))
    else:

        return '''<body bgcolor="gold"><h3>Affine Decryption</h3><br><br>
        Sample values A=3 and B=9<br><br>
              <form method="POST">
                  Enter the Text: <input type="text" name="en"><br>
                  Enter key A: <input type="number" name="key1"><br>
                  Enter key B: <input type="number" name="key2"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
