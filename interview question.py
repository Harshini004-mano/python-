a=[1]
b=a
b+=[2]
b.append(3)
b=b+[4]
b.append(5)
print(a)
print(b)

#Step	Operation	        a	        b          Shared?
#1	    a=[1]	            [1]	        —       	—
#2	    b=a             	[1]	        [1]	        ✅ same
#3    	b+=[2]          	[1,2]	    [1,2]	    ✅ same
#4	    b.append(3)     	[1,2,3]	    [1,2,3]	    ✅ same
#5	    b=b+[4]	            [1,2,3]	    [1,2,3,4]	❌ new list
#6	    b.append(5)	        [1,2,3] 	[1,2,3,4,5]