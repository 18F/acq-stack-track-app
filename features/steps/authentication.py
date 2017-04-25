from bs4 import BeautifulSoup
import selenium

@given('a logged-in user')
def step_impl(context):
    from django.contrib.auth.models import User
    user = User(username='test', email='test@fake.gov')
    user.save()
    context.test.client.force_login(user)

@then('I should have the option to submit a request')
def step_impl(context):
    br = context.browser
    start = br.find_element_by_id('start-request')
    text = 'Make a request'
    assert text in start.text

@given('an unauthenticated user')
def step_impl(context):
    # TODO: should this affirmatively set AnonymousUser?
    pass

@when('I visit a request page')
def step_impl(context):
    context.response = context.test.client.get(context.base_url + '/start')

@then('I do not have the option to submit a request')
def step_impl(context):
    br = context.browser
    try:
        start = br.find_element_by_id('start-request')
    except selenium.common.exceptions.NoSuchElementException:
        assert True

@then('I am redirected to the login page')
def step_impl(context):
    assert context.response.status_code == 301
    expected_url = context.base_url + "/auth/login"
    assert context.browser.current_url == expected_url
