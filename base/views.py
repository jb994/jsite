from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def portfolio(request):
	return render(request, 'base/portfolio.html')

def about(request):
	return render(request, 'base/about.html')

# ---------------------------------------------------------------------------
# Publications  (Vancouver / AMA style)
#
# To add a new publication, copy one { ... } block below and fill it in.
# Keep the newest at the top (they're shown as a numbered list in this order).
#   authors : author list as "Surname Initials", separated by commas, ending
#             with a period. Wrap your own name in <strong></strong> so it
#             shows in bold, e.g. <strong>Brons J</strong>.
#   title   : article title (end it with a period).
#   journal : journal name, ideally the standard abbreviation (e.g. 'Gut',
#             'Exp Hematol Oncol'). The full name works too.
#   year    : year of publication (string).
#   volinfo : the volume / page part, if any. Leave as '' when there's none.
#             Examples: '15'  or  '33:201031'. It renders as ';<volinfo>'.
#   doi     : the DOI, e.g. '10.1136/gutjnl-2025-337970'
#             (it's automatically turned into a https://doi.org/... link).
# Rendered as:  Authors Title Journal. Year;volinfo. doi:...
# ---------------------------------------------------------------------------
PUBLICATIONS = [
	{
		'authors': 'Van den Bossche J-L, Vliet M, Michiels E, Azurmendi O, '
			'Van Lint S, Madran Z, Coolens K, <strong>Brons J</strong>, Nacher M, '
			'Arsenijevic T, Messaoudi N, Lefesvre P, Bouchart C, Verset L, Navez J, '
			'Fallas J, Dusetti N, Montanya E, Rovira M, Rooman I.',
		'title': 'Luminal–basal stratification of the native human pancreatic '
			'duct is differentially represented in pancreatic cancers.',
		'journal': 'Gut',
		'year': '2026',
		'volinfo': '',
		'doi': '10.1136/gutjnl-2025-337970',
	},
	{
		'authors': 'Tu C, Van der Vreken A, Meeus F, Broecke L, '
			'<strong>Brons J</strong>, De Veirman K, Vanderkerken K, De Bruyne E, '
			'Breckpot K, Menu E.',
		'title': 'Hypoxia promotes BCMA loss and a suppressive secretome thereby '
			'hindering CAR T cell therapy in multiple myeloma.',
		'journal': 'Exp Hematol Oncol',
		'year': '2026',
		'volinfo': '15',
		'doi': '10.1186/s40164-025-00732-6',
	},
	{
		'authors': 'Tuyaerts S, Geeraerts X, Reale A, Stevens L, Bertazzon G, '
			'<strong>Brons J</strong>, Janssen T, Van Riet I, Calistri A, Neyns B.',
		'title': 'An oncolytic herpes simplex virus type 1 expressing FMS-like '
			'tyrosine kinase 3 ligand (FLT3L) inhibits the growth of melanoma, '
			'glioblastoma and pancreatic adenocarcinoma cells in vitro, and induces '
			'immunogenic cell death triggering partial maturation of conventional '
			'dendritic cells.',
		'journal': 'Mol Ther Oncol',
		'year': '2025',
		'volinfo': '33:201031',
		'doi': '10.1016/j.omton.2025.201031',
	},
]

def publications(request):
	return render(request, 'base/publications.html', {'publications': PUBLICATIONS})

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

def cow_ml(request):
	return render(request, 'portfolio/cow-ml.html')

def spatial_transcriptomics(request):
	return render(request, 'portfolio/spatial-transcriptomics.html')