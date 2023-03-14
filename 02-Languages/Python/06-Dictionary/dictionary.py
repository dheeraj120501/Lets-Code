import random

#Dictionary (and quiz implementation)
#A linear data structure that stores data as key-value pairs.
#Refer: dictionary.png

#create a dictionary
states = {'Maharashtra':'Bombay', 'UP':'Lucknow', 'MP': 'Bhopal'}

#print
print(type(states))
print(states)

#add/update
states['Maharashtra'] = 'Mumbai' #value of existing pair is updated, because key is duplicated
states['J&K'] = ['Srinagar', 'Jammu'] #new pair is added
states['Punjab'] = 'Chandigarh' #new pair is added
states['Haryana'] = 'Chandigarh' #new pair is added with duplicate value

#print
print(states)

#traverse (access every pair for processing)
for k in states:
    print(k, states[k], sep= ' -> ')


#another dictionary
ut = {'Pondicherry' : 'Puducherry', 'Lakshadweep' : 'Kavaratti', 'Andaman and Nicobar' : 'Port Blair'}
print(ut)

#Create a dictionary from a list
more_ut_list = ['Dadra and Nagar Haveli and Daman and Diu', 'Chandigarh', 'Delhi', 'Ladakh']
more_ut_dictionary = {}.fromkeys(more_ut_list, 'XYZ')
print(more_ut_dictionary)

#Merge all into a country
country ={}
country.update(states)
country.update(ut)
country.update(more_ut_dictionary)

#Fetch all the keys (as a sequence)
print(country.keys())

#Fetch all the values (as a sequence)
print(country.values())

print(country)

#search (using membership operator in)
if 'Pondicherry' in country:
    print('Pondicherry present in country')

print(country.get('Pondicherry')) #Fetch value associated with the key, returns value or None (on key not present)
print(country['Pondicherry'])#Fetch value associated with the key, returns value or raise KeyError if key not present

#Deleting a pair
#a dummy entries
country['pqr'] = '12345'
country['abc'] = '54321'
country['lmn'] = '11111'
print(country)
del country['pqr'] #deletes pair 'pqr' or raises KeyError if key doesnt exist.
print(country.pop('abc', 'Alternate Value')) #deletes pair 'abc' and returns the value of the pair. If key is not found then returns 'Alternate Value' (second parameter). If the 'Alternate Value' (second parameter) and the key, both, are not available then KeyError is raised.
print(country.popitem()) #deletes and returns the last pair of the dictionary. If dictionary is empty then it raises KeyError.
print(country)


#Quiz Implementation
score = 0
questions = [] #add 3 random yet unique numbers in list, say: 7,3,1
while len(questions) < 3:
    temp = random.randint(0, len(country)-1)
    if temp not in questions:
        questions.append(temp) 

#fetch the dictionary keys as a list
keys = list(country.keys())

#for each question [7,3,1]
for indx in questions:
    print('Enter captial of ', keys[indx])
    cap = input().lower()

    #isinstance : to check the datatype of an object
    if isinstance(country[keys[indx]], list):
        if cap.capitalize() in country[keys[indx]]:
            score+=2
        else:
            score-=1
    else:
        if country[keys[indx]].lower() == cap:
            score+=2
        else:
            score-=1

print('Score: ', score, '/6')
if score < 0:
    print('Shame on you!')

