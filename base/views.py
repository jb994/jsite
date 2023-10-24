from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def portfolio(request):
	return render(request, 'base/portfolio.html')

def about(request):
	return render(request, 'base/about.html')

def contact(request):
	return render(request, 'base/contact.html')

def singlecell(request):
	return render(request, 'portfolio/singlecell.html')

def singlecell_cell_types(request):
	return render(request, 'html_images/Percentage_Cell_Types_unnamed.html')
def volcano_plot(request):
	return render(request, 'html_images/Normal_Vehicle_scVolcano.html')
def gene_net(request):
	return render(request, 'html_images/NormalxVehicle_2.0lfc_NET.html')

def ml_models(request):
	return render(request, 'portfolio/ml-models.html')

def predictive_medicine(request):
	return render(request, 'portfolio/predictive-medicine.html')

def splicing(request):
	return render(request, 'portfolio/splicing-analysis.html')

def pathway_analysis(request):
	return render(request, 'portfolio/pathway-analysis.html')
