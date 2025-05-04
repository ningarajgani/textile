from django.urls import path
from . import views

urlpatterns = [
    # Home/Index URLs
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    # Pages
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('404-page/', views.page_404, name='page_404'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    
    # Team
    path('team/', views.team, name='team'),
    path('team-details/', views.team_details, name='team_details'),
    path('team-single/', views.team_single, name='team_single'),
    
    # Services
    path('fabric-dyeing/', views.fabric_dyeing, name='fabric_dyeing'),
    path('stich-fabric/', views.stich_fabric, name='stich_fabric'),
    path('synthetics-wool/', views.synthetics_wool, name='synthetics_wool'),
    path('satin-weaving/', views.satin_weaving, name='satin_weaving'),
    path('cotton-velvet/', views.cotton_velvet, name='cotton_velvet'),
    path('digital-printing/', views.digital_printing, name='digital_printing'),
    path('gis-and-planning/', views.gis_and_planning, name='gis_and_planning'),
    path('inter-design/', views.inter_design, name='inter_design'),
    
    # Portfolio
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-two-columns/', views.portfolio_two_columns, name='portfolio_two_columns'),
    path('portfolio-four-columns/', views.portfolio_four_columns, name='portfolio_four_columns'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    
    # Blog
   path('blog/', views.blog, name='blog'),
    path('blog/list/', views.blog_list, name='blog_list'),
    path('blog/details/', views.blog_details, name='blog_details'),
    path('blog/grid/two-columns/', views.blog_grid_two_columns, name='blog_grid_two_columns'),
    path('blog/grid/two-columns/left-sidebar/', views.blog_grid_two_columns_left_sidebar, 
         name='blog_grid_two_columns_left_sidebar'),  # Fixed name to match template
    path('blog/grid/two-columns/right-sidebar/', views.blog_grid_two_columns_right_sidebar, 
         name='blog_grid_two_columns_right_sidebar'),  # Fixed name to match template
    path('blog/grid/', views.blog_grid, name='blog_grid'),
    
    # Contact
    path('contact/', views.contact, name='contact'),
]