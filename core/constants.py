""" Core constants module"""

#Permitted chars on the postcodes dependin on their position.
FIRST_CHAR = '[ABCDEFGHIJKLMNOPRSTUWYZ]'
SECOND_CHAR = '[ABCDEFGHKLMNOPQRSTUVWXY]'
THIRD_CHAR = '[ABCDEFGHJKPMNRSTUVWXY]'
FOURTH_CHAR = '[ABEHMNPRVWXY]'
FIFTH_CHAR = '[ABDEFGHJLNPQRSTUWXYZ]'
BFPO_CHAR5 = '[ABDEFGHJLNPQRST]{1}'
BFPO_CHAR6 = '[ABDEFGHJLNPQRSTUWZYZ]{1}'


REGEXES = []


# Expression for postcodes: ANA NAA
REGEXES.append('^('+FIRST_CHAR+'{1}[0-9]{1}'+SECOND_CHAR+'{1})([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')

# Expression for postcodes: AANA NAA
REGEXES.append('^('+FIRST_CHAR+'{1}'+SECOND_CHAR+'{1}[0-9]{1}'+FOURTH_CHAR+')([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')
  
  
# Exception for the  GIR 0AA
REGEXES.append('^(GIR)([[" " ]]{0,})(0AA)$')
  
# Standard BFPO numbers
REGEXES.append('^(BFPO)([[" " ]]{0,})([0-9]{1,4})$')
  
# BFPO numberss
REGEXES.append('^(BFPO)([[" " ]]{0,})(c\/o([[" " ]]{0,})[0-9]{1,3})$')
  
# Other Territories
REGEXES.append('^([A-Z]{4})([[" " ]]{0,})(1ZZ)$')

# BF1 type postcodes 
REGEXES.append('^(BF1)([[" " ]]{0,})([0-9]{1}' + BFPO_CHAR5 + BFPO_CHAR6 +')$')

# Expression for postcodes: ANN NAA, AN NAA, AANN NAA and AAN NAA
REGEXES.append('^('+FIRST_CHAR+'{1}'+SECOND_CHAR+'{0,1}[0-9]{1,2})([[" " ]]{0,})([0-9]{1}'+FIFTH_CHAR+'{2})$')

# AI-2640
REGEXES.append('^AI-2640$')

