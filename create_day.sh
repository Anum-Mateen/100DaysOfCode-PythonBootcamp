#!/bin/bash

# Check if project name is passed
if [ -z "$1" ]; then
  echo "❌ Please provide a project title (e.g., \"Day 05 - Password Generator\")"
  exit 1
fi

# Replace spaces and dashes with underscores for folder naming
folder_name=$(echo "$1" | sed -E 's/[ -]+/_/g')

# Create the folder and move inside
mkdir "$folder_name"
cd "$folder_name"

# Create files
touch README.md
touch main.py

# Optional: Pre-fill README.md with title
echo "# $1" > README.md

# Open in VS Code (only if 'code' is available)
if command -v code &> /dev/null; then
  code .
else
  echo "📁 Project created: $folder_name (open manually if VS Code not available)"
fi