import sys
from pathlib import Path
import importlib.util

# Add backend to the Python path (so relative imports work if needed)
backend_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(backend_dir))

# Dynamically load backend/app/__init__.py as "app_module"
app_init_path = backend_dir / "app" / "__init__.py"
spec = importlib.util.spec_from_file_location("app", str(app_init_path))
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

# Use create_app from the dynamically loaded module
app = app_module.create_app()

if __name__ == "__main__":
    app.run(debug=True)
