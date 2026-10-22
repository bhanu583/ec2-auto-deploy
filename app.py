from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello, AWS CI/CD! | Flask Application</title>
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f7f8;
                color: #123b4a;
            }

            nav {
                background: #123b4a;
                color: white;
                padding: 20px 8%;
                font-size: 20px;
                font-weight: bold;
            }

            header {
                background: linear-gradient(135deg, #123b4a, #237d83);
                color: white;
                padding: 65px 8%;
            }

            header h1 {
                font-size: 42px;
                margin: 0 0 15px;
            }

            header p {
                font-size: 17px;
                line-height: 1.7;
                color: #d1e5e9;
            }

            .status {
                display: inline-block;
                background: #36c5a0;
                color: #102f38;
                padding: 12px 20px;
                border-radius: 8px;
                margin-top: 15px;
                font-weight: bold;
            }

            main {
                max-width: 950px;
                margin: 35px auto;
                padding: 0 20px;
            }

            .card {
                background: white;
                padding: 30px;
                border-radius: 14px;
                box-shadow: 0 5px 20px #123b4a12;
            }

            .card h1 {
                font-size: 32px;
                color: #123b4a;
            }

            .card h2 {
                font-size: 26px;
                color: #237d83;
            }

            .card h3 {
                font-size: 21px;
                color: #345a65;
            }

            .card h4 {
                font-size: 17px;
            }

            .card h5 {
                font-size: 14px;
                color: #617780;
            }

            .card h6 {
                font-size: 12px;
                color: #84969c;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #617780;
                font-size: 14px;
            }

            @media (max-width: 600px) {
                header h1 {
                    font-size: 32px;
                }

                .card {
                    padding: 20px;
                }
            }
        </style>
    </head>
    <body>
        <nav>HelloWorld</nav>

        <header>
            <h1>Hello, World!</h1>
            <p>Your Flask application is running successfully
            on Amazon EC2.</p>
            <span class="status">Deployment Successful</span>
        </header>

        <main>
            <section class="card">
                <h1>Hello World — H1</h1>
                <h2>Hello World — H2</h2>
                <h3>Hello World — H3</h3>
                <h4>Hello World — H4</h4>
                <h5>Hello World — H5</h5>
                <h6>Hello World — H6</h6>
            </section>
        </main>

        <footer>
            Powered by Flask | Hosted on Amazon EC2
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
