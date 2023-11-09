from django.urls import re_path, path , include
from . import views

app_name = "users"


urlpatterns = [
   	# Login, Register, Forgot password, Logout
    re_path(r'^login/$', views.LoginView.as_view(), name="login_url"),
    re_path(r'^register/$', views.RegisterView.as_view(), name="register_url"),
    re_path(r'^forgot-password/$', views.ForgotPasswordView.as_view(), name="forgot_password_url"),
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout_url"),

    re_path(r'^charts/$', views.ChartsView.as_view(), name="charts_url"),

    re_path(r'^tables/$', views.TablesView.as_view(), name="tables_url"),
    re_path(r'^tables1/$', views.TablesView1.as_view(), name="tables1_url"),
    re_path(r'^tables2/$', views.TablesView2.as_view(), name="tables2_url"),
    re_path(r'^tables3/$', views.TablesView3.as_view(), name="tables3_url"),
    re_path(r'^tables4/$', views.TablesView4.as_view(), name="tables4_url"),
    re_path(r'^tables5/$', views.TablesView5.as_view(), name="tables5_url"),
    re_path(r'^tables6/$', views.TablesView6.as_view(), name="tables6_url"),
    re_path(r'^tables7/$', views.TablesView7.as_view(), name="tables7_url"),
    re_path(r'^tables8/$', views.TablesView8.as_view(), name="tables8_url"),
    
    re_path(r'^simulation_count_url/$', views.simulation_count_url.as_view(), name="simulation_count_url"),
    re_path(r'^simulation_count_results_url/$', views.simulation_count_results_url.as_view(), name="simulation_count_results_url"),

    re_path(r'^simulation_close_url/$', views.simulation_close_url.as_view(), name="simulation_close_url"),
    re_path(r'^simulation_close_results_url/$', views.simulation_close_results_url.as_view(), name="simulation_close_results_url"),

    re_path(r'^buttons/$', views.ButtonsView.as_view(), name="buttons_url"),

    re_path(r'^cards/$', views.CardsView.as_view(), name="cards_url"),

	re_path(r'^page_not_found/$', views.PageNotFoundView.as_view(), name="page_not_found_url"),    

	re_path(r'^blank/$', views.BlankView.as_view(), name="blank_page_url"),    

	# Utilities
	re_path(r'^colors/$', views.ColorsView.as_view(), name="colors_url"),    

	re_path(r'^borders/$', views.BordersView.as_view(), name="borders_url"),    

	re_path(r'^animations/$', views.AnimationsView.as_view(), name="animations_url"),    

	re_path(r'^others/$', views.OthersView.as_view(), name="others_url"),    

    re_path(r'^map/$', views.Map_View.as_view(), name="map_view_url"),
    re_path(r'^tables1/$', views.Map_View1.as_view(), name="map_view1_url"),
    re_path(r'^map/$', views.Map_View2.as_view(), name="index_url"),
    
]
