# Python Testing Demo (Unit Tests + Coverage)

A tiny Python app with unit tests using `pytest` and coverage using `pytest-cov` / `coverage.py`.

## Project layout
```
python_testing_demo/
├─ app/
│  ├─ __init__.py
│  ├─ bank.py
│  └─ utils.py
├─ tests/
│  ├─ test_bank.py
│  └─ test_utils.py
├─ .coveragerc
├─ requirements.txt
└─ README.md
```

## Quick start (CLI)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run tests
pytest -q

# run tests with coverage (terminal summary + missing lines)
pytest --cov=app --cov-report=term-missing

# create HTML report in htmlcov/ and open it in a browser
coverage html
# then open htmlcov/index.html
```

### What to show your class
- Break a test on purpose to demo **fast feedback**.
- Add a new branch in `bank.withdraw` to show how **branch coverage** moves.
- Use `pytest -k fibonacci -q` to run just a subset.
- Use `-vv` to make output more verbose.
- Show the HTML report for a visual of line-by-line coverage.

## PyCharm Coverage
1. Open the folder as a project.
2. Right-click the **tests** directory → **Run 'pytest in tests' with Coverage**.
3. View **Run** tool window → **Coverage** tab to see % per file.
4. Double-click a file to see green/red gutters for executed/missed lines.
5. Re-run after a code change to show regression protection.

## Notes
- Tests use **parametrization** and **error handling** paths to increase coverage.
- `Account.transfer` test includes a type guard example.
```

Happy testing!
