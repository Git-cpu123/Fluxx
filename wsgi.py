from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


# Homepage
@app.route('/')
def home():
    return render_template('index.html', title="Fluxx Studios")


# Book pages
@app.route('/patchwork')
def patchwork():
    return render_template('patchwork.html', title="Patchwork: Issue 1")


@app.route('/marchcall')
def march_call():
    return render_template('march_call.html', title="March Call")


@app.route('/neuronet')
def neuronet():
    return render_template('neuronet.html', title="NeuroNet")


@app.route('/extinction')
def extinction():
    return render_template('extinction.html', title="Extinction.exe")


# Serve PDFs from static folder
@app.route('/pdf/<filename>')
def pdf(filename):
    return send_from_directory('static', filename)


@app.route('/MERCH!')
def merch():
    return render_template('MERCH!.html', title="MERCH")


if __name__ == "__main__":
    # Listen on all interfaces for ngrok
    app.run(host='0.0.0.0', port=5000)