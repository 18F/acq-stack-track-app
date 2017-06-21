Feature: Authentication

  Scenario: Submitting a request

    Given a logged-in user
    When I visit the root url
    Then I should have the option to submit a request

  Scenario: Unauthenticated user submits request

    Given an unauthenticated user
    When I visit a request page
    Then I am redirected to the login page

  Scenario: Unauthenticated user visits site

    Given an unauthenticated user
    When I visit the root url
    Then I do not have the option to submit a request

  Scenario: Visit request from a different user

    Given a logged-in user
    Given a request from another user
    When I visit the page of a request from another user
    Then I am redirected to the index page
