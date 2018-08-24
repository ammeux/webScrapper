
import re

from myapp.app.models.description import Description

from weboob.browser.pages import HTMLPage
from weboob.capabilities.base import BaseObject, Field, StringField, IntField
from weboob.browser.elements import TableElement, ItemElement, method
from weboob.browser.filters.standard import CleanText, CleanDecimal, TableCell
from weboob.browser.filters.html import Attr

#### I left in comment below another method to scrap the table values ###############
#                                                                                   #
#def get_table_value(el, sibling):                                                  #
#    item_xpath = u'//div[contains(., "Aper")]/following-sibling::table'            #
#                                                                                   #
#    tr = el.xpath(item_xpath)[0].xpath('//tr[contains(., "{}")]'.format(sibling))  #
#                                                                                   #
#    return tr[0].xpath('td[2]')                                                    #
#                                                                                   #
#AND BELOW THE CORRESPONDING PAGE                                                   #
#                                                                                   #
#class DescriptionPage(HTMLPage):                                                   #
#    @method                                                                        #
#    class get_strategic_view(ItemElement):                                         #
#        klass = Description                                                        #
#                                                                                   #
#       #def obj_pv(self):                                                          #
#       #    return CleanText().filter(get_table_value(self, 'PV'))                 #
#       #def obj_attack(self):                                                      #
#       #    return CleanText().filter(get_table_value(self, 'Attaque'))            #
#       #def obj_defense(self):                                                     #            
#       #    return CleanText().filter(get_table_value(self, 'D' + u'\u00e9' +'fense'))
#       #def obj_speAttack(self):
#       #    return CleanText().filter(get_table_value(self, 'Attaque sp' + u'\u00e9'))
#       #def obj_speDefense(self):
#       #    return CleanText().filter(get_table_value(self, 'D' + u'\u00e9' + 'fense sp' + u'\u00e9'))
#       #def obj_speed(self):                                                       #
#       #    return CleanText().filter(get_table_value(self, 'Vitesse'))            #
#                                                                                   #    
#####################################################################################

class DescriptionPage(HTMLPage):
    @method
    class get_strategic_view(ItemElement):
        klass = Description

        obj_pv = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[2]/td[2]/div/div/strong')
        obj_attack = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[3]/td[2]/div/div/strong')
        obj_defense = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[4]/td[2]/div/div/strong')
        obj_speAttack = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[5]/td[2]/div/div/strong')
        obj_speDefense = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[6]/td[2]/div/div/strong')
        obj_speed = CleanText('//*[@id="content"]/div[4]/div[2]/div/table//tr[7]/td[2]/div/div/strong')
        