from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def random(request):
	template=loader.get_template("main.html")
	return render(request, 'main.html')

def convert(request):
	 # Initialize variables to hold results (empty by default)
	if request.method == 'POST':
		# Get the user input data from the form
		
		
		height = float(request.POST.get('height'))  # Convert to float
		legoHeight=round(height/0.96)
		
		apples=round(height/7.5)
		playCard=round(height/8.89)
		toiletPaper=round(height/7.9)
		googlePixel9p=round(height/15.56)
		comicBooks=round(height/49.5)
		stopSigns=round(height/76)
		doorWays=round(height/203.2)
		suv=round(height/1280.16)
		
		legor=range(legoHeight)
		appler=range(apples)
		toiletr=range(toiletPaper)
		playCardr=range(playCard)
		googler=range(googlePixel9p)
		comicr=range(comicBooks)
		stopr=range(stopSigns)
		doorr=range(doorWays)
		suvr=range(suv)
		# Pass the results to the template for display
		
		return render(request, 'convert.html', {
			'height': int(round(height)),  # Pass rounded height
			'lego': legoHeight,
			'toilet': toiletPaper,
			'playC': playCard,
			'phone': googlePixel9p,
			'book': comicBooks,
			'door': doorWays,
			'suv': suv,
			'legor': legor,
			'toiletr': toiletr,
			'playr': playCardr,
			'googler': googler,
			'comicr': comicr,
			'doorr': doorr,
			'suvr': suvr,
		})	
		
	else:
		return render(request,'main.html')
	
	
    
