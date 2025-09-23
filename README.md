# Don’tJustWarnMe

Don’tJustWarnMe is a Visual Studio Code extension that integrates a custom-trained neural network to automatically detect and correct common Python code errors. Unlike conventional linters or IDE warnings, this project provides real-time correction suggestions, enabling developers to focus on logic and higher-level design rather than routine syntax and structural mistakes.

## Abstract

This tool operates locally and in real time. As a user edits Python files in VS Code, the extension communicates with a Flask-hosted model to analyze code, identify evident mistakes (syntax and minor structural errors), and propose automated fixes. The objective is to reduce time spent on trivial debugging while ensuring the system does not depend on external services or internet access.

## Features

- Real-time detection of syntactic and structural Python errors
- Automated suggestions to correct common mistakes
- Local execution with no cloud or external API requirements
- VS Code extension written in TypeScript
- Backend service built with Python and Flask
- Transformer-based model trained on pairs of buggy and corrected code

## Tech Stack

- **Frontend:** Visual Studio Code extension (Node.js, TypeScript)
- **Backend:** Flask (Python)
- **Model:** Transformer-based architecture (PyTorch)
- **Dataset:** Curated and synthetically generated buggy-to-fixed pairs
- **Execution:** Local host; inference runs without network connectivity

## Prerequisites

- Visual Studio Code (latest stable version)
- Python 3.10 or newer
- Node.js 18 or newer
- npm or yarn

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnikethMungara/DontJustWarnMe.git
   cd DontJustWarnMe
   ```

2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the extension (frontend):
   ```bash
   cd ../extension
   npm install
   ```

4. Run the VS Code extension:
   - Open the `extension/` folder in Visual Studio Code.
   - Press **F5** to launch the Extension Development Host.

## Usage

Open a Python file in the VS Code Extension Host. The extension will automatically highlight and suggest fixes for common coding errors, which can be reviewed and applied directly in the editor.

## Project Structure

```text
DontJustWarnMe/
├── backend/        # Flask service, model inference, training scripts
├── extension/      # VS Code extension (TypeScript, client side)
├── dataset/        # Buggy-to-fixed code sample pairs
├── model/          # Model architecture, training & checkpoint files
├── README.md       # This file
└── LICENSE         # License file (if added)
```

## Roadmap

- Expand training dataset to 20,000+ samples
- Improve model accuracy and reduce false positives
- Add user-configurable fix policies
- Explore support for additional programming languages

## Contributing

Contributions are welcome. To propose improvements, add features, or report bugs:
1. Open an issue describing the bug or requested feature.
2. Fork the repository and create a feature branch.
3. Submit a pull request for review.

Please ensure proposed changes follow existing style conventions and include tests where applicable.

## License

This project is currently unlicensed. Usage, modification, and distribution are permitted, but no warranties are provided. If broader public use is intended, consider adding a standard open-source license (e.g., MIT or Apache-2.0).

## About the Author

**Aniketh Mungara**  
Arizona State University  
Bachelor of Science in Computer Science  
Minors in Data Science & Business
