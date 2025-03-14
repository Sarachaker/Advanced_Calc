# Create the project folder
mkdir midterm-2024-calc
cd midterm-2024-calc

# Create the folder structure
mkdir -p app tests data .github/workflows

# Create the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pandas pytest pylint

# Create initial files
touch app/__init__.py app/calculator.py app/history_manager.py app/plugin_system.py app/repl.py
touch tests/__init__.py tests/test_calculator.py tests/test_history_manager.py tests/test_plugins.py
touch data/history.csv .github/workflows/ci.yml .coveragerc .pylintrc logging.conf main.py pytest.ini README.md requirements.txt
