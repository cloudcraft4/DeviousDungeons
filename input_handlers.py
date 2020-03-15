import libtcodpy as libtcod

from game_states import GameStates

from game_messages import Message


def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.TARGETING:
        return handle_targeting_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key)
    elif game_state == GameStates.GAIN_SKILL:
        return handle_gain_skill_menu(key)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key)
    elif game_state == GameStates.SHOW_SKILL:
        return handle_show_skill_list(key)

    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key.vk == libtcod.KEY_KP8 or key.vk == libtcod.KEY_8:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key.vk == libtcod.KEY_KP2 or key.vk == libtcod.KEY_2:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key.vk == libtcod.KEY_KP4 or key.vk == libtcod.KEY_4:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key.vk == libtcod.KEY_KP6 or key.vk == libtcod.KEY_6:
        return {'move': (1, 0)}
    elif key.vk == libtcod.KEY_HOME or key.vk == libtcod.KEY_KP7 or key.vk == libtcod.KEY_7:
        return {'move': (-1, -1)}
    elif key.vk == libtcod.KEY_PAGEUP or key.vk == libtcod.KEY_KP9 or key.vk == libtcod.KEY_9:
        return {'move': (1, -1)}
    elif key.vk == libtcod.KEY_END or key.vk == libtcod.KEY_KP1 or key.vk == libtcod.KEY_1:
        return {'move': (-1, 1)}
    elif key.vk == libtcod.KEY_PAGEDOWN or key.vk == libtcod.KEY_KP3 or key.vk == libtcod.KEY_3:
        return {'move': (1, 1)}
    elif key.vk == libtcod.KEY_KP5 or key.vk == libtcod.KEY_5:
        return {'wait': True}

    if key_char == 'g':
        return {'pickup': True}

    elif key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 's':
        return {'show_skill': True}

    elif key_char == 'd':
        return {'drop_inventory': True}

    elif key.vk == libtcod.KEY_ENTER:
        return {'take_stairs': True}

    elif key_char == 'c':
        return {'show_character_screen': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}


def handle_targeting_keys(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key):
    key_char = chr(key.c)

    if key_char == 'i':
        return {'show_inventory': True}

    if key_char == 's':
        return {'show_skill': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_main_menu(key):
    key_char = chr(key.c)

    if key_char == 'a':
        return {'new_game': True}
    elif key_char == 'b':
        return {'load_game': True}
    elif key_char == 'c' or key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_level_up_menu(key):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            return {'level_up': 'hp'}
        elif key_char == 'b':
            return {'level_up': 'str'}
        elif key_char == 'c':
            return {'level_up': 'def'}

    return {}

def handle_gain_skill_menu(key):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            return {'gain_skill': 'Firebreath'}
        elif key_char == 'b':
            return {'gain_skill': 'Thorn Armor'}
        elif key_char == 'c':
            return {'gain_skill': 'Regeneration'}

    return {}

def handle_show_skill_list(key):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            Message('You have used ability under A slot', libtcod.blue)
            return {}
        elif key_char == 'b':
            Message('You have used ability under B slot', libtcod.blue)
            return {}
        elif key_char == 'c':
            Message('You have used ability under C slot', libtcod.blue)
            return {}

    return {}


def handle_character_screen(key):
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    return {}


def handle_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)

    if mouse.lbutton_pressed:
        return {'left_click': (x, y)}
    elif mouse.rbutton_pressed:
        return {'right_click': (x, y)}

    return {}
