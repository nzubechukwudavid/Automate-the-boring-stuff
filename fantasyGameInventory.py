# fantasy game inventory project
bag = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for key, value in inventory.items():
        print(str(value), key)
        total_items += value
    print("Total number of items:", total_items)


displayInventory(bag)


def addToInventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
