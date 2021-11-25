class Login:
    # locator
    user_name_loc = "//input[@id='user-name']"
    password_loc = "//input[@id='password']"
    login_button_loc = "//input[@id='login-button']"
    add_card_loc = "//div[@class='inventory_list']/child::div[{}]//child::button"
    shopping_bucket_icon_loc = "//a[@class='shopping_cart_link']"
    error_text_loc = "//h3[@data-test='error']"
