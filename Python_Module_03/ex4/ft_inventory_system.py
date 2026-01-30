"""Player Inventory Management System.

A simple system to manage player inventories, track items, and perform
transactions between players in a game environment.
"""

data = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1,
                'health_byte': 1,
                'quantum_ring': 3
            },
            'total_value': 1875,
            'item_count': 6
        },
        'bob': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 2
            },
            'total_value': 900,
            'item_count': 5
        },
        'charlie': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1
            },
            'total_value': 350,
            'item_count': 2
        },
        'diana': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 3,
                'health_byte': 3,
                'data_crystal': 3
            },
            'total_value': 4125,
            'item_count': 12
        }
    },
    'catalog': {
        'pixel_sword': {
            'type': 'weapon',
            'value': 150,
            'rarity': 'legendary'
        },
        'quantum_ring': {
            'type': 'accessory',
            'value': 500,
            'rarity': 'rare'
        },
        'health_byte': {
            'type': 'consumable',
            'value': 25,
            'rarity': 'common'
        },
        'data_crystal': {
            'type': 'material',
            'value': 1000,
            'rarity': 'legendary'
        },
        'code_bow': {
            'type': 'weapon',
            'value': 200,
            'rarity': 'uncommon'
        }
    }
}

print("=== Player Inventory System ===\n")


def transaction(pfrom, pto, number, item_name):
    """Transfer items from one player to another.

    Args:
        pfrom: Name of the player giving items
        pto: Name of the player receiving items
        number: Quantity of items to transfer
        item_name: Name of the item being transferred
    """
    print(f"=== Transaction: {pfrom} gives {pto} {number} {item_name} ===")

    if number > data['players'][pfrom]['items'][item_name]:
        print("Transaction Fails!")
    else:
        data['players'][pfrom]['items'][item_name] -= number

        if item_name not in data['players'][pto]['items']:
            data['players'][pto]['items'][item_name] = 0

        data['players'][pto]['items'][item_name] += number
        print("Transaction successful!\n")
        show_update(pfrom, pto, item_name)


def show_update(player1, player2, item_name):
    """Display updated item counts for both players after a transaction.

    Args:
        player1: First player name
        player2: Second player name
        item_name: Name of the item that was transferred
    """
    print("=== Updated Inventories ===")
    count1 = data['players'][player1]['items'][item_name]
    count2 = data['players'][player2]['items'][item_name]
    print(f"{player1} {item_name}s: {count1}")
    print(f"{player2} {item_name}s: {count2}\n")


def must_value():
    """Calculate and display game analytics.

    Shows the most valuable player, player with most items,
    and lists all legendary rarity items.
    """
    max_value = 0
    items_number = 0
    value_player = ""
    items_player = []
    rarity = []

    for player_name, value in data['players'].items():
        player_items = data['players'][player_name]['items']

        if len(player_items) > items_number:
            items_number = len(player_items)
            items_player = [player_name]
        elif len(player_items) == items_number:
            items_player.append(player_name)

        if value['total_value'] > max_value:
            max_value = value['total_value']
            value_player = player_name

    for item, options in data['catalog'].items():
        if options['rarity'] == 'legendary':
            rarity.append(item)

    result = " ".join(items_player)
    ra_result = " ".join(rarity)

    print(f"Most valuable player: {value_player} ({max_value} gold)")
    print(f"Most items: {result} ({items_number} items)")
    print(f"Rarest items: {ra_result}")


def inventory(player_name):
    """Display detailed inventory for a specific player.

    Shows all items owned by the player with their type, rarity,
    quantity, and total value. Also displays overall statistics
    and item categories.

    Args:
        player_name: Name of the player whose inventory to display
    """
    print(f"=== {player_name}'s Inventory ===")
    categories = ""
    types_data = {
        "weapon": 0,
        "accessory": 0,
        "consumable": 0,
        "material": 0
    }

    for item_name, quantity in data['players'][player_name]['items'].items():
        item_info = data['catalog']
        item_type = item_info[item_name]['type']
        item_value = item_info[item_name]['value']
        item_rarity = item_info[item_name]['rarity']
        total_item_value = item_value * quantity

        print(f"{item_name} ({item_type}, {item_rarity}): "
              f"{quantity}x @ {item_value} gold each = "
              f"{total_item_value} gold")

        types_data[item_type] += 1

    first = True
    for item_type, count in types_data.items():
        if count > 0:
            if not first:
                categories += ", "
            categories += f"{item_type}({count})"
            first = False

    total_value = data['players'][player_name]['total_value']
    item_count = data['players'][player_name]['item_count']

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {item_count} items")
    print(f"Categories: {categories}\n")

    transaction('diana', 'alice', 1, 'code_bow')

    print("=== Inventory Analytics ===")
    must_value()


inventory('diana')
