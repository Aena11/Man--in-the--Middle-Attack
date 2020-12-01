# tom is a hacker or attacker!!
#2 Large prime numbers n and g these numbers are publicly known
n=int(input("Enter the value for n:(Must be a prime value):>>  "))
g=int(input("Enter the value for g:(Must be a prime value):>>  "))


#alice
x=int(input("Enter the value for alice's key:-> "))
A_a=(g**x)%n


#bob
y=int(input("Enter the value for bob's key:-> "))
B_b=(g**y)%n

#tom(hacker)
x_tom=int(input("Enter the value for tom's key :-> "))
y_tom=int(input("Enter the value for tom's key:-> "))
T_a=(g**x_tom)%n
T_b=(g**y_tom)%n


#Key gen in alice
k1=(T_b**x)%n
#Key gen in bob
k2=(T_a**y)%n
#Key gen in tom
k1_tom=(B_b**x_tom)%n
k2_tom=(A_a**y_tom)%n

print("\n\nAlice's Key "+ str(k1))
print("Tom's key "+ str(k2_tom))
print("\n\nBob's Key "+ str(k2))
print("Tom's key "+ str(k1_tom))
