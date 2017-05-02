
Feature: Starting a request

  Scenario: Client starts a request

    Given a logged-in user
    When I visit the start request page
    And I click 'Create Request'
    Then I should see a form asking if the requested item costs more than $3,500 per year

  Scenario: Client requests item that costs less than $3,500 per year

    Given a logged-in user
    Given a request
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'No'
    And I click 'Next'
    Then I should see text prompting me towards other options

  Scenario: Client requests item that costs more than $3,500 per year

    Given a logged-in user
    Given a request
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'Yes'
    And I click 'Next'
    Then I should see a form asking if the purchase is for a training

  Scenario: Client does not know if item costs more than $3,500 per year

    Given a logged-in user
    Given a request
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'I'm not sure'
    And I click 'Next'
    Then I should see a form asking if the purchase is for a training

  Scenario: Client requests a training

    Given a logged-in user
    Given a request
    When I visit the training form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see text informing me that this form is not for training purposes

  Scenario: Client requests something other than training

    Given a logged-in user
    Given a request
    When I visit the training form page
    And I select 'No'
    And I click 'Next'
    Then I should see a form asking me if the request is for TTS or external

  Scenario: Client requests external purchase

    Given a logged-in user
    Given a request
    When I visit the internal or external form page
    And I select 'External'
    And I click 'Next'
    Then I should see text informing me that this form is just for internal buys

  Scenario: Client requests internal purchase

    Given a logged-in user
    Given a request
    When I visit the internal or external form page
    And I select 'TTS'
    And I click 'Next'
    Then I should see a form asking me if I have approval

  Scenario: Client has approval

    Given a logged-in user
    Given a request
    When I visit the approval form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see a form asking the best way to reach me

  Scenario: Client does not have approval

    Given a logged-in user
    Given a request
    When I visit the approval form page
    And I select 'No'
    And I click 'Next'
    Then I should see text informing me approval is needed before starting the request

  Scenario: Client enters contact information

    Given a logged-in user
    Given a request
    When I visit the contact form page
    And I enter an email address
    And I click 'Next'
    Then I should see a form asking if the request is urgent

  Scenario: Client has urgent request

    Given a logged-in user
    Given a request
    When I visit the urgency form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see a form asking how urgent the request is

  Scenario: Client describes the urgency of their request

    Given a logged-in user
    Given a request
    When I visit the urgency description form page
    And I fill in the urgency description textbox
    And I click 'Next'
    Then I should see a form asking me for a description of the request

  Scenario: Client does not have urgent request

    Given a logged-in user
    Given a request
    When I visit the urgency form page
    And I select 'No'
    And I click 'Next'
    Then I should see a form asking me for a description of the request

  Scenario: Client describes the request

    Given a logged-in user
    Given a request
    When I visit the description form page
    And I fill in the description text box
    And I click 'Next'
    Then I see a form prompting me to submit my request
