from dotenv import load_dotenv
load_dotenv()

from fetch_amazon import fetch_products
from shopify_connector_amazon import create_shopify_product

def main():
    products = fetch_products()
    for product in products:
        create_shopify_product(product)

if __name__ == "__main__":
    main()

