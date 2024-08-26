from flask import Flask, render_template, request

app = Flask(__name__)

def get_model_response(model, user_input):
    return "This is a response from the model."

@app.route('/', methods=['GET', 'POST'])
def index():
    models = [
        'gpt-4o-mini-base',
        'gpt-4o-mini-few-shot',
        'gpt-4o-mini-fine-tuned'
    ]
    model1_response = ""
    model2_response = ""

    if request.method == 'POST':
        user_input = request.form.get('user_input')
        model1 = request.form.get('model1')
        model2 = request.form.get('model2')

        model1_response = get_model_response(model1, user_input)
        model2_response = get_model_response(model2, user_input)
    
    return render_template(
        'index.html',
        models=models,
        model1_response=model1_response,
        model2_response=model2_response
    )

if __name__ == '__main__':
    app.run(debug=True)