from weboob.capabilities.base import (
    BaseObject, Field, StringField, IntField
)

class PokeOptions(BaseObject):
    abilityOptions = Field('These are the Pokemon ability options', dict)
    generationsOptions = Field('These are the Pokemon generations options', dict)
    tierOptions = Field('These are the Pokemon tier options', dict)