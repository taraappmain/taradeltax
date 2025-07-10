import os
from dotenv import load_dotenv
import requests
from go_supps_connector import fetch_go_supps_products

load_dotenv()

SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")

products = fetch_go_supps_products()

if not products:
    print("❌ No products were fetched from GoSupps.")
    exit()

print(f"✅ Uploading {len(products)} products to Shopify...")

for product in products:
    payload = {
        "product": {
            "title": product["title"],
            "body_html": f"<img src='{product['image']}' />",
            "vendor": "GoSupps",
            "product_type": "Supplements",
            "images": [{"src": product["image"]}],
            "variants": [{
                "price": product["price"].replace("US$", "").replace("$", "").strip(),
                "inventory_quantity": 10
            }]
        }
    }

    res = requests.post(
        f"{SHOPIFY_STORE_URL}/admin/api/2024-01/products.json",
        headers={
            "X-Shopify-Access-Token": SHOPIFY_API_KEY,
            "Content-Type": "application/json"
        },
        json=payload
    )

    if res.status_code == 201:
        print(f"✅ Uploaded: {product['title']}")
    else:
        print(f"❌ Failed to upload: {product['title']}")
        print("→", res.status_code, res.text)
