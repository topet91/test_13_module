purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(p['price'] * p['quantity'] for p in purchases)

def items_by_category(purchases):
    categories = {}
    for p in purchases:
        categories.setdefault(p['category'], set()).add(p['item'])
    return {cat: sorted(list(items)) for cat, items in categories.items()}

def expensive_purchases(purchases, min_price):
    return [p for p in purchases if p['price'] >= min_price]

def average_price_by_category(purchases):
    sums = {}
    counts = {}
    for p in purchases:
        cat = p['category']
        sums[cat] = sums.get(cat, 0) + p['price']
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(sums[cat] / counts[cat], 2) for cat in sums}

def most_frequent_category(purchases):
    quantities = {}
    for p in purchases:
        quantities[p['category']] = quantities.get(p['category'], 0) + p['quantity']
    return max(quantities, key=quantities.get)

if __name__ == "__main__":
    min_price = 1.0
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
