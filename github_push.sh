#!/bin/bash

# GitHub Push Script for Tara Unified System

# Optional commit message from user
MESSAGE=${1:-"Update: Global affiliate injection + sync with unified 
backend/dashboard"}

# Navigate to project root (edit path if needed)
cd ~/Desktop/"TaraApp Main" || {
  echo "❌ Project folder not found. Check path."
  exit 1
}

# Initialize Git (if not already)
if [ ! -d ".git" ]; then
  echo "🔧 Initializing Git..."
  git init
  git branch -M main
  git remote add origin https://github.com/tarasaudi/taramain.git
fi

# Stage and commit
echo "📦 Staging all changes..."
git add .

echo "📝 Committing with message: $MESSAGE"
git commit -m "$MESSAGE"

# Push to GitHub
echo "🚀 Pushing to GitHub main branch..."
git push -u origin main

echo "✅ Push complete!"

