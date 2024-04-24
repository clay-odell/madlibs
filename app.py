from flask import Flask, render_template, request
from stories import story

app = Flask(__name__) 

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html", prompts=story.prompts)

@app.route("/story", methods=["POST"])
def story_view():
    # Get user answers from the form
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    # Generate completed story
    completed_story = story.generate(answers)
    return render_template("story.html", story=completed_story)
if __name__ == "__main__":
    app.run(debug=True)