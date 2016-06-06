# Postcodes
API to validate and fromat postcodes

Django application to validate and format UK postcodes.

#How to validate
  http://localhost:8000/postcode/validate/:postcode_string
  
  Valid Response:
  
    {"message": "The postcode is valid", "valid": true, "postcode": "DN55 1PT"}
    
  Invalid Response:
  
    {"message": "The postcode is valid", "valid": true, "postcode": "DN55 1PT"}
