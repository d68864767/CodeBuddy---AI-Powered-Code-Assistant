```python
import openai
from openai.api_resources.completion import Completion

class DocGenerator:
    def __init__(self):
        self.openai_api_key = 'your_openai_api_key'
        openai.api_key = self.openai_api_key

    def generate(self, data):
        try:
            code = data['code']
            prompt = f"Generate documentation for the following code:\n{code}\n"
            response = Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=200)
            documentation = response.choices[0].text.strip()
            return {'status': 'success', 'documentation': documentation}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
```
