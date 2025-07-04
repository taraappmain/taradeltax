
import os
import zipfile

BASE_DIR = os.path.abspath("TaraApp Main")
MARKETPLACE = os.path.join(BASE_DIR, "marketplace")
CRYPTO = os.path.join(MARKETPLACE, "crypto")
DASHBOARD = os.path.join(MARKETPLACE, "dashboard")
UPDATER = os.path.join(BASE_DIR, "updater")

def ensure_dirs():
    os.makedirs(CRYPTO, exist_ok=True)
    os.makedirs(DASHBOARD, exist_ok=True)
    os.makedirs(UPDATER, exist_ok=True)

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)

def generate_files():
    print("📁 Writing system files...")

    write_file(os.path.join(BASE_DIR, "launch_tara.sh"), """#!/bin/bash
echo "🛸 Launching Tara Delta Dashboard..."
cd "$(dirname "$0")/marketplace"
streamlit run dashboard/tara_unified_dashboard.py
""")
    os.chmod(os.path.join(BASE_DIR, "launch_tara.sh"), 0o755)

    write_file(os.path.join(BASE_DIR, "requirements.txt"), """streamlit
pandas
matplotlib
requests
""")

    write_file(os.path.join(BASE_DIR, "version.txt"), "1.0.0-delta")

    write_file(os.path.join(UPDATER, "update_stub.py"), """import time, os
def check_for_updates():
    print("🔍 Checking for updates...")
    time.sleep(1)
    print("✅ Tara is up to date. Version:", get_version())

def get_version():
    try:
        with open(os.path.join(os.path.dirname(__file__), '..', 'version.txt')) as f:
            return f.read().strip()
    except:
        return "unknown"

if __name__ == "__main__":
    check_for_updates()
""")

    write_file(os.path.join(BASE_DIR, ".gitignore"), """__pycache__/
.env/
*.log
*.pyc
*.db
*.DS_Store
TaraDeltaInstaller.pkg
*.zip
env/
""")

def zip_build():
    zip_path = os.path.join(os.path.dirname(BASE_DIR), "TaraDelta_FullBuild.zip")
    print(f"🗜️  Creating ZIP: {zip_path}")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(BASE_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(BASE_DIR))
                zipf.write(full_path, rel_path)
    print("✅ ZIP completed!")

def main():
    print("🚀 Starting Tara Delta Build Process...")
    ensure_dirs()
    generate_files()
    zip_build()
    print("🎉 All done. Launch with ./launch_tara.sh or unzip the build anywhere.")

if __name__ == "__main__":
    main()
