from bs4 import BeautifulSoup

@given('a logged-in user')
def step_impl(context):
    from django.contrib.auth.models import User
    user = User(username='test', email='test@fake.gov')
    user.save()
    context.test.client.force_login(user)

# @when('I visit the root url')
# def step_impl(context):
#     br = context.browser
#     br.open(context.browser_url('/'))

@then('I should have the option to submit a request')
def step_impl(context):
    br = context.browser
    start = br.find_element_by_id('start-request')
    text = 'Start a request'
    assert text in start.text

@given('an unauthenticated user')
def step_impl(context):
    pass

@when('I visit a request page')
def step_impl(context):
    pass

@then('I do not have the option to submit a request')
def step_impl(context):
    pass

@then('I am redirected to the login page')
def step_impl(context):
    pass
