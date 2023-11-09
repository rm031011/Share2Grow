from django.shortcuts import render,redirect
from django.http import HttpResponse
from textblob import TextBlob
from digifest.models import Reviews
#from django.contrib.auth.forms import UserCreationForm
#from digifest.forms import UserRegistrationForm 
from django.contrib import messages
from .models import UserRegist
from django.template import loader
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords 
import pandas as pd
import nltk
#from digifest.dictonary import 
from digifest import dictonary
# import networkx as nx

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

matplotlib.use('agg')
# Create your views here.

reviews=["his organisation has a good plans and policies and all are very easy to understand.",
	"Sold my kidney to buy this, I am now in the hospital on dialysis and using this beautiful product. Just go for it, you won't regret it.",
	"Very bad product .For this price go and buy a gaming laptop.Dell inspiron 15 gaming laptop is better than this garbage",
	"he 15.4 inch 512 gig ssd has radeon pro 560x graphics card not 555x only 256 gig model has 555x card",
	"overpriced.... You could find a better windows laptop at 1/5 th of the price. Go for it only if you have no idea on how to spend 2.2 lakhs"]

def index(request):
	return render(request,'index.html')

def citpage(request):
	const=['kansascity','dallas']


	const1={
	'con1':const
	}
	return render(request,'vote.html',const1)

def log(request):
	# temp1=loader.get_template('pol_log.html')
	# return HttpResponse(temp1.render())
	return render(request, 'pol_log.html')

def signup(request):
	return render(request,'signup.html')

def manifest(request):
	return render(request,'mainifest.html')


def result(request):
	'''reviews=["his organisation has a good plans and policies and all are very easy to understand.",
		"Sold my kidney to buy this, I am now in the hospital on dialysis and using this beautiful product. Just go for it, you won't regret it.",
		"Very bad product .For this price go and buy a gaming laptop.Dell inspiron 15 gaming laptop is better than this garbage",
		"he 15.4 inch 512 gig ssd has radeon pro 560x graphics card not 555x only 256 gig model has 555x card",
		"overpriced.... You could find a better windows laptop at 1/5 th of the price. Go for it only if you have no idea on how to spend 2.2 lakhs"]
'''
	
	sr=[]
	sr1=[]
	#sr3=[]
	sr2=[]
	k=0

	# const_names = Reviews.objects.all()
	# uniq_const_names = set(const_names.ConstituencyName)


	for j in Reviews.objects.all():
		
		sr2.append(j.ConstituencyName)
		# print("sr2 is",sr2)
		#print(j.ConstituencyName)
		ri1=request.POST.get('retcon',False)
		#print("ri1 is ",ri1)
		if sr2[k]==ri1:
			#print("hi")
			sr1.append(j.reviews)
			#print("k value is",k)
			print('ri1' +ri1)
		k=k+1
	sr3=sr1.copy()
		#print(len(sr1))
	# print(sr3)
	
		
	pdReviews = pd.DataFrame(sr3, columns = ['pubReviews'])

	def processFun(txt):
		tokens = word_tokenize(txt)

		nonStopTok = [token for token in tokens if token not in stopwords.words('english')]
		print(nonStopTok)
		lemmat = WordNetLemmatizer()

		lemTok = [lemmat.lemmatize(token) for token in nonStopTok]

		process_txt = ' '.join(lemTok)

		return process_txt

	pdReviews['pubReviews'] = pdReviews['pubReviews'].apply(processFun)
	analyser = SentimentIntensityAnalyzer()

	def sentiAnaly(txt):

		score = analyser.polarity_scores(txt)
		print(score)

		sentiment = 1 if (score['compound']>0.5) else 0 #or score['pos'] >0.5

		return sentiment


	res = pdReviews['pubReviews'].apply(sentiAnaly)	

	pdReviews['Sentiments'] = pdReviews['pubReviews'].apply(sentiAnaly)
		# print(result)

	posDF = pdReviews.loc[pdReviews['Sentiments'].isin([1])]
	negDF = pdReviews.loc[pdReviews['Sentiments'].isin([0])]

	pos = posDF['pubReviews']
	neg = negDF['pubReviews']



	con={
		'review':sr3,
		'pos':pos,
		'neg':neg,
			#'con1':const

	}

	
	comm_words=' '
	#print(positive)
	for k in pos:
		print(k)
		token=k.split()
		print(token)
		for i in range(len(token)):
			token[i]=token[i].lower()
			for word in token:
				comm_words=comm_words+word+' '

	wordcloud=WordCloud(width=500,height=400,min_font_size=6).generate(comm_words)
	fig=plt.figure(figsize=(10,10))
	plt.imshow(wordcloud)
		#plt.axis("off")
	fig.savefig('digifest/static/img/pos_plot.jpg')


	
	comm_words1=' '
		#print(positive)
	for k in neg:
			#print(k)
		token=k.split()
			#print(token)
		for i in range(len(token)):
			token[i]=token[i].lower()
			for word in token:
				comm_words1=comm_words1+word+' '

	wordcloud=WordCloud(width=500,height=400,min_font_size=6).generate(comm_words1)
	fig=plt.figure(figsize=(10,10))
	plt.imshow(wordcloud)
		#plt.axis("off")
	fig.savefig('digifest/static/img/neg_plot.jpg')



	return render(request,'result.html',con)	

def register(request):
	
	'''if request.method=='POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Acoount creates for {username}')
			return redirect('home')
	else:
		form=UserRegistrationForm()'''
	if request.method == "POST":
		first=request.POST["fname"]
		last=request.POST["lname"]
		uname=request.POST["uname"]
		emailid=request.POST["email"]
		passw=request.POST["pass"]
		cpassw=request.POST["cpass"]

		user=UserRegist(fname=first,lname=last,username=uname,email=emailid,password=passw,cpassword=cpassw)
		user.save()
		return redirect('home')

	else:
		return redirect('signup.html')

def logged(request):

	if request.method == "POST":
		
		#use=UserRegist.objects.all()
		
		const=['kansascity','dallas']

		const1={
		'const2':const
		}


		for i in UserRegist.objects.all():
			email1=i.email
			passw=i.password

			if (email1==request.POST["username1"]) and (passw==request.POST["password1"]):
				return render(request,'mainifest.html',const1)
		return render(request,'hi.html')

	else:
		return render(request, 'mainifest.html')
	

def ins_rev(request):


	if request.method=="POST":
		cn=request.POST['selconst']
		repro=request.POST['yp']

		revi=Reviews(ConstituencyName=cn,reviews=repro)
		revi.save()
		return HttpResponse("<h3>Successfully Sent!</h3>")
	else:
		return redirect('vote.html')


def ind(request):
	return redirect('index.html')

def problem(request):
	return redirect('index.html')

def list(request):
	sr=[]
	sr1=[]
	for j in Reviews.objects.all():
		sr.append(j.reviews)
		if len(sr)>22:
			# print(len(sr))
			sr1.append(j.reviews)
			

	conlist={
	'list1':sr1
	}

	return render(request,'result1.html',conlist)