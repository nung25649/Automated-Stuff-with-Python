def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for key in sorted(inventory.keys()):
        num = inventory[key]
        print(str(num) + ' ' + key)
        total += num
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)