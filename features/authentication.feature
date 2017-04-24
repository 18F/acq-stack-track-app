Feature: Authentication

  Scenario: Submitting a request

    Given a logged-in user
    When I visit the root url
    Then I should have the option to submit a request

  Scenario Outline: Unauthenticated user

    Given an unauthenticated user
    When I visit <page>
    Then I <result>

    Examples:
      | page | result |
      | the root url | do not have the option to submit a request |
      | a request page | am redirected to the login page |
