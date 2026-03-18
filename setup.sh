#!/bin/bash
set -e

echo "Installing dependencies..."
pip install requests beautifulsoup4 datasette sqlite_utils

echo "Converting CSV to SQLite database..."
sqlite-utils insert alerts.db alerts all_sanctions.csv --csv --detect-types

echo "Setup complete. To launch the Datasette web interface, run:"
echo "  python -m datasette alerts.db"
