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
            'rarity': 'common'
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

print("=== Player Inventory System ===")
count = 0
inventory_value = 0
item_count = 0


def Inventory(player_name):
    for item_name, quantity in data['players'][player_name]['items'].items():
        
        item_info = data['catalog']
        item_type = item_info[item_name]['type']
        item_value = item_info[item_name]['value']
        item_rarity = item_info[item_name]['rarity']
        
        print(f"{item_name} ({item_type}, {item_rarity}): {quantity}x @ {item_value} gold each = {item_value * quantity} gold")
        # print(f"{item_name} ({data['catalog'][item_name]}, ) {quantity}")


Inventory('alice')