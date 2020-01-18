# Write a function named displayInventory() that would take any possible
# “inventory” and display it like the following:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62


inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print('Inventory:')
    totalnumber = 0
    for a, b in inventory.items():
        totalnumber += b
        print(str(b), a )
    print('Total number of items:', totalnumber)

#displayInventory(inventory)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1

        else:
            inventory[i] = 1
    return inventory

inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)