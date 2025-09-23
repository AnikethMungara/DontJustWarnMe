# run_tests.py
import sys
from pathlib import Path

# Add backend directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent / "backend"))

from app.model.inference import load_model_and_tokenizer, fix_code

# Load model
tokenizer, model = load_model_and_tokenizer()

# Test cases
test_cases = [
    ("pritn('Hello')", "print('Hello')"),
    ("def add(a, b)\n    return a + b", "def add(a, b):\n    return a + b"),
    ("x = input('Enter: ')\nprint(x + 1)", "x = int(input('Enter: '))\nprint(x + 1)"),
    ("for i in range(5):\nprint(i)", "for i in range(5):\n    print(i)"),
    ("reutrn x", "return x"),
    ("if x == 10\n    print('yes')", "if x == 10:\n    print('yes')"),
    ("if x = 5:\n    print('ok')", "if x == 5:\n    print('ok')"),
    ("def foo():\nprint('hi')", "def foo():\n    print('hi')"),
    ("data = np.array([1, 2])", "import numpy as np\ndata = np.array([1, 2])"),
    ("result = (a + b", "result = (a + b)"),
]

# Run
for i, (buggy, expected) in enumerate(test_cases, 1):
    print(f"Test {i}")
    print("Buggy:\n", buggy)
    print("Expected:\n", expected)
    fixed = fix_code(buggy, tokenizer, model)
    print("Model Output:\n", fixed)
    print("-" * 60)
