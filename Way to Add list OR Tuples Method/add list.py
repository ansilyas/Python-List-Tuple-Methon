#%%
A=[2,3,45,5,1,]
A=A+[1]
A

# We can also like (string) like this:
A=A+["BAD"]
A
#another Way;
#But it add them Separately:
A=A+list("BAD")
A
#_________________________#
#Add (Number) in the list:
A=A+[123]
A
# We can convet the (number) into (string):
#A=A+str(1,2,3) this will not work.
A=A+list(str(123))
A
#Make or Add list (inside) the list:
A=A+[[1,8,3,8]]
A
A[-1]
#_________________________#
#Insert Method:
#Insert Between two number:
A=[2,4,2,50,120,]
A.insert(2,1000)
A
A.insert(2,[0,0,1])
A
#Replace the number:
A=[1,2,4,4]
A
A[2]=3
A

# %%
