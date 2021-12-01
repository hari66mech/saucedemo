Feature: Fill the text box field
    As I was filled the text box and clicked submit button, the output box is displayed.

    Background:
        Given The demoqa text page is displayed


    Scenario: Validate all the fields are accepting the valid data and validate the output box field is displayed after clicking submit button.
        When I fill the user_name
        And I fill the email_id
        And I fill the current_address
        And I fill the permanent_address
        And I am clicking submit button
        Then I validate the output box field is displayed
