from bs4 import BeautifulSoup

@given(u'a client')
def step_impl(context):
    pass

@when(u'I visit the intake form page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)

@then(u'I should see a form asking if the requested item costs more than $3,500 per year')
def step_impl(context):
    br = context.browser
    soup = BeautifulSoup(br.page_source, 'html.parser')
    form = soup.find('form', id='mp_threshold')
    assert form
    assert 'Does this cost more than $3500 per year?' in form.get_text()

@when(u'I select \'No\'')
def step_impl(context):
    br = context.browser
    br.find_elements_by_css("input[type='radio'][value='No']").click

@when(u'I click \'Next\'')
def step_impl(context):
    br = context.browser
    br.find_elements_by_css("input[type='submit']").click

@then(u'I should see text prompting me towards other options')
def step_impl(context):
    br = context.browser
    text = "Sorry, this form is only for purchases greater than $3500 per year. If you are in OPP, you can file your request on [Salesforce](https://gsa.my.salesforce.com/). If you are in another team in TTS, file your request on [C2](https://cap.18f.gov/)."
    assert text in br.page_source
