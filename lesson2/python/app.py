### Реализация на Python
from flask import Flask, Response

app = Flask(__name__)

HTML = """<!doctype html>
<html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Собачка (Flask)</title>
<style>
  body{font-family:system-ui,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;gap:12px}
  button{padding:10px 20px;font-size:1.1rem;cursor:pointer}
  #msg{font-size:1.6rem}
</style>
</head><body>
<h1>Учебное приложение №2 (Flask)</h1>
<button id="dog-btn">Что говорит собачка</button>
<div id="msg" aria-live="polite"></div>
<script>
  document.getElementById('dog-btn').addEventListener('click',()=>{document.getElementById('msg').textContent='Гав'})
</script>
</body></html>"""

@app.get("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
