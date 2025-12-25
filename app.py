from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nama_input = None
    if request.method == 'POST':
        # Mengambil data dari TextField dengan name="user_name"
        nama_input = request.form.get('user_name')
    
    return render_template('index.html', nama=nama_input)

if __name__ == '__main__':
    app.run(debug=True)