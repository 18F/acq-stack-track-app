Feature: Authentication

  Scenario: Submitting a request

    Given a logged-in user
    When I visit the main page
    Then I should have the option to submit a request

  Scenario: Unauthenticated user

    Given an unauthenticated user
    When I visit a request page
    Then I am redirected to the login page
