# Does this cost more than $3500 per year?
# Yes
# [display next question]
# No
# Display text: “Sorry, this form is only for purchases greater than $3500 per year. If you are in OPP, you can file your request on [Salesforce](https://gsa.my.salesforce.com/). If you are in another team in TTS, file your request on [C2](https://cap.18f.gov/).”
# I’m not sure.
# [display next question]
# Is this for training?
# Yes
# Display text: “Sorry, this form is not for training purchases. If you are in OPP, you can file your request on [Salesforce](https://gsa.my.salesforce.com/). If you are in another team in TTS, file your request on [C2](https://cap.18f.gov/). You might also need additional approvals for your IDP and SF-182 -- learn more about [professional development and training in the 18F Handbook](https://handbook.18f.gov/professional-development-and-training/).”
# No
# [display next question]
# Is this purchase primarily for TTS or an external partner?
# TTS
# [display next question]
# External partner
# Display text: “Sorry, this form is for internal purchases. We recommend reaching out on Slack in #acquisition.”
# Did you get approval to buy this from the person who will be signing the check? (In other words, the person who manages the budget that will pay for this, such as your manager or the project lead.)
# Yes
# [display next question]
# No
# Display text: “To manage our workflow, we ask that you get this approval before starting a request with us. Thank you!”
# What is the best way to reach you? (For example, please share your email address or slack handle.)
# [open text field]

Feature: Starting a request

  Scenario: Client requests item that costs less than $3,500 per year

    Given a client
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'No'
    And I click 'Next'
    Then I should see text prompting me towards other options

  Scenario: Client requests item that costs more than $3,500 per year

    Given a client
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'Yes'
    And I click 'Next'
    Then I should see a form asking if the purchase is for a training

  Scenario: Client does not know if item costs more than $3,500 per year

    Given a client
    When I visit the intake form page
    Then I should see a form asking if the requested item costs more than $3,500 per year
    When I select 'I'm not sure'
    And I click 'Next'
    Then I should see a form asking if the purchase is for a training

  Scenario: Client requests a training

    Given a client
    When I visit the training form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see text informing me that this form is not for training purposes

  Scenario: Client requests something other than training

    Given a client
    When I visit the training form page
    And I select 'No'
    And I click 'Next'
    Then I should see a form asking me if the request is for TTS or external

  Scenario: Client requests external purchase

    Given a client
    When I visit the internal or external form page
    And I select 'External'
    And I click 'Next'
    Then I should see text informing me that this form is just for internal buys

  Scenario: Client requests internal purchase

    Given a client
    When I visit the internal or external form page
    And I select 'TTS'
    And I click 'Next'
    Then I should see a form asking me if I have approval

  Scenario: Client has approval

    Given a client
    When I visit the approval form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see a form asking the best way to reach me

  Scenario: Client does not have approval

    Given a client
    When I visit the approval form page
    And I select 'No'
    And I click 'Next'
    Then I should see text informing me approval is needed before starting the request

  Scenario: Client enters contact information

    Given a client
    When I visit the contact form page
    And I enter an email address
    And I click 'Next'
    Then I should see a form asking how urgent the request is

  Scenario: Client has urgent request

    Given a client
    When I visit the urgency form page
    And I select 'Yes'
    And I click 'Next'
    Then I should see a form asking me for a description of the request

  Scenario: Client does not have urgent request

    Given a client
    When I visit the urgency form page
    And I select 'No'
    And I click 'Next'
    Then I should see a form asking me for a description of the request

# Is this urgent?
# No
# Yes
# Can you provide a brief description of how urgent?
# What is it? Can you provide a brief description of what you need to purchase?
# [open text field]
