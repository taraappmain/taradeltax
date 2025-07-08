# smart_tags.py

def generate_tags(title):
    keywords = ["vitamin", "supplement", "energy", "capsule", "immune", 
"organic"]
    return [kw for kw in keywords if kw.lower() in title.lower()]

def apply_price_strategy(price_str):
    try:
        price = float(price_str.replace("US$", "").strip())
        return f"{round(price * 1.15, 2):.2f}"  # 15% markup
    except Exception:
        return price_str

