import os
import requests

SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL").rstrip("/")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_API_PASSWORD = os.getenv("SHOPIFY_API_PASSWORD")

def create_shopify_product(product):
    api_url = f"{SHOPIFY_STORE_URL}/admin/api/2024-01/products.json"
    buy_link = product.get("product_url", "#")

    payload = {
        "product": {
            "title": product["title"],
            "body_html": f"<a href='{buy_link}' target='_blank'>Buy 
Now</a><br>{product.get('description', '')}",
            "images": [{"src": product["image"]}] if product.get("image") 
else [],
            "variants": [{
                "price": product.get("price", "0.00"),
                "inventory_quantity": 0,
                "inventory_management": None
            }],
            "status": "active"
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, auth=(SHOPIFY_API_KEY, 
SHOPIFY_API_PASSWORD), json=payload, headers=headers)

    if response.status_code == 201:
        print(f"✅ Created Shopify product: {product['title']}")
    elif response.status_code == 422:
        print(f"⚠️ Shopify product might already exist: 
{product['title']}")
    else:
        print(f"❌ Failed to create product: {product['title']} - 
{response.text}")

