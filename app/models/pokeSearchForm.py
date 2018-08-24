from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, RadioField
from myapp.data.browser import Browser
class PokeSearchForm(Form):
    abilityOptions = list(Browser.getOptions().abilityOptions.items())
    abilityOptions[0] = ('','')
    tierOptions = list(Browser.getOptions().tierOptions.items())
    tierOptions[0] = ('', '')
    ability = SelectField('Ability',
                          choices=abilityOptions)
    tier = SelectField('Tier',
                       choices=tierOptions)
    generations = RadioField('Generations',
                              choices = [('',''),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7')], default='')