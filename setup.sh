#!/bin/bash
set -e

echo "Installing dependencies..."
pip install requests beautifulsoup4 datasette sqlite_utils

echo "Converting CSV to SQLite database..."
python -m sqlite_utils insert alerts.db alerts scrapers/alerts.csv --csv --detect-types

echo "Setup complete. To launch the Datasette web interface, run:"
echo "  python -m datasette alerts.db"
