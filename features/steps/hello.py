@when(u'I visit the root url')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)

@then(u'I should see the message to randy')
def step_impl(context):
    br = context.browser
    assert 'randy..............thank you' in br.page_source
