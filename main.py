import subprocess
from flask import Flask,request, render_template
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def playsound():
    if request.method == 'GET':
        return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Browser voices</title>
    <style type="text/css">
                            * {
                      box-sizing: border-box;
                    }
                    html,
                    body {
                      min-height: 100vh;
                      margin: 0;
                      padding: 0;
                    }
                    body {
                      font-family: Helvetica, Arial, sans-serif;
                      color: #0d122b;
                      display: flex;
                      flex-direction: column;
                      padding-left: 1em;
                      padding-right: 1em;
                    }
                    h1 {
                      text-align: center;
                      font-weight: 100;
                    }
                    header {
                      border-bottom: 1px solid #0d122b;
                      margin-bottom: 2em;
                    }
                    main {
                      flex-grow: 2;
                      display: flex;
                      justify-content: space-around;
                      align-items: center;
                      background-color: #fff;
                      border-radius: 12px;
                      margin-bottom: 2em;
                    }
                    @keyframes bg-pulse {
                      0% {
                        background-color: #fff;
                      }

                      50% {
                        background-color: #c7ecee;
                      }

                      100% {
                        backgrouond-color: #fff;
                      }
                    }
                    main.speaking {
                      animation: bg-pulse 1.5s alternate ease-in-out infinite;
                    }
                    .input {
                      text-align: center;
                      width: 100%;
                    }
                    label {
                      display: block;
                      font-size: 18px;
                      margin-bottom: 1em;
                    }
                    .field {
                      margin-bottom: 2em;
                    }
                    input {
                      font-size: 24px;
                      padding: 0.5em;
                      border: 1px solid rgba(13, 18, 43, 0.25);
                      border-radius: 6px;
                      width: 75%;
                      display: inline-block;
                      transition: border-color 0.25s;
                      text-align: center;
                    }
                    input:focus,
                    select:focus {
                      border-color: rgba(13, 18, 43, 1);
                    }
                    select {
                      width: 75%;
                      font-size: 24px;
                      padding: 0.5em;
                      border: 1px solid rgba(13, 18, 43, 0.25);
                      border-radius: 6px;
                      transition: border-color 0.25s;
                    }
                    button {
                      font-size: 18px;
                      font-weight: 200;
                      padding: 1em;
                      width: 200px;
                      background: transparent;
                      border: 4px solid #f22f46;
                      border-radius: 4px;
                      transition: all 0.4s ease 0s;
                      cursor: pointer;
                      color: #f22f46;
                      margin-bottom: 2em;
                    }
                    button:hover,
                    button:focus {
                      background: #f22f46;
                      color: #fff;
                    }

                    a {
                      color: #0d122b;
                    }
                    .error {
                      color: #f22f46;
                      text-align: center;
                    }
                    footer {
                      border-top: 1px solid #0d122b;
                      text-align: center;
                    }
    </style>
  </head>
      <body>

          <header>
              <h1>Text to Speech</h1>
          </header>

        <main>
          <form class="input" id="voice-form" method="post">
                <div class="field">
                    <label for="speech">Type Something</label>
                    <input type="text" name="speech" id="speech" required />
                </div>
                <div class="field">
                    <label for="voices">Choose a Voice Assistant</label>
                      <select name="voices" id="voices">
                          <option value="Male">Male</option>
                          <option value="Female">Female</option>
                      </select>
                </div>
              <button>
                    Say it!
              </button>
          </form>
        </main>

        <footer>
            <p>
                Built by <a href=<BLOG LINK>><YOUR NAME></a>
            </p>
        </footer>

      </body>
</html>'''
    text = request.values.get("text")
    MyOut = subprocess.call(f'''termux-tts-speak {text}''', shell=True)
    return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Browser voices</title>
    <style type="text/css">
                            * {
                      box-sizing: border-box;
                    }
                    html,
                    body {
                      min-height: 100vh;
                      margin: 0;
                      padding: 0;
                    }
                    body {
                      font-family: Helvetica, Arial, sans-serif;
                      color: #0d122b;
                      display: flex;
                      flex-direction: column;
                      padding-left: 1em;
                      padding-right: 1em;
                    }
                    h1 {
                      text-align: center;
                      font-weight: 100;
                    }
                    header {
                      border-bottom: 1px solid #0d122b;
                      margin-bottom: 2em;
                    }
                    main {
                      flex-grow: 2;
                      display: flex;
                      justify-content: space-around;
                      align-items: center;
                      background-color: #fff;
                      border-radius: 12px;
                      margin-bottom: 2em;
                    }
                    @keyframes bg-pulse {
                      0% {
                        background-color: #fff;
                      }

                      50% {
                        background-color: #c7ecee;
                      }

                      100% {
                        backgrouond-color: #fff;
                      }
                    }
                    main.speaking {
                      animation: bg-pulse 1.5s alternate ease-in-out infinite;
                    }
                    .input {
                      text-align: center;
                      width: 100%;
                    }
                    label {
                      display: block;
                      font-size: 18px;
                      margin-bottom: 1em;
                    }
                    .field {
                      margin-bottom: 2em;
                    }
                    input {
                      font-size: 24px;
                      padding: 0.5em;
                      border: 1px solid rgba(13, 18, 43, 0.25);
                      border-radius: 6px;
                      width: 75%;
                      display: inline-block;
                      transition: border-color 0.25s;
                      text-align: center;
                    }
                    input:focus,
                    select:focus {
                      border-color: rgba(13, 18, 43, 1);
                    }
                    select {
                      width: 75%;
                      font-size: 24px;
                      padding: 0.5em;
                      border: 1px solid rgba(13, 18, 43, 0.25);
                      border-radius: 6px;
                      transition: border-color 0.25s;
                    }
                    button {
                      font-size: 18px;
                      font-weight: 200;
                      padding: 1em;
                      width: 200px;
                      background: transparent;
                      border: 4px solid #f22f46;
                      border-radius: 4px;
                      transition: all 0.4s ease 0s;
                      cursor: pointer;
                      color: #f22f46;
                      margin-bottom: 2em;
                    }
                    button:hover,
                    button:focus {
                      background: #f22f46;
                      color: #fff;
                    }

                    a {
                      color: #0d122b;
                    }
                    .error {
                      color: #f22f46;
                      text-align: center;
                    }
                    footer {
                      border-top: 1px solid #0d122b;
                      text-align: center;
                    }
    </style>
  </head>
      <body>

          <header>
              <h1>Text to Speech</h1>
          </header>

        <main>
          <form class="input" id="voice-form" method="post">
                <div class="field">
                    <label for="speech">Type Something</label>
                    <input type="text" name="speech" id="speech" required />
                </div>
                <div class="field">
                    <label for="voices">Choose a Voice Assistant</label>
                      <select name="voices" id="voices">
                          <option value="Male">Male</option>
                          <option value="Female">Female</option>
                      </select>
                </div>
              <button>
                    Say it!
              </button>
          </form>
        </main>

        <footer>
            <p>
                Built by <a href=<BLOG LINK>><YOUR NAME></a>
            </p>
        </footer>

      </body>
</html>'''
if __name__ =='__main__':
    app.run(port=8080 , debug=True)
