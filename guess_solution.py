from aluLib import *

card_width = 100
card_height = 145
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

cards = ['A', 'A', 'K', 'J', '2', 'K', 'J', '2', '5', '5']
state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
start_x = 50
start_y = 50
offset = 50
turned_cards = 0


def draw_cards():
    for i in range(0, len(cards)):
        x_pos = start_x + (i%5) * (card_width + offset)
        y_pos = start_y if i < len(cards)/2 else start_y + card_width + offset

        if state[i] == 0:
            enable_stroke()
            set_fill_color(0, 0, 1)
            draw_rectangle(x_pos, y_pos, card_width, card_height)
        elif state[i] == 1:
            image_file = load_image('assets/'+cards[i])
            draw_image(image_file, x_pos, y_pos)
        elif state[i] == 2:
            disable_stroke()
            set_fill_color(1, 1, 1)
            draw_rectangle(x_pos, y_pos, card_width, card_height)


def check_card_state():
    global state, turned_cards
    if turned_cards == 2:
        card1_index = state.index(1)
        for i in range(card1_index + 1, len(cards)):
            if state[i] == 1:
                card2_index = i
                break

        if cards[card1_index] == cards[card2_index]:
            state[card1_index] = 2
            state[card2_index] = 2
        else:
            state[card1_index] = 0
            state[card2_index] = 0

        turned_cards = 0
    # If there are 2 cards that are flipped
    # compare them
    # If they are the same, put them in state 2
    # Else, put them back to state 0


def check_mouse_input():
    global state, turned_cards

    if is_mouse_pressed():
        clicked_x = mouse_x()
        clicked_y = mouse_y()

        for i in range(0, len(cards)):
            card_x_pos = start_x + (i % 5) * (card_width + offset)
            card_y_pos = start_y if i < len(cards) / 2 else start_y + card_width + offset

            check_x = card_x_pos <= clicked_x <= card_x_pos + card_width
            check_y = card_y_pos <= clicked_y <= card_y_pos + card_height
            if check_x and check_y and state[i] == 0:
                state[i] = 1
                turned_cards += 1


def main():
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)
