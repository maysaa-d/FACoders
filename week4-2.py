s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name = str(input("Enter student's name:"))
if name in s1 :
    print('Ahmad'), s1.remove('Ahmad') and sum(s1)
elif name in s2 :
    print('Sami'), s2.remove('Sami') and sum(s2)
elif name in s3 :
    print('Faris'),s3.remove('Faris') and sum(s3)
else:
    print("student  is not recorded" ,str('0'))
