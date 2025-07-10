import os

AFFILIATE_TAG = os.getenv("AMAZON_AFFILIATE_TAG", "tara0b6-20")
AMAZON_REGION = os.getenv("AMAZON_REGION", "com")
SEARCH_KEYWORD = os.getenv("AMAZON_SEARCH_KEYWORD", "electronics")

def fetch_products():
    # Placeholder: implement Amazon Product Advertising API or scraping 
here.
    # For now, returning a dummy product list.

    products = [
        {
            "title": "Example Amazon Product",
            "description": "High-quality product from Amazon",
            "price": "29.99",
            "image": 
"https://images-na.ssl-images-amazon.com/images/I/sample.jpg",
            "product_url": 
f"https://www.amazon.{AMAZON_REGION}/dp/B000000?tag={AFFILIATE_TAG}"
        }
    ]
    print(f"✅ Total products fetched from Amazon: {len(products)}")
    return products

