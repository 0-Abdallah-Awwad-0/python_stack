from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

# This function displays the main Ninja Gold page
def index(request):

    # If gold does not exist in session, create it and start at 0
    if "gold" not in request.session:
        request.session["gold"] = 0

    # If activities does not exist in session, create empty list
    if "activities" not in request.session:
        request.session["activities"] = []

    return render(request, "index.html")


# This function handles all form submissions
def process_money(request):

    # Get the location from the hidden input
    location = request.POST["location"]

    gold_earned = 0

    # Decide gold amount depending on location
    if location == "farm":
        gold_earned = randint(10, 20)

    elif location == "cave":
        gold_earned = randint(5, 10)

    elif location == "house":
        gold_earned = randint(2, 5)

    elif location == "quest":
        gold_earned = randint(-50, 50)

    # Update total gold in session
    request.session["gold"] += gold_earned

    # Create timestamp
    time = datetime.now().strftime("%B %d %Y %I:%M %p")

    # Create activity message
    if gold_earned >= 0:
        message = f"You entered a {location} and earned {gold_earned} gold. ({time})"
        color = "green"
    else:
        message = f"You failed a {location} and lost {abs(gold_earned)} gold. Ouch. ({time})"
        color = "red"

    # Add activity to the beginning of the list
    activities = request.session["activities"]
    activities.insert(0, {"message": message, "color": color})
    request.session["activities"] = activities

    return redirect("/")


# This function resets the game
def reset(request):
    request.session.clear()
    return redirect("/")