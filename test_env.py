import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env from current directory

print("SHOPIFY_STORE_URL =", os.getenv("SHOPIFY_STORE_URL"))
print("SHOPIFY_API_KEY =", os.getenv("SHOPIFY_API_KEY"))

