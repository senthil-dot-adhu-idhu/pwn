from pwn import *

p = remote('challenges.traboda.com', 30840)

#level1
p.recv()
p.sendline(b"madrid")

#level2
p.recv()
p.sendline(b"vincent van gogh")

#level3
p.recv()
p.sendline(b"alan turing")

#level4 (a)
p.recvuntil("Find their mean!\n\n")
a=p.recv()

data1 = a.decode("utf-8")
list=data1.split()

numbers = []
for item in list:
    if(item.isdigit()):
        numbers.append(item)

sum_of_five_stud=0
for i in numbers:
    sum_of_five_stud=sum_of_five_stud+int(i)
mean=sum_of_five_stud/5
p.sendline(str(int(mean)))

#level4 (b)
b=p.recv()
data2 = b.decode("utf-8")
list=data2.split()

number = []
for item in list:
    if(item.isdigit()):
        number.append(int(item))

tot_stud=number[0]+5
sum_of_scores_tot_stud=mean*tot_stud
sum_of_scores_new_stud=sum_of_scores_tot_stud-sum_of_five_stud
p.sendline(str(int(sum_of_scores_new_stud)))

#level5
p.recvuntil("order!\n")
c=p.recv()
data3 = c.decode("utf-8")
list=data3.split()

numbers = []
for item in list:
    if(item.isdigit()):
        numbers.append(int(item))
numbers.sort()
p.sendline(str(numbers))

#level6 Sub-level: 1
p.recv()
p.sendline(b'crypto{ASCII_pr1nt4bl3}')

# #level6 Sub-level: 2
p.recv()
p.sendline(b'EMYPU DDVAQ')

# #level6 Sub-level: 3
p.recv()
p.sendline(b'13371337')

# #level6 Sub-level: 4
p.recv()
p.sendline(b'YELLOW SUBMARINE!!')

#level7
p.recv()
p.sendline(b'flag{I_am_Sm0r7!_Y0u_c4n7_b347_m3!!}')

# for i in ran
p.interactive()
# p.recv()
