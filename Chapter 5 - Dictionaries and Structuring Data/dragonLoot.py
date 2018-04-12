# Practical project from Chapter 5, creating an inventory system to show a list of items in the user's possession.
# The code adds dropped items from monster into the user's inventory.

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'ruby', 'ruby', 'diamond', 'fangs']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Function counts the total amount of items in the user's inventory.
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' ' + k)
        item_total = item_total + v
    print('Total number of items: ' + str(item_total))

# Function adds drops from enemies into user's inventory.
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in list(inventory.keys()):
            inventory.setdefault(addedItems[i], 0)
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1
        else:
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    return(inventory)

# Shows inventory before dropped items are added into inventory.
print('Inventory BEFORE slaying monster:')
displayInventory(stuff)
print('')

# Calls addToInventory function to add dropped loot into user's inventory.
inv = addToInventory(stuff, dragonLoot)

# Show inventory after items are added.
print('Inventory AFTER slaying monster:')
displayInventory(inv)


# Comment:
# - Added a system that asks for user input to access the inventory. Code shown below.

##while True:
##    inventory = (input().lower()).rstrip('?.,!@~#$%^&*()_+{}|:"<>?[]\;/') # Uppercase to lowercase.
##    if inventory == 'inventory':
##        displayInventory(inv)
##        break
##    else:
##        break
