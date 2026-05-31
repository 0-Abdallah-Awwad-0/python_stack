import random
from django.shortcuts import render, redirect


def index(request):
    # If there is no random number in session, create one
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = ''
        request.session['game_over'] = False
        request.session['won'] = False
        request.session['winner_saved'] = False

    context = {
        'status': request.session.get('status'),
        'attempts': request.session.get('attempts'),
        'game_over': request.session.get('game_over'),
        'won': request.session.get('won'),
        'winner_saved': request.session.get('winner_saved'),
    }

    return render(request, 'game/index.html', context)


def guess(request):
    if request.method == 'POST':
        # If the game already ended, do not allow more guesses
        if request.session.get('game_over') == True:
            return redirect('/')

        # Get the guess from the form
        user_guess = request.POST.get('guess')

        # Make sure the user entered something
        if user_guess == '':
            request.session['status'] = 'Please enter a number.'
            return redirect('/')

        # Convert the guess from string to integer
        user_guess = int(user_guess)

        # Get the random number from session
        number = request.session['number']

        # Increase attempts by 1
        request.session['attempts'] += 1

        # Check if guess is too low
        if user_guess < number:
            if request.session['attempts'] >= 5:
                request.session['status'] = f'You Lose! The correct number was {number}.'
                request.session['game_over'] = True
                request.session['won'] = False
            else:
                request.session['status'] = 'Too low!'

        # Check if guess is too high
        elif user_guess > number:
            if request.session['attempts'] >= 5:
                request.session['status'] = f'You Lose! The correct number was {number}.'
                request.session['game_over'] = True
                request.session['won'] = False
            else:
                request.session['status'] = 'Too high!'

        # Correct guess
        else:
            request.session['status'] = f'{number} was the number!'
            request.session['game_over'] = True
            request.session['won'] = True

    return redirect('/')


def reset(request):
    # Keep leaderboard if it exists
    leaderboard = request.session.get('leaderboard', [])

    # Clear session
    request.session.flush()

    # Put leaderboard back
    request.session['leaderboard'] = leaderboard

    return redirect('/')


def save_winner(request):
    if request.method == 'POST':
        # Only save if user actually won
        if request.session.get('won') == True and request.session.get('winner_saved') == False:
            name = request.POST.get('name')

            if name == '':
                name = 'Anonymous'

            winner = {
                'name': name,
                'attempts': request.session.get('attempts')
            }

            leaderboard = request.session.get('leaderboard', [])
            leaderboard.append(winner)

            # Sort winners by lowest attempts
            leaderboard.sort(key=lambda player: player['attempts'])

            request.session['leaderboard'] = leaderboard
            request.session['winner_saved'] = True

    return redirect('/leaderboard')


def leaderboard(request):
    context = {
        'leaderboard': request.session.get('leaderboard', [])
    }

    return render(request, 'game/leaderboard.html', context)