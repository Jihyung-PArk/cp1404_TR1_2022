import random

print(random.randint(5, 20))        #line 1
print(random.randrange(3, 10, 2))   #line 2
print(random.uniform(2.5, 5.5))     #line 3

'''
1st run
20
5
3.7935503407011812

2nd run
5
9
2.736981362292097

3rd run
17
7
5.272194402964981

4th run
10
9
4.5397124873003065

5th run
7
7
3.952920293255134

6th run
5
5
5.373176830027887

7th run
5
3
3.2115084400494376
'''

'''
Questions
1. What did you see on line 1?
  =>20, 5, 17, 10, 7, 5, 5
   What was the smallest number you could have seen, what was the largest?
  =>The smallest number was 5 and the largest number was 20
  
2. What did you see on line 2?
  =>5, 9, 7, 9, 7, 5, 3
   What was the smallest number you could have seen, what was the largest?
  =>The smallest number was 3 and the largest number was 9
   Could line 2 have produced a 4?
  => no, it could not. Because step is 2, only 3, 5, 7, 9 exit
  
3. What did you see on line 3?
  =>3.7935503407011812, 2.736981362292097, 5.272194402964981, 4.5397124873003065, 
    3.952920293255134, 5.373176830027887, 3.2115084400494376
   What was the smallest number you could have seen, what was the largest?
  =>The smallest number was 2.736981362292097 and the largest number was 5.373176830027887
   
4. Write code, not a comment, to produce a random number between 1 and 100 inclusive.
  =? random.randint(1, 100>
  '''