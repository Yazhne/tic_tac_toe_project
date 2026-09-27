from django.shortcuts import render

def home(request):
    return render(request, 'game/home.html')

def game(request):
    return render(request, 'game/game.html')

def ai_game(request):
    return render(request, 'game/ai_game.html')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mode = request.POST.get('mode')  # 'human' or 'ai'

        # Pass username to game page
        if mode == 'human':
            return render(request, 'game/game.html', {'username': username})
        else:
            return render(request, 'game/ai_game.html', {'username': username})

    return render(request, 'game/login.html')
