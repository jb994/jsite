from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('portfolio', views.portfolio),
	path('about', views.about),
	path('contact', views.contact),
	path('portfolio/singlecell', views.singlecell),
		path('portfolio/singlecell/cellTypes', views.singlecell_cell_types),
		path('portfolio/singlecell/volcano-plot', views.volcano_plot),
		path('portfolio/singlecell/gene-net', views.gene_net),
	path('portfolio/ml-models', views.ml_models),
	path('portfolio/predictive-medicine', views.predictive_medicine),
	path('portfolio/splicing', views.splicing),
	path('portfolio/pathway-analysis', views.pathway_analysis),
]