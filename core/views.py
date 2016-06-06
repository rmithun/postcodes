import re
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from constants import REGEXES

# Create your views here.


@require_http_methods(["GET"])
def validate(request, postcode):
    """method to validate & format postcode"""
    try:
    	postcode = postcode.replace(' ','').upper()
    	inward_code = postcode[-3:]
    	outward_code = postcode[:-3]
    	postcode = outward_code +' '+inward_code
    	formatted_postcode = None
    	formatted = False
        if request.method == 'GET':
        	ai_regex = re.compile(REGEXES[8])
        	for regex in REGEXES:
        		re_gex = re.compile(regex)
        		matches = re_gex.findall(postcode)
        		if matches:
        			matches = list(sum(matches,()))
        			postcode = matches[0] + ' ' + matches[2]
        			formatted_postcode = re.sub('C\/O([[:space:]]{0,})', 'c/o ', postcode);
        			if (ai_regex.findall(postcode)):
        				formatted_postcode = 'AI-2640';
        			formatted = True
        			break;
        	if formatted:
        		response = json.dumps({'postcode':formatted_postcode,'message':"Postcode is valid","valid":True})
        	else:
        		response = json.dumps({'message':"The postcode is invalid","postcode":postcode,"valid":False})
        	return HttpResponse(response, status=200)
        else:
            return HttpResponse('Method not allowed', status=405)
    except Exception as e:
        print repr(e)
        return HttpResponse('Internal server error', status=500)
