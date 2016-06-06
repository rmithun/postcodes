# Postcodes
API to validate and fromat postcodes

Django application to validate and format UK postcodes.

#How to validate
  
  Run the App
  
    1.Start the server at 8000
    
    2.Go to 'http://localhost:8000/'
    
    3.Input the postcode to be validated and click 'Go'
    
    4.The response will be rendered
  
  
  API to validate postcode
  
    http://localhost:8000/postcode/validate/:postcode_string
    
    Valid Response:
    
      {"message": "The postcode is valid", "valid": true, "postcode": "DN55 1PT"}
      
    Invalid Response:
    
      {"message": "The postcode is valid", "valid": true, "postcode": "DN55 1PT"}
