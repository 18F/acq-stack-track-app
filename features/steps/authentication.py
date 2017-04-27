from bs4 import BeautifulSoup
# from seleniumlogin import force_login
import selenium

@given('a logged-in user')
def step_impl(context):
    from django.contrib.auth.models import User
    user = User.objects.create(username='testuser', password='testpassword', email='fake@test.gov')
    user.save()

    # Log in by creating a cookie in the Django test client and then passing it
    # over to the Selenium setup
    driver = context.browser
    base_url = context.base_url

    from importlib import import_module
    from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY
    from django.conf import settings
    SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
    driver.get(context.base_url + '/')

    session = SessionStore()
    session[SESSION_KEY] = user.id
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()

    domain = base_url.split(':')[-2].split('/')[-1]
    cookie = {
        'name': settings.SESSION_COOKIE_NAME,
        'value': session.session_key,
        'path': '/',
        'domain': '.localhost',
        'max-age': None,
        'expires': None,
        'secure': False,
    }

    driver.add_cookie(cookie)
    driver.refresh()

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
