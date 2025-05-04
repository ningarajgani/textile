
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Home/Index Views
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect
        else:
            # Return error message
            pass
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired redirect
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Page Views
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def faq(request):
    return render(request, 'faq.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def page_404(request):
    return render(request, '404-page.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

# Team Views
def team(request):
    return render(request, 'team.html')

def team_details(request):
    return render(request, 'team-details.html')

def team_single(request):
    return render(request, 'team-single.html')

# Service Views
def fabric_dyeing(request):
    return render(request, 'fabric-dyeing.html')

def stich_fabric(request):
    return render(request, 'stich-fabric.html')

def synthetics_wool(request):
    return render(request, 'synthetics-wool.html')

def satin_weaving(request):
    return render(request, 'satin-weaving.html')

def cotton_velvet(request):
    return render(request, 'cotton-velvet.html')

def digital_printing(request):
    return render(request, 'digital-printing.html')

def gis_and_planning(request):
    return render(request, 'gis-and-planning.html')

def inter_design(request):
    return render(request, 'inter-design.html')

# Portfolio Views
def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_two_columns(request):
    return render(request, 'portfolio-two-columns.html')

def portfolio_four_columns(request):
    return render(request, 'portfolio-four-columns.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

# Blog Views
def blog(request):
    return render(request, 'blog.html')

def blog_list(request):
    return render(request, 'blog-list.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog_grid(request):
    return render(request, 'blog-grid.html')

def blog_grid_two_columns(request):
    return render(request, 'blog-grid-two-columns.html')

def blog_grid_two_columns_left_sidebar(request):
    return render(request, 'blog-grid-two-columns-left-sidebar.html')

def blog_grid_two_columns_right_sidebar(request):
    return render(request, 'blog-grid-two-columns-right-sidebar.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')