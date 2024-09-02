from flask import Flask, render_template, request

from llm_manager import LLMManager

app = Flask(__name__)
llm_manager = LLMManager()

@app.route('/', methods=['GET', 'POST'])
def index():
    models = ['zero_shot', 'few_shot', 'fine_tuned']
    model1_response = ""
    model2_response = ""
    model1_input = ""
    model2_input = ""
    user_input = ""
    
    if request.method == 'POST':
        print("POST request received")
        user_input = request.form.get('user_input')
        model1_input = request.form.get('model1')
        model2_input = request.form.get('model2')

        model1_response = llm_manager.get_benn_llm_response(model1_input, user_input)
        model2_response = llm_manager.get_benn_llm_response(model2_input, user_input)
    
    return render_template(
        'index.html',
        models=models,
        model1_response=model1_response,
        model2_response=model2_response,
        model1_input=model1_input,
        model2_input=model2_input,
        user_input=user_input
    )

if __name__ == '__main__':
    app.run(debug=True)