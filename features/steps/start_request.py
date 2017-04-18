from bs4 import BeautifulSoup
import time

@given(u'a client')
def step_impl(context):
    pass

@when(u'I visit the intake form page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/start')

@then(u'I should see a form asking if the requested item costs more than $3,500 per year')
def step_impl(context):
    br = context.browser
    soup = BeautifulSoup(br.page_source, 'html.parser')
    form = soup.find('form', id='mp_threshold')
    assert form
    assert 'Does this cost more than $3500 per year?' in form.get_text()

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
    br.get(context.base_url + '/training')

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
    br.get(context.base_url + '/internal_or_external')

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
    br.get(context.base_url + '/approval')

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
