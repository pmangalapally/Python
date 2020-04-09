def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v), ' ', k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    #print("test")
    count = 0
    # your code goes here
    for i in addedItems:
        #print(i)
        count = inventory.setdefault(i, 0)
        inventory[i] = count + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
