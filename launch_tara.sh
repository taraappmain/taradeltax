#!/bin/bash
# Launch Tara Unified Dashboard

cd "$(dirname "$0")/marketplace/dashboard" || exit
streamlit run tara_unified_dashboard.py

