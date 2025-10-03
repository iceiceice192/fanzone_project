
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PreferencesForm

# Data embedded in code (teams list)
AVAILABLE_TEAMS = [
    ('team_red', 'Red Rockets'),
    ('team_blue', 'Blue Sharks'),
    ('team_green', 'Green Giants'),
]

def index(request):
    # redirect to settings page as main entry
    return redirect('settings')

def user_settings(request):
    # read current cookies
    theme = request.COOKIES.get('theme', 'light')
    lang = request.COOKIES.get('lang', 'en')
    favorites_cookie = request.COOKIES.get('favorites', '')
    favorites = favorites_cookie.split(',') if favorites_cookie else []

    if request.method == 'POST':
        form = PreferencesForm(request.POST, teams_choices=AVAILABLE_TEAMS)
        if form.is_valid():
            favorites_selected = form.cleaned_data['favorites']
            theme_selected = form.cleaned_data['theme']
            lang_selected = form.cleaned_data['lang']

            response = redirect('favorites')

            # set cookies for 30 days
            cookie_value = ','.join(favorites_selected)
            response.set_cookie('favorites', cookie_value, max_age=30*24*3600)
            response.set_cookie('theme', theme_selected, max_age=30*24*3600)
            response.set_cookie('lang', lang_selected, max_age=30*24*3600)

            # track last visited pages - append this page
            last_pages = request.COOKIES.get('last_pages', '')
            pages = last_pages.split('|') if last_pages else []
            pages.append('settings')
            # keep only last 5
            pages = pages[-5:]
            response.set_cookie('last_pages', '|'.join(pages), max_age=30*24*3600)

            return response
    else:
        form = PreferencesForm(initial={'favorites': favorites, 'theme': theme, 'lang': lang}, teams_choices=AVAILABLE_TEAMS)
    context = {'form': form, 'teams': AVAILABLE_TEAMS, 'theme': theme, 'lang': lang}
    return render(request, 'teams/settings.html', context)

def favorites(request):
    theme = request.COOKIES.get('theme', 'light')
    lang = request.COOKIES.get('lang', 'en')
    favorites_cookie = request.COOKIES.get('favorites', '')
    favorites = favorites_cookie.split(',') if favorites_cookie else []
    # find friendly names
    friendly = [label for key,label in AVAILABLE_TEAMS if key in favorites]
    # update last pages cookie
    response = render(request, 'teams/favorites.html', {'favorites': friendly, 'theme': theme, 'lang': lang})
    last_pages = request.COOKIES.get('last_pages', '')
    pages = last_pages.split('|') if last_pages else []
    pages.append('favorites')
    pages = pages[-5:]
    response.set_cookie('last_pages', '|'.join(pages), max_age=30*24*3600)
    return response

def clear_cookies(request):
    response = redirect('settings')
    response.delete_cookie('favorites')
    response.delete_cookie('theme')
    response.delete_cookie('lang')
    response.delete_cookie('last_pages')
    return response
