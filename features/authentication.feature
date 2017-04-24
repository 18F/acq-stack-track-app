Feature: Authentication

  Scenario: Submitting a request

    Given a logged-in user
    When I visit the root url
    Then I should have the option to submit a request

  Scenario Outline: Unauthenticated user submits request

    Given an unauthenticated user
    When I visit a request page
    Then I am redirected to the login page

  Scenario Outline: Unauthenticated user visits site

    Given an unauthenticated user
    When I visit the root url
    Then I do not have the option to submit a request
