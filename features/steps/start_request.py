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
    form = soup.find('form', id='training')
    assert form
    assert 'Is this for training?' in form.get_text()

@when(u'I select \'No\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("mp_radio_no").click()

@when(u'I select \'Yes\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("mp_radio_yes").click()

@when(u'I click \'Next\'')
def step_impl(context):
    br = context.browser
    br.find_element_by_id("mp_submit").click()

@then(u'I should see text prompting me towards other options')
def step_impl(context):
    br = context.browser
    text = "Sorry, this form is only for purchases greater than $3500 per year."
    sorry = br.find_element_by_id('sorry')
    assert text in sorry.text
