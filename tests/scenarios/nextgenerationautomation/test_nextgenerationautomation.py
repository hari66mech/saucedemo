from pytest_bdd import scenarios, when, then, parsers
from pageobjectmodel.nextgenerationautomation.home_page import Home
from pageobjectmodel.nextgenerationautomation.login_page import Login
from pageobjectmodel.nextgenerationautomation.signup_page import SignUp
from pageobjectmodel.nextgenerationautomation.success_page import Success
from pageobjectmodel.nextgenerationautomation.meet_our_founder_page import MeetOurFounder
from pageobjectmodel.nextgenerationautomation.overseas_hiring_model_page import OverseasHiringModel
from pageobjectmodel.nextgenerationautomation.why_choose_us_page import WhyChooseUs
from pageobjectmodel.nextgenerationautomation.placements_page import Placements
from pageobjectmodel.nextgenerationautomation.apply_indian_opening_page import ApplyIndianOpening
from pageobjectmodel.nextgenerationautomation.video_library_page import VideoLibrary
from pageobjectmodel.nextgenerationautomation.blog_page import Blog


scenarios("C:/Users/harikrishna.manokara/PycharmProjects/demo/tests/features/nextgenerationautomation")


@when("I click the login/signUp button")
def click_signup_button(driver):
    """This method is used to click sign_up button"""
    Home(driver).sign_up_button.click()


@when("I signup as a user")
def fill_new_user_details(driver, credential):
    """This method is used to register as a new user"""
    SignUp(driver).registration(credential)


@when("I click the log-in button")
def click_login_button(driver):
    """This method is used to click login button"""
    SignUp(driver).login_button.click()
    Login(driver).login_with_email.click()


@when(parsers.parse("I login as a valid {email} and {password}"))
def login_as_user(driver, email, password):
    """This method is used to login as a user"""
    Login(driver).login(email, password)


@when(parsers.parse("I click the {page} button"))
def click_heading(driver, page):
    """This method is used to click site heading"""
    if page == "Why_Choose_Us":
        Home(driver).why_choose_us_heading.click()
    elif page == "Meet_Our_Founder":
        Home(driver).click_meet_our_founder()
    elif page == "Our_Services":
        Home(driver).our_services_heading.click()
    elif page == "Overseas_Hiring_Model":
        Home(driver).click_overseas_hiring_model()
    elif page == "Placements":
        Home(driver).placements_heading.click()
    elif page == "signup":
        Home(driver).click_apply_overseas_qa_job()
    elif page == "Apply_Indian_Opening":
        Home(driver).click_apply_india_opening()
    elif page == "Video_Library":
        Home(driver).video_library_heading.click()
    elif page == "Blog":
        Home(driver).blog_heading.click()
    elif page == "Book_Bank":
        Home(driver).book_bank_heading.click()
    else:
        raise NotImplementedError


@then("I validate login button is clickable")
def validate_login_button(driver):
    """This method is used to validate login button is clickable"""
    Login(driver).login_button.click()


@then("I validate the success message")
def verify_success_message(driver, credential):
    """This method is used to validate the success message"""
    Success(driver).validate_success_message(credential)


@then(parsers.parse("I validate the page is redirect to the {page} page"))
def verify_page_title(driver, page):
    """This method is used to validate site heading page title"""
    if page == "Why_Choose_Us":
        WhyChooseUs(driver).validate_why_choose_us_title()
    elif page == "Meet_Our_Founder":
        MeetOurFounder(driver).validate_meet_our_founder_title()
    elif page == "Our_Services":
        Home(driver).validate_our_key_services_title()
    elif page == "Overseas_Hiring_Model":
        OverseasHiringModel(driver).validate_overseas_hiring_model_title()
    elif page == "Placements":
        Placements(driver).validate_placements_title()
    elif page == "signup":
        SignUp(driver).validate_sign_up_title()
    elif page == "Apply_Indian_Opening":
        ApplyIndianOpening(driver).validate_apply_india_opening_title()
    elif page == "Video_Library":
        VideoLibrary(driver).validate_video_library_title()
    elif page == "Blog":
        Blog(driver).validate_blog_title()
    else:
        raise NotImplementedError
