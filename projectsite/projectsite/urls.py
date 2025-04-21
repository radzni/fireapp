from django.contrib import admin
from django.urls import path

from fire.views import HomePageView
from fire import views
from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('line_chart/', LineCountbyMonth, name='chart'),
    path('multiline_chart/', MultilineIncidentTop3Country, name='chart'),
    path('multiple_bar_chart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('Incidents', views.map_incidents, name='map-incident'),

]
