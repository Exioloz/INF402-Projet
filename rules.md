# (n x n) futoshiki rules:

C(x, i, j) := The case (i, j) contains the number x.  

## Each case contains a number in the set {1, ..., n}

### Has to contain a number

with (i, j) as a valid case:  
    sum(x in {1, ..., n})  
        { C(x, i, j) }  

### That is unique

with (i, j) as a valid case:  
    prod(x in {1, ..., n-1})  
    prod(y in {x+1, ..., n})  
        { -C(x, i, j) + -C(y, i, j) }  

### Numbers have to respect pre-assigned values

with (i, j) a valid case being assigned the number x:
	C(x, i, j)

## Each line can't contain two times the same number

with x as a number in {1, ..., n}:  
    prod(i1 in {1, ..., n-1})  
    prod(i2 in {i1+1, ..., n})  
        { -C(x, i1, j) + -C(x, i2, j) }  

## Each columns can't contain two times the same number

with x as a number in {1, ..., n}:  
    prod(j1 in {1, ..., n-1})  
    prod(j2 in {j1+1, ..., n})  
        { -C(x, i, j1) + -C(x, i, j2) }  

## Numbers have to respect inequality operators

with (i, j) < (k, l) as two valid cases:  
    -C(n, i, j)  
    -C(1, k, l)  
    prod{x in {2, ..., n}}  
        -C(x, k, l) + sum(y in {x-1, ..., 1}) { C(y, i, j) }  
