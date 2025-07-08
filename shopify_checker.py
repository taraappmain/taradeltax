import os
import requests

# Load credentials from environment variables
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL", 
"https://tarasupp.myshopify.com")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

def check_shopify_credentials():
    print("🔍 Checking Shopify product list...")

    if not SHOPIFY_ACCESS_TOKEN:
        print("❌ Missing Shopify access token. Please set 
SHOPIFY_ACCESS_TOKEN as an environment variable.")
        return

    url = f"{SHOPIFY_STORE_URL}/admin/api/2024-01/products.json"
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        print(f"✅ Found {len(products)} product(s) in Shopify.")
        for p in products:
            print(f"→ {p['title']} | ID: {p['id']}")
    else:
        print("❌ Shopify API call failed.")
        print(f"→ Status: {response.status_code}")
        print("→ Response:", response.text)

if __name__ == "__main__":
    check_shopify_credentials()

