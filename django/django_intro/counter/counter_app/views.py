from django.shortcuts import render, redirect

# Root route
def index(request):

    # If visits does not exist yet, create it and start at 0
    if "visits" not in request.session:
        request.session["visits"] = 0

    # If counter does not exist yet, create it and start at 0
    if "counter" not in request.session:
        request.session["counter"] = 0

    # Every time root route is visited, visits increases by 1
    request.session["visits"] += 1

    # Main counter also increases by 1 on page visit
    request.session["counter"] += 1

    return render(request, "index.html")


# Clears the session and redirects back to root
def destroy_session(request):
    request.session.clear()
    return redirect("/")


# Adds 2 to the counter
def add_two(request):

    if "counter" not in request.session:
        request.session["counter"] = 0

    request.session["counter"] += 2

    return redirect("/")


# Adds custom number from form
def custom_increment(request):

    if "counter" not in request.session:
        request.session["counter"] = 0

    amount = int(request.POST["amount"])

    request.session["counter"] += amount

    return redirect("/")