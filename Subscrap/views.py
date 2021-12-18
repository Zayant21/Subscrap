import json
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login as Login, authenticate, logout
from Subscrap.forms import StudentForm, AuthenticationForm, UserCheckForm
from Subscrap.forms import *
from Subscrap.models import *
from Subscrap.helperfunctions import *
from django.contrib import messages                             # to display messsages in html
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator                     # Pagination of pages
from django.views.decorators.cache import cache_control         # to get rid of browser cache browsing 
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.template.loader import render_to_string             # Email Message
from django.core.mail import EmailMessage




################# Landing Views Functions ###################

def home(request):
	#make_sub()
	return render(request, 'subscrap/home.html')


#@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
login_required(login_url='/login')
def main(request):
	curruser = request.user
	expense = sublist.objects.filter(
        startDate__year=datetime.today().year, author=curruser.id)
	expenselist = sublist.objects.filter(author = curruser.id)

	today = datetime.now()
	if today.day == 1:
			item.is_notified = False
			item.save(update_fields=['is_notified'])
			
	for item in expenselist:
		if ( item.is_active == True ):
			if datetime.now().date() > item.dueDate:
				item.is_active = False
				item.save(update_fields=['is_active'])
				
				#expire_email_notification
				if (item.is_notified == False):
					template = render_to_string(
						'subscrap/expire_template.html', {'name': curruser.username, 'subscription': item.name})
					email = EmailMessage(
						'Subscription has expired!',
						template,
						settings.EMAIL_HOST_USER,
						[curruser.email],
						)
					email.fail_silently = False
					email.send()
					item.is_notified = True
					item.save(update_fields=['is_notified'])
		
		if (item.is_autorenewal== True and item.is_active == True):
			if datetime.now().date() > item.dueDate:
				item.startDate = datetime.now().date()
				item.save(update_fields=['startDate'])

				#renew_email
				if (item.is_notified == False):
					template = render_to_string(
						'subscrap/renew_template.html', {'name': curruser.username, 'subscription': item.name})
					email = EmailMessage(
						'Subscription has been Renewed!',
						template,
						settings.EMAIL_HOST_USER,
						[curruser.email],
						)
					email.fail_silently = False
					email.send()
					item.is_notified = True
					item.save(update_fields=['is_notified'])
	
	payments = list((expense.annotate(month=Month('startDate')).values('month').annotate(total=Sum('cost')).order_by('month')))
	paymentMonths = []
	paymentTotal = []
	for i in payments:
		paymentMonths = (i["month"])
		paymentTotal = (i["total"])

		monthname = month_name(paymentMonths)

		obj, created = Payment.objects.update_or_create(
			author=curruser,
            month=monthname,
            defaults={"total": paymentTotal},
			)	

	yearcost = Payment.objects.filter(author=curruser.id)
	p = Paginator(sublist.objects.filter(author = curruser.id), 7 )
	page = request.GET.get('page')
	expense = p.get_page(page)

	total_price = gettotalcost()
	
	return render (request, 'subscrap/main.html', {'student': curruser, 'sublist': expense, 'totalcost':total_price, 'yearcost':yearcost})




################# Registration Views Functions ###################

def registration(request):
	context = {}
	if request.POST:
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			Login(request, account)
			return redirect('/login')
		else:
			context['registration_form'] = form

	else:
		form = StudentForm()
		context['registration_form'] = form
	return render(request, 'Subscrap/signup.html', context)



def login(request):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("/")

	if request.POST:
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				Login(request, user)
				return redirect("/")

	else:
		form = AuthenticationForm()

	context['login_form'] = form

	return render(request, "Subscrap/templates/login.html", context)



def Log_out(request):
	logout(request)
	return redirect("/")




################# Data Manipualtion Views Functions ###################



def addnew(request):
	if request.method == 'POST':
		form = SublistForm(request.POST)
		if form.is_valid():
			try:
				form.instance.author = request.user

				form.save()
				curruser = request.user
				expense = sublist.objects.filter(author = curruser.id)
				total = expense.count() - 1

				currentSublist = expense[total]
				currentDueDate = gettheduedate(currentSublist.startDate,currentSublist.renewalcycle)

				obj, created = sublist.objects.update_or_create(
					author = curruser,
    				name = currentSublist.name,
    				cost = currentSublist.cost,
    				renewalcycle = currentSublist.renewalcycle,
					image = currentSublist.image,
					subtype = currentSublist.subtype,
					website = currentSublist.website,
    				startDate = currentSublist.startDate,
    				dueDate = currentSublist.dueDate,
					is_active = currentSublist.is_active,
					is_autorenewal = currentSublist.is_autorenewal,
					defaults={"dueDate" : currentDueDate}
					
				)
			
				return redirect('/main')
			except:
			
				pass
		else:
			messages.success(request, 'Error')
			pass
	else:
		form = SublistForm()
	return render(request, 'subscrap/addnew.html', {'form': form})



@login_required(login_url='/login')
def addpresavedsubscription(request,id):
	expense = prebuildsublist.objects.filter(id = id)
	initial_data = {
		'name' : expense[0].name,
		'image' : expense[0].image,
		'website' : expense[0].website,
		'subtype': expense[0].subtype
		}
	if request.method == 'POST':
		
		curruser = request.user
		
		form = SublistForm(request.POST)
		if form.is_valid():
			try:
				form.instance.image = expense[0].image 
				form.instance.author = request.user				
				form.save()

				expense = sublist.objects.filter(author = curruser.id)
				total = expense.count() - 1

				currentSublist = expense[total]
				currentDueDate = gettheduedate(currentSublist.startDate,currentSublist.renewalcycle)

				obj, created = sublist.objects.update_or_create(
					author = curruser,
    				name = currentSublist.name,
    				cost = currentSublist.cost,
    				renewalcycle = currentSublist.renewalcycle,
					image = currentSublist.image,
					subtype = currentSublist.subtype,
					website = currentSublist.website,
    				startDate = currentSublist.startDate,
    				dueDate = currentSublist.dueDate,
					is_active = currentSublist.is_active,
					is_autorenewal = currentSublist.is_autorenewal,
					defaults={"dueDate" : currentDueDate}
					
				)
			

				return redirect('/main')
			except:
				pass
		else:
			messages.success(request, 'Error')
			pass
	else:
		form = SublistForm(initial=initial_data)
	return render(request, 'subscrap/addnew.html', {'form': form})



def edituserprofile(request):
	user = request.user
	form = UserEditForm(instance=user)
	if request.method == 'POST':
		form = UserEditForm(request.POST, request.FILES, instance = user)
		if form.is_valid():
			form.save()
	context = {'form': form }
	return render (request, 'subscrap/editprofile.html', context)

@login_required(login_url='/login')
def useraccountsettings(request):
	user = request.user
	form = AccountEditForm(instance=user)
	if request.method == 'POST':
		form = AccountEditForm(request.POST, request.FILES, instance = user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, request.user)
	context = {'form': form }
	return render (request, 'subscrap/accountsettings.html', context)



def editusersub(request,id):
	sublistid = sublist.objects.get(id=id)
	form = SubscirptionEditForm(instance=sublistid)
	if request.method == 'POST':
		form = SubscirptionEditForm(request.POST, request.FILES, instance = sublistid)
		if form.is_valid():
			try:
				form.instance.author = request.user

				form.save()
				curruser = request.user
				expense = sublist.objects.filter(author = curruser.id, id = id)
				currentSublist = expense[0]
				currentDueDate = gettheduedate(currentSublist.startDate,currentSublist.renewalcycle)


				obj, created = sublist.objects.update_or_create(
					author = curruser,
    				name = currentSublist.name,
    				cost = currentSublist.cost,
    				renewalcycle = currentSublist.renewalcycle,
					image = currentSublist.image,
					subtype = currentSublist.subtype,
					website = currentSublist.website,
    				startDate = currentSublist.startDate,
    				dueDate = currentSublist.dueDate,
					is_active = currentSublist.is_active,
					is_autorenewal = currentSublist.is_autorenewal,
					defaults={"dueDate" : currentDueDate}
					
				)
			except:
				pass

	context = {'form': form ,'sublistitem': sublistid}
	return render (request, 'subscrap/editsubscription.html', context)


def deletelist(request,id):
      sublistid = sublist.objects.get(id=id)
      sublistid.delete()
      #messages.success(request, 'Success! Subscription Deleted')
      return redirect('/main')




################# (JSON,AJAX) Search Views Functions ###################


def search_user_sublist(request):
	if request.method == "POST":
		search_str = json.loads(request.body).get('SearchText')
		search_sublist = sublist.objects.filter(
		name__istartswith=search_str, author = request.user)| sublist.objects.filter(
		subtype__startswith=search_str, author = request.user )
		
		data = search_sublist.values()

	return JsonResponse(list(data), safe = False)



def ajaxview(request):
	return render(request, 'subscrap/ajax.html',{})



def search_results(request):
	if request.is_ajax():
		res = None
		presub = request.POST.get('presub')
		print(presub)
		qs = prebuildsublist.objects.filter(name__istartswith=presub)
		if  len(qs) > 0 and len(presub) > 0:
			data = []
			for pos in qs:
				item ={
				'id': pos.id,
				'name':pos.name,
				'image': str(pos.image.url)
				}
				data.append(item)
			res = data
		else:
			user = request.user
			if user.is_authenticated:
				res = "Subscription Does Not Exist"
			else:
				res = "Login To Add Custom Subscriptions"

		return JsonResponse({'data': res})

	return JsonResponse({})