from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def search_location_keyboard() -> InlineKeyboardMarkup:
    """
    Returns an inline keyboard with preset Nigerian city buttons.
    Shown after the user types /search so they can pick a city quickly
    instead of typing it manually.

    Returns:
        InlineKeyboardMarkup: A 2-column grid of city buttons
    """
    buttons = [
        [
            InlineKeyboardButton("Lagos", callback_data="search_Lagos"),
            InlineKeyboardButton("Abuja", callback_data="search_Abuja"),
        ],
        [
            InlineKeyboardButton("Kano", callback_data="search_Kano"),
            InlineKeyboardButton("Kaduna", callback_data="search_Kaduna"),
        ],
        [
            InlineKeyboardButton("Port Harcourt", callback_data="search_Port_Harcourt"),
            InlineKeyboardButton("Remote", callback_data="search_Remote"),
        ],
    ]

    return InlineKeyboardMarkup(buttons)