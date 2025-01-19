from selenium.webdriver.common.by import By


class Locators:
    BUTTON_LOGIN_IN_ACCOUNT_MAIN_PAGE = (By.XPATH,'//button [@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]') #Кнопка Войти в аккаунт на главной странице
    LINK_FOR_REGISTRATION_ON_LOGIN_PAGE = (By.XPATH, "//a [@href='/register']") #Ссылка на регистрацию странице авторизации
    NAME_FOR_REGISTRATION = (By.XPATH,'(//input [@name="name"])[1]')#Ввод Имя для регистрации
    EMAIL_FOR_REGISTRATION =  (By.XPATH,'(//input [@name="name"])[2]')#Ввод Емайл для регистрации
    PASSWORD_FOR_REGISTRATION = (By.XPATH,'//input [@name="Пароль"]')#Ввод Пароль для регистрации
    TITLE_FOR_PAGE_LOGIN = (By.XPATH,"//*[text()='Вход']")#
    REGISTRATION_BUTTON = (By.XPATH,'//button [@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ERROR_FOR_INCORRECT_PASSWORD = (By.XPATH,'//p [@class="input__error text_type_main-default"]') #ошибка о неверном пароле
    NAME_FOR_LOGIN = (By.XPATH,'//input [@name="name"]')# Имя пользователя страница для авторизации
    PASSWORD_FOR_LOGIN = (By.XPATH,'//input [@name="Пароль"]') # Пароль пользователя страница для авторизации
    BUTTON_LOGIN_IN_AUTORIZATION_PAGE = (By.XPATH,'//button [@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')#Кнопка войти на странице авторизации
    BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE = (By.XPATH,'//*[@id="root"]/div/header/nav/a/p') #Кнопка личный кабинет на главной странице
    LINK_LOGIN_ON_REGISTRATIONS_PAGE = (By.XPATH,'//a [@class="Auth_link__1fOlj"]') #Ссылка "Войти" для авторизации на странице регистрации
    LINK_FORGOT_PASSWORD_ON_AUTORIZATION_PAGE=(By.XPATH,'//a [@class="Auth_link__1fOlj" and @href="/forgot-password"]') #Ссылка на страницу восстановления пароля
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH,'//p [text()="Личный Кабинет"]')#Кнопка Личный кабинет после авторизации
    BUTTON_PROFILE=(By.XPATH,'//a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9" ]')#Кнопка профиль в личном кабинете
    BUTTON_CONSTRUCTOR = (By.XPATH,'//p [@class="AppHeader_header__linkText__3q_va ml-2" and text()= "Конструктор"]') #Кнопка Конструктор
    BUTTON_ORDER_FEED = (By.XPATH,'//p [@class="AppHeader_header__linkText__3q_va ml-2" and text()= "Лента Заказов"]') #Кнопка Лента заказов
    BUTTON_MAKE_ORDERS= (By.XPATH,'//Button [text()="Оформить заказ"]')#Кнопка оформить заказ на главной странице
    LOGO_PAGE_PERSONAL_ACCOUNT = (By.XPATH ,'//div [@class="AppHeader_header__logo__2D0X2"]') # Лого в личном кабинете
    BUTTON_EXIT_FROM_PERSONAL_ACCOUNT = (By.XPATH,'//button [@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    LINK_SAUCES_CONSTRUCTOR = (By.XPATH ,'//span[text()="Соусы"]')#Вкладка Соусы в Конструкторе
    LINK_BUNS_CONSTRUCTOR=(By.XPATH,'//span[text()="Булки"]')#Вкладка Булки в Конструкторе
    LINK_FILLING_CONSTRUCTOR=(By.XPATH,'//span[text()="Начинки"]')#Вкладка Начинки в Конструкторе
    FIRST_SAUCE = (By.XPATH,'//p [@class="BurgerIngredient_ingredient__text__yp3dH"][1]')
    FIRST_BUNS = (By.XPATH , '// p[@class ="BurgerIngredient_ingredient__text__yp3dH"][1]')
    FIRST_FILLING = (By.XPATH, '// p[@class ="BurgerIngredient_ingredient__text__yp3dH"][1]')