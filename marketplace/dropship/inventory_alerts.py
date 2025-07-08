def check_inventory_changes(previous, current):
    changes = []
    for p_old, p_new in zip(previous, current):
        if p_old['price'] != p_new['price']:
            changes.append((p_old['title'], p_old['price'], p_new['price']))
    return changes