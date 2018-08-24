from weboob.capabilities.base import (
    BaseObject, Field, StringField, IntField, DecimalField
)

class Description(BaseObject):
    pv = StringField('Pv of the Pokemon')
    attack = StringField('Attack of the Pokemon')
    defense = StringField('Defense of the Pokemon')
    speAttack = StringField('Special attack of the Pokemon')
    speDefense = StringField('Special defense of the Pokemon')
    speed = StringField('Speed of the Pokemon')