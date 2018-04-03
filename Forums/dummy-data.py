from flask import Flask, render_template
import models
import stores

app = Flask(__name__)
poststore = stores.PostsStore()
poststore.add(models.Post("Life", "Life is alawys great"))
poststore.add(models.Post("hi", "this is my first web site and i'm enjoying"))


@app.route("/index")
def home():
    return render_template("index.html",posts=poststore.get_all())
app.run()
