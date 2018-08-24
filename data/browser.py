from weboob.browser import PagesBrowser, URL
from myapp.data.pages.pokemon import PokemonPage
from myapp.data.pages.description import DescriptionPage
from weboob.tools.compat import urlencode

class MyBrowser(PagesBrowser):
    BASEURL = 'https://www.pokebip.com'
    
    """
    Pages definition
    """
    pokemon = URL(r'/pokedex/pokemon$', PokemonPage)
    description = URL(r'/pokedex/pokemon/(?P<name>.*)', DescriptionPage)
    pokeSearch = URL(r'/pokedex/pokemon\?(?P<request>.*)', PokemonPage)

    def get_pokemons(self):
        self.pokemon.go()
        return self.page.get_pokemons()

    def get_descriptions(self, name):
        self.description.go(name=name)
        return self.page.get_strategic_view()

    def getOptions(self):
        data = {'talent': '',
                'generations': '',
                'tier': ''}
        self.pokeSearch.go(request=urlencode(data))
        return self.page.get_options()

    def do_pokeSearch(self, request):
        data = {'talent': request.ability,
                'generations': request.generations,
                'tier': request.tier}
        self.pokeSearch.go(request = urlencode(data))
        return self.page.get_pokemons()

Browser = MyBrowser()