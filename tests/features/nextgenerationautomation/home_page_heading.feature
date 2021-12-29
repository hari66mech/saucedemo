Feature: Next generation automation features

    Background:
        Given The nextgenerationautomation home_page is displayed

    Scenario: Verify the page is redirect to the Why_Choose_Us page when click Why_Choose_Us
        When I click the Why_Choose_Us button
        Then I validate the page is redirect to the Why_Choose_Us page

    Scenario: Verify the page is redirect to the Meet_Our_Founder page when click Meet_Our_Founder
        When I click the Meet_Our_Founder button
        Then I validate the page is redirect to the Meet_Our_Founder page

    Scenario: Verify the page is redirect to the Our_Services page when click Our_Services
        When I click the Our_Services button
        Then I validate the page is redirect to the Our_Services page

    Scenario: Verify the page is redirect to the Overseas_Hiring_Model page when click Overseas_Hiring_Model
        When I click the Overseas_Hiring_Model button
        Then I validate the page is redirect to the Overseas_Hiring_Model page

    Scenario: Verify the page is redirect to the Placements page when click Placements
        When I click the Placements button
        Then I validate the page is redirect to the Placements page

    Scenario: Verify the page is redirect to the Apply_Overseas_QA_Job page when click Apply_Overseas_QA_Job
        When I click the Apply_Overseas_QA_Job button
        Then I validate the page is redirect to the signup page

    Scenario: Verify the page is redirect to the Apply_Indian_Opening page when click Apply_Indian_Opening
        When I click the Apply_Indian_Opening button
        Then I validate the page is redirect to the Apply_Indian_Opening page

    Scenario: Verify the page is redirect to the Video_Library page when click Video_Library
        When I click the Video_Library button
        Then I validate the page is redirect to the Video_Library page

    Scenario: Verify the page is redirect to the Blog page when click Blog
        When I click the Blog button
        Then I validate the page is redirect to the Blog page

    Scenario: Verify the page is redirect to the Book_Bank page when click Book_Bank
        When I click the Book_Bank button
        Then I validate the page is redirect to the signup page
