from flask import Flask, render_template, request
import random
import datetime

app = Flask(__name__)

TEMPLATES = [
    "{number} Proven Ways to Master {Kw} in {year}",
    "The Ultimate Guide to {Kw} for Beginners",
    "How to Learn {Kw}: A Step-by-Step Guide",
    "{number} {Kw} Mistakes You Should Avoid",
    "Why {Kw} Matters More Than Ever in {year}",
    "{Kw} 101: Everything You Need to Know",
    "{number} {Kw} Tips That Actually Work",
    "The Beginner's Roadmap to {Kw}",
    "{Kw} Trends to Watch in {year}",
    "A Complete Guide to {Kw}"
]

NUMBERS = [3, 5, 7, 9, 10, 12, 15]


def generate_titles(topic, count):

    topic = topic.strip()

    kw = topic
    Kw = topic[0].upper() + topic[1:]
    year = datetime.datetime.now().year

    selected = random.sample(TEMPLATES, count)

    titles = []

    for template in selected:

        title = template.format(
            kw=kw,
            Kw=Kw,
            year=year,
            number=random.choice(NUMBERS)
        )

        titles.append(title)

    return titles


@app.route("/", methods=["GET", "POST"])
def index():

    titles = []
    topic = ""

    if request.method == "POST":

        topic = request.form.get("topic", "").strip()

        print("TOPIC:", topic)

        if topic:

            titles = generate_titles(topic, 8)

            print("TITLES:", titles)

    return render_template(
        "index.html",
        topic=topic,
        titles=titles
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )