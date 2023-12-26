```python
from flask import Flask, request, jsonify
from code_generation import CodeGenerator
from debugging_assistant import DebuggingAssistant
from code_explanation import CodeExplain
from documentation_generator import DocGenerator
from learning_support import LearningSupport
from code_optimizer import CodeOptimizer
from database import Database

app = Flask(__name__)

# Initialize all the classes
code_gen = CodeGenerator()
debug_assist = DebuggingAssistant()
code_explain = CodeExplain()
doc_gen = DocGenerator()
learn_support = LearningSupport()
code_opt = CodeOptimizer()
db = Database()

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.get_json()
    result = code_gen.generate(data)
    return jsonify(result)

@app.route('/debug_code', methods=['POST'])
def debug_code():
    data = request.get_json()
    result = debug_assist.debug(data)
    return jsonify(result)

@app.route('/explain_code', methods=['POST'])
def explain_code():
    data = request.get_json()
    result = code_explain.explain(data)
    return jsonify(result)

@app.route('/generate_doc', methods=['POST'])
def generate_doc():
    data = request.get_json()
    result = doc_gen.generate(data)
    return jsonify(result)

@app.route('/learn_support', methods=['POST'])
def learn_support():
    data = request.get_json()
    result = learn_support.support(data)
    return jsonify(result)

@app.route('/optimize_code', methods=['POST'])
def optimize_code():
    data = request.get_json()
    result = code_opt.optimize(data)
    return jsonify(result)

@app.route('/store_query', methods=['POST'])
def store_query():
    data = request.get_json()
    result = db.store(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
```
