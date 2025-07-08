import os
import requests
from dotenv import load_dotenv
load_dotenv()

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")
shopify_api_url = f"{SHOPIFY_STORE_URL}/admin/api/2024-04/products.json"
headers = {
    "X-Shopify-Access-Token": SHOPIFY_API_KEY,
    "Content-Type": "application/json"
}

def format_for_shopify(products):
    formatted = []
    for p in products:
        formatted.append({
            "title": p['title'],
            "body_html": f"<img src='{p['image']}' /><p>{p['title']}</p>",
            "vendor": "SkyNova Mart",
            "product_type": "Supplements",
            "variants": [{"price": p['price'].replace('$', '')}]
        })
    return formatted

def push_to_shopify(products):
    for p in products:
        res = requests.post(shopify_api_url, headers=headers, json={"product": p})
        print("Pushed:", res.status_code)