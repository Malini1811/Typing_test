from flask import Flask, render_template, request
from essential_generators import DocumentGenerator
import time

app = Flask(__name__)
gen = DocumentGenerator()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        original = request.form["original"]
        typed = request.form["typed"]
        start_time = float(request.form["start_time"])
        end_time = time.time()

        time_taken = round(end_time - start_time, 2)
        original_words = original.split()
        typed_words = typed.split()
        word_count = len(original_words)

        correct = 0
        mistake_count = 0

        for o, t in zip(original_words, typed_words):
            if o == t:
                correct += 1
            else:
                mistake_count += 1

        # Count extra or missing words as mistakes
        mistake_count += abs(len(original_words) - len(typed_words))

        accuracy_percent = round((correct / word_count) * 100, 2)
        wpm = round((word_count / time_taken) * 60)

        if accuracy_percent < 50 or wpm < 30:
            feedback = "You need to practice typing more!"
        elif accuracy_percent < 80 or wpm < 60:
            feedback = "You are doing great!"
        elif accuracy_percent <= 100 or wpm <= 100:
            feedback = "You are a pro in typing!"
        else:
            feedback = "You are a typing machine!"

        return render_template("result.html", original=original, typed=typed,
                               accuracy=accuracy_percent, time=time_taken,
                               wpm=wpm, feedback=feedback, mistakes=mistake_count)

    sentence = gen.sentence()
    start_time = time.time()
    return render_template("index.html", sentence=sentence, start_time=start_time)

if __name__ == "__main__":
    app.run(debug=True)
