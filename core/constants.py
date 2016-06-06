""" Core constants module"""

#Permitted chars on the postcodes dependin on their position.
FIRST_CHAR = '[ABCDEFGHIJKLMNOPRSTUWYZ]'
SECOND_CHAR = '[ABCDEFGHKLMNOPQRSTUVWXY]'
THIRD_CHAR = '[ABCDEFGHJKPMNRSTUVWXY]'
FOURTH_CHAR = '[ABEHMNPRVWXY]'
FIFTH_CHAR = '[ABDEFGHJLNPQRSTUWXYZ]'
BFPO_CHAR5 = '[ABDEFGHJLNPQRST]{1}'
BFPO_CHAR6 = '[ABDEFGHJLNPQRSTUWZYZ]{1}'


# REGEX for BF1 type postcodes 
REGEXES = []

# Expression for BF1 type postcodes 
REGEXES.append('^(BF1)([[" " ]]{0,})([0-9]{1}' + BFPO_CHAR5 + BFPO_CHAR6 +')$')


# Expression for postcodes: AN NAA, ANN NAA, AAN NAA, and AANN NAA with a space
REGEXES.append('^('+FIRST_CHAR+'{1}'+SECOND_CHAR+'{0,1}[0-9]{1,2})([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')

# Expression for postcodes: ANA NAA
REGEXES.append('^('+FIRST_CHAR+'{1}[0-9]{1}'+SECOND_CHAR+'{1})([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')

# Expression for postcodes: AANA NAA
REGEXES.append('^('+FIRST_CHAR+'{1}'+SECOND_CHAR+'{1}[0-9]{1}'+FOURTH_CHAR+')([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')
  
# Exception for the special postcode GIR 0AA
REGEXES.append('^(GIR)([[" " ]]{0,})(0AA)$')
  
# Standard BFPO numbers
REGEXES.append('^(BFPO)([[" " ]]{0,})([0-9]{1,4})$')
  
# c/o BFPO numberss
REGEXES.append('^(BFPO)([[" " ]]{0,})(c\/o([[" " ]]{0,})[0-9]{1,3})$')
  
# Overseas Territories
REGEXES.append('^([A-Z]{4})([[" " ]]{0,})(1ZZ)$')
  
# Anquilla
REGEXES.append('^AI-2640$')

