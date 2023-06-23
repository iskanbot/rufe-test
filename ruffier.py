''' Module for calculating the results of the Rufier test.
 
The sum of heart rate measurements in three attempts (before exercise, immediately after and after a short rest)
Ideally, there should be no more than 200 beats per minute.
We suggest that children measure their pulse for 15 seconds,
and we bring the result to beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The farther this result is from the ideal 200 strokes, the worse.
Traditionally, tables are given for a value divided by 10.
 
Rufier Index 
   IR = (S - 200) / 10
Evaluated according to the table according to age:
 7-8 9-10 11-12 13-14 15+ (teens only!)
ex. 6.4 and less 4.9 and less than 3.4 and less than 1.9 and less than 0.4 and less
chor. 6.5 - 11.9 5 - 10.4 3.5 - 8.9 2 - 7.4 0.5 - 5.9
udovl. 12 - 16.9 10.5 - 15.4 9 - 13.9 7.5 - 12.4 6 - 10.9
weak 17 - 20.9 15.5 - 19.4 14 - 17.9 12.5 - 16.4 11 - 14.9
21 and more 19.5 and more 18 and more 16.5 and more 15 and more
 
For all ages, the result of "failure" is 4 away from "weak",
the one from "satisfactory" to 5, and the "good" from "ud" to 5.5
 
Therefore, let's write the function ruffier_result(r_index, level), which will receive
the calculated Rufier index and the level of "failure" for the age of the test taker, and give the result
 
'''
# here are the lines with which the result is stated:
txt_index = "Your Rufier index: "
txt_workheart = "Heart health: "
txt_nodata = '''
There is no data for this age'''
txt_res = []
txt_res. append('''низкая.
Consult a doctor immediately!''')
txt_res. append('''удовлетворительная.
See your doctor!''')
txt_res. append('''средняя.
It may be worthwhile to be further examined by a doctor.''')
txt_res. append('''
Above Average''')
txt_res. append('''
high''')

def ruffier_index(P1, P2, P3):
   ''' returns the index value for three heart rate indicators for comparison with the table'''
   return (4 * (P1+P2+P3) - 200) / 10

def neud_level(age):
   ''' options with an age of less than 7 and adults need to be treated separately,
 Here we select the "failure" level only inside the table:
 At the age of 7 years, "failure" is an index of 21, then every 2 years it drops by 1.5 to a value of 15 at 15-16 years old '''
   norm_age = (min(age, 15) - 7)   2 # every 2 years, differences from 7 years turn into one - up to 15 years  
   result = 21 - norm_age * 1.5 # multiply every 2 years of the difference by 1.5, this is how the levels in the table are distributed 
   return result

def ruffier_result(r_index, level):
   ''' function gets the Rufier index and interprets it,
 Returns the readiness level: a number between 0 and 4
 (the higher the level of readiness, the better). '''
   if r_index >= level:
       return 0
    level = level - 4 # this will not be executed if we have already returned a "bad" response
   if r_index >= level:
       return 1
    level = level - 5 # similarly, we get here if the level is at least "ud" 
   if r_index >= level:
       return 2
   level = level - 5.5 # следующий уровень
   if r_index >= level:
       return 3
   return 4 # are here if the index is less than all intermediate levels, i.e. the tested one is cool.

def test(P1, P2, P3, age):
   ''' this function can be used outside the module to calculate the Rufier index.
 Returns ready-made texts that remain to be drawn in the desired place
 Uses the constants specified at the beginning of this module for texts. '''
   if age < 7:
       return (txt_index + "0", txt_nodata) # This mystery is not for this test
   else:
       ruff_index = ruffier_index(P1, P2, P3) # расчет
       result = txt_res[ruffier_result(ruff_index, neud_level(age))] # interpretation, translation of numerical level of training into text data
       res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
       return res
