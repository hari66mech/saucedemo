Feature: Enter the user data

    Background:
        Given The demoqa text page is displayed


    Scenario: Validate all the fields are accept valid data
        When I am entering user_name
        And I am entering email_id
        And I am entering current_address
        And I am entering permanent_address
        And I am clicking submit button
        Then I validate the output box
