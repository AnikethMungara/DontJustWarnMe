from flask import Blueprint, request, jsonify
from app.model.inference import load_model_and_tokenizer, fix_code

api = Blueprint("api", __name__)
tokenizer, model = load_model_and_tokenizer()

@api.route("/fix_code", methods=["POST"])
def fix_code_route():
    data = request.get_json()
    buggy_code = data.get("code", "")
    if not buggy_code.strip():
        return jsonify({"error": "No code provided"}), 400

    fixed = fix_code(buggy_code, tokenizer, model)
    return jsonify({"fixed_code": fixed})
