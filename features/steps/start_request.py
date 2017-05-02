from intake.models import *
from intake.services import *
from bs4 import BeautifulSoup
import time

def get_request(context):
    request = context.request
    print(request.pk)
    return request

@given(u'a client')
def step_impl(context):
    pass

@given(u'a client and a request')
def step_impl(context):
    context.request = CreateRequest().perform()

@given(u'a request')
def step_impl(context):
    class MockRequest(object):
        pk = 12
    mock_request = MockRequest()
    context.request = mock_request

@when(u'I visit the start request page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/requests/new')

@when(u'I click \'Create Request\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("create_request").click()

@when(u'I visit the intake form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/start')

@then(u'I should see a form asking if the requested item costs more than $3,500 per year')
def step_impl(context):
    br = context.browser
    context.asserter.assertIn('Does this cost more than $3500 per year?', br.page_source)

@then(u'I should see a form asking if the purchase is for a training')
def step_impl(context):
    br = context.browser
    soup = BeautifulSoup(br.page_source, 'html.parser')
    form = soup.find('form', id='training_form')
    assert form
    assert 'Is this for training?' in form.get_text()

@when(u'I select \'No\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("radio_no").click()

@when(u'I select \'Yes\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("radio_yes").click()

@when(u'I select \'I\'m not sure\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("radio_not_sure").click()

@when(u'I click \'Next\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("submit").click()

@then(u'I should see text prompting me towards other options')
def step_impl(context):
    br = context.browser
    text = "Sorry, this form is only for purchases greater than $3500 per year."
    sorry = br.find_element_by_id('sorry')
    assert text in sorry.text

@when(u'I visit the training form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/training')

@then(u'I should see text informing me that this form is not for training purposes')
def step_impl(context):
    br = context.browser
    text = "Sorry, this form is not for training purchases."
    assert text in br.page_source

@then(u'I should see a form asking me if the request is for TTS or external')
def step_impl(context):
    br = context.browser
    text = "Is this purchase primarily for TTS or an external partner?"
    assert text in br.page_source

@when(u'I visit the internal or external form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/internal_or_external')

@when(u'I select \'External\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('radio_external').click()

@then(u'I should see text informing me that this form is just for internal buys')
def step_impl(context):
    br = context.browser
    text = "Sorry, this form is for internal purchases."
    context.asserter.assertIn(text, br.page_source)

@when(u'I select \'TTS\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('radio_tts').click()

@then(u'I should see a form asking me if I have approval')
def step_impl(context):
    br = context.browser
    text = "Did you get approval to buy this from the person who will be signing the check?"
    context.asserter.assertIn(text, br.page_source)

@when(u'I visit the approval form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/approval')

@then(u'I should see a form asking the best way to reach me')
def step_impl(context):
    br = context.browser
    text = "What is the best way to reach you?"
    context.asserter.assertIn(text, br.page_source)

@then(u'I should see text informing me approval is needed before starting the request')
def step_impl(context):
    br = context.browser
    text = "we ask that you get this approval before starting a request with us"
    context.asserter.assertIn(text, br.page_source)

@when(u'I visit the contact form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    url = context.base_url + '/requests/' + str(request.pk) + '/contact'
    """
    Dear Alan of tomorrow, here is what Alan of yesterday figured out:
    you're getting these errors because in /requests/{{ request_id }}/contact',
    request_id is null, so of course the URL isn't found.
    """
    br.get(url)

@when(u'I enter an email address')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('contact').send_keys("someemail@somewhere.com")

@then(u'I should see a form asking if the request is urgent')
def step_impl(context):
    br = context.browser
    text = "Is this urgent?"
    context.asserter.assertIn(text, br.page_source)

@when(u'I visit the urgency form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/urgency')

@then(u'I should see a form asking how urgent the request is')
def step_impl(context):
    br = context.browser
    text = "How urgent is the request?"
    context.asserter.assertIn(text, br.page_source)

@when(u'I visit the urgency description form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/urgency_description')

@then(u'I should see a form asking me for a description of the request')
def step_impl(context):
    br = context.browser
    text = "Can you provide a brief description of what you need to purchase?"
    context.asserter.assertIn(text, br.page_source)

@when(u'I fill in the urgency description textbox')
def step_impl(context):
    br = context.browser
    description = """
    This is very urgent! Drop everything!
    """
    br.find_element_by_id('urgency_description').send_keys(description)

@when(u'I fill in the description text box')
def step_impl(context):
    br = context.browser
    description = """
    This is the description of the thing I want. It's got the cloud in it.
    And it's written in Go, but also lots of React.
    """
    br.find_element_by_id('description').send_keys(description)

@when(u'I visit the description form page')
def step_impl(context):
    br = context.browser
    request = get_request(context)
    br.get(context.base_url + '/requests/' + str(request.pk) + '/description')

@then(u'I see a form prompting me to submit my request')
def step_impl(context):
    br = context.browser
    text = "Please review the information below and click submit if it's correct:"
    context.asserter.assertIn(text, br.page_source)
