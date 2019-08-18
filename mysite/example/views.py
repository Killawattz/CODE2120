from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
import random 

# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]

			jsob = json.loads(data)

			index = 0
			for i in jsob ["demo"]:
				index += 1
			index = jsob ["var"]+str(index) 


			return JsonResponse({"count":index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")




@csrf_exempt
def fib(request):
	
	jsob = {"startNumber": 0, "length": 20}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			###################################################
			#everything above this line is always required!!!!#
			###################################################

			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno + addno 
				addno = fibno - addno 


			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)



@csrf_exempt
def add(request):
	jsob = {"startNumber": 0, "length": 40}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			###################################################
			#everything above this line is always required!!!!#
			###################################################

			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			mathboi = startNumber
			addboi = 5
			timesboi = 10
			for l in loop:
				numarray.append(mathboi)
				mathboi = mathboi + addboi * timesboi  


			return JsonResponse({"add":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)


@csrf_exempt
def insult(request):
	
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)

			Insult1 = ["artless","bawdy","beslubbering","bootless","churlish","cockered","clouted","craven",
			"currish","dankish","dissembling","droning","errant","fawning","fobbing","froward","frothy","gleeking","goatish",
			"gorbellied","impertinent","infectious","jarring","loggerheaded"] 

			Insult2 = ["base-court","bat-fowling","beef-witted","beetle-headed","boil-brained","clapper-clawed","clay-brained","common-kissing","crook-pated",
			"dismal-dreaming","dizzy-eyed","doghearted","dread-bolted","earth-vexing","elf-skinned","fat-kidneyed","fen-sucked","flap-mouthed","fly-bitten",
			"folly-fallen","fool-born","full-gorged","guts-griping","half-faced"] 

			Insult3 = ["apple-john","baggage","barnacle","bladder","boar-pig","bugbear","bum-bailey","canker-blossom","clack-dish","clotpole","coxcomb","codpiece",
			"death-token","dewberry","flap-dragon","flax-wench","flirt-gill","foot-licker","fustilarian","giglet","gudgeon","haggard","harpy","hedge-pig"]

			sent = random.randrange(0,24)

			print('Thou' + Insult1[sent] + ' ' + Insult2[sent] + ' ' + Insult3[sent])

		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("nah didn't work")








