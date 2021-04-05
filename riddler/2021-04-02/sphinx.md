Can't figure out the closed form for the value in terms of n,q
```
       2    3    4    5     6     7
q = 2: 2    4    8    16    32    64
q = 3: 1    1.3  1.6  2     2.461 3.0476

3,3: 1.33 = 4/3
4,3: 1.6  = 4/3 + 4/15  = 8/5
5,3: 2    = 16/8
6,3: 2.4615384615384617 = 32/13

is the pattern 2^n/fib(n)?
7,3 = 64/21? Yes, = 3.047619047619048

q = 4
3,4: 1                 = 4/4
4,4: 1.142857142857143 = 8/7
5,4: 1.230769230769230 = 16/13
6,4: 1.333333333333333 = 32/24
7,4: 1.454545454545455 = 64/44
8,5: 1.580246913580247 = 128/81
9,5: 1.718120805369128 = 256/149

q = 5
2,5: 1                  = 2/2
3,5: 1                  = 4/4
4,5: 1                  = 8/8
5,5: 1.0666666666666667 = 16/15
6,5: 1.103448275862069  = 32/29
7,5: 1.1428571428571428 = 64/56
8,5: 1.1851851851851851 = 128/108
9,5: 1.2307692307692306 = 256/208

denoms:
q=3: 5,8,13,21 (+3, +5, +8) (*2-1, *2-2, *2-3)
q=4: 7,13,24,44 (+6, +11, +20) (*2-1, *2-2, *2-4, *2-7, *2-13)
q=5: 15,29,56 (+14, +17) (*2-1, *2-2, *2-4, *2-8)

1,2,4,7,13 is the tribonnaci sequence.
Ah,
So the answer is that F(N,Q) = 2^(N-1)/nnacci(n=Q-1,i=N+Q-2)
```

### Here's what I submitted: 
Dunno if you all have an even simpler formulation, but the simplest way I was able to get was F(n,q) = 2^(n-1)/n_nacci_{q-1}(n+q-2) where n_nacci_{a}(b) is the bth a-nacci number (where 2-nacci=fibonacci = (starting with the 0th term:) 0,1,1,2,3,5,... and 3-nacci=0,0,1,1,2,4,7...

### And for "Show your work" I said:
For the first part, I drew out the tree consisting of all the possible answers that the Sphinx could dictate.  Anywhere the Sphinx only has 1 possible answer, you may "all-in" and thus double your money.  At any other junction, you may bet a value of x on "true" (if x is negative, then bet -x on "false").  x is given by setting the payout of "true" and "false" equal to each other.  That is, (1+y)*p_1 = (1-y)*p_2.  This means the value of the junction is 2*p1*p2/(p1+p2).  Working our way from the bottom of the tree up gives up the answer 1.6

For the second part, I spent a long fucking time (10 hours, maybe??? you destroyed my weekend!!!) looking at the game tree and trying various simplifications of the game tree, including a recursive formula for F(n,q) in terms of `F(n-i,q)` for `i = 1,...,q`.  The recursive formula involved `q` iterative applications of the `2*p1*p2/(p1+p2)` formula though, and I couldn't figure out how to simplify that any further.

So out of desperation, I found the values for various values of F (like F(5,3), F(6,3), F(5,4), etc) using a python program that implements the `2*p1*p2/(p1+p2)` logic.  And I googled the decimal values it spat out, like `1.103448275862069`.  The google results showed that this was 32/29.  I googled a few more values and inspected the results to find a pattern.  Eventually, I figured out the pattern I submitted as the answer above, which e.g. gives the values for F(4,5), F(5,5), F(6,5), etc. as 8/8, 16/15, 32/29, 64/56, 128/108, 256/208.