from flask import Flask, request, flash, redirect, render_template, url_for
from wtforms import (
    Form, BooleanField, StringField, PasswordField, validators,
)
from myapp.data.browser import Browser
from myapp.app.models.pokeSearchForm import PokeSearchForm
from myapp.app.models.pokeSearch import PokeSearch
import os

app = Flask(__name__, template_folder='views')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/allPokemons')
def allPokemons():
    Pokemons = dict()
    Pokemons = Browser.get_pokemons()
    return render_template('allPokemons.html', values = Pokemons)

@app.route('/pokeSearch', methods=['GET', 'POST'])
def pokeSearch():
    form = PokeSearchForm(request.form)
    if request.method == 'POST' and form.validate():
        myPokeSearch = PokeSearch(form.ability.data, form.generations.data, form.tier.data)
        Pokemons = Browser.do_pokeSearch(myPokeSearch)
        return render_template('allPokemons.html', values = Pokemons)
    return render_template('pokeSearch.html', form = form)

@app.route('/<name>')
def show_pokemon(name):
    Descriptions = Browser.get_descriptions(name.lower())
    return render_template('descPokemon.html', description = Descriptions)
