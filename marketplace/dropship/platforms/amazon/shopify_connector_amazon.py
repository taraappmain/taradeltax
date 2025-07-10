import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL", "").rstrip("/")
SHOPIFY_API_PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")

def create_shopify_product(product):
    api_url = f"{SHOPIFY_STORE_URL}/admin/api/2024-01/products.json"

    body_html = (
        f"<a href='{product['product_url']}' target='_blank'>"
        f"Buy on Amazon</a><br><p>{product['description']}</p>"
    )

    payload = {
        "product": {
            "title": product["title"],
            "body_html": body_html,
            "images": [{"src": product["image"]}],
            "variants": [{
                "price": product["price"],
                "inventory_quantity": 0,
                "inventory_management": None
            }],
            "status": "active"
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_API_PASSWORD
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"✅ Uploaded: {product['title']}")
    else:
        print(f"❌ Failed: {product['title']}")
        print(f"→ {response.status_code}: {response.text}")

