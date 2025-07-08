from go_supps_connector import fetch_go_supps_products

if __name__ == "__main__":
    print(">>> Running GoSupps scrape test...")
    products = fetch_go_supps_products()
    if not products:
        print(">>> No products found.")
    else:
        for p in products:
            print(p)

