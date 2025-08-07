#!/bin/bash

# Check if project name is passed
if [ -z "$1" ]; then
  echo "❌ Please provide the same project title you used earlier. (e.g., \"Day 05 - Password Generator\")"
  exit 1
fi

# Convert title into folder name
folder_name=$(echo "$1" | sed -E 's/[ -]+/_/g')

# Pull latest changes
git pull origin main

# Stage only that folder
git add "$folder_name"

# Commit and push
git commit -m "Add $1 Project"
git push origin main

echo "✅ Successfully pushed $folder_name to GitHub!"