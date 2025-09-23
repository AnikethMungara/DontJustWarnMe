from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from pathlib import Path

from pathlib import Path

# 🛠️ Correct the model path relative to backend/app/model/inference.py
MODEL_PATH = Path(__file__).resolve().parents[3] / "model_training" / "saved_model"

def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(str(MODEL_PATH), local_files_only=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(str(MODEL_PATH), local_files_only=True)
    return tokenizer, model


def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH, local_files_only=True)
    return tokenizer, model

def fix_code(code_snippet, tokenizer, model):
    inputs = tokenizer(
        code_snippet,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=256
    )
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,          # Enable sampling instead of greedy decoding
            top_k=50,                # Top-k sampling to reduce repetition
            temperature=0.8          # Slight randomness
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
