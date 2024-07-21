
from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data['code']
    
    # Save code to a temporary file
    with open('temp.cpp', 'w') as f:
        f.write(code)
    
    # Compile and run the C++ code
    try:
        compile_result = subprocess.run(['g++', 'temp.cpp', '-o', 'temp.out'], capture_output=True, text=True)
        if compile_result.returncode != 0:
            return jsonify({'output': compile_result.stderr})
        
        run_result = subprocess.run(['./temp.out'], capture_output=True, text=True)
        return jsonify({'output': run_result.stdout})
    except Exception as e:
        return jsonify({'output': str(e)})
    finally:
        # Clean up the temporary files
        if os.path.exists('temp.cpp'):
            os.remove('temp.cpp')
        if os.path.exists('temp.out'):
            os.remove('temp.out')

if __name__ == '__main__':
    app.run(debug=True)
