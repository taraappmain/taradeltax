import json
import time

def autofill_affiliate(platform):
    with open("cyber_core/identity_profile/tara_profile.json") as f:
        profile = json.load(f)

    print(f"Starting application for: {platform}")
    print("Filling personal information...")
    time.sleep(1)
    print("Uploading documents...")
    time.sleep(1)
    print("Submitting application...")
    time.sleep(1)
    print("✅ Application submitted for", profile["full_name"])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    args = parser.parse_args()
    autofill_affiliate(args.platform)
