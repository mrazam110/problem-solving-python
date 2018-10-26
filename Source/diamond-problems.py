# 0
# 0 0
# 0 0 0
# 0 0 0 0
# 0 0 0 0 0

for i in range(0, 5):
    for j in range(0, i+1):
        print(0, end = ' ')
    print()

print("--------------------\n")

# 0
# 0 0
# 0 0 0
# 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0
# 0 0 0
# 0 0
# 0

n = 5

for i in range(0, n):
    for j in range(0, i+1):
        print(0, end = ' ')
    print()
for i in range(n-1, 0, -1):
    for j in range(i, 0, -1):
        print(0, end = ' ')
    print()

print("--------------------\n")


#     0 
#    0 0 
#   0 0 0 
#  0 0 0 0 
# 0 0 0 0 0 

for i in range(0, n):
    # spaces
    for j in range(n, i, -1):
        print("", end=' ')
    # zeros
    for k in range(i+1):
        print("0", end=' ')
    print()

print("--------------------\n")

#     0 
#    0 0 
#   0 0 0 
#  0 0 0 0 
# 0 0 0 0 0 
#  0 0 0 0 
#   0 0 0 
#    0 0 
#     0 

for i in range(0, n):
    # spaces
    for j in range(n, i, -1):
        print("", end=' ')
    # zeros
    for k in range(i+1):
        print("0", end=' ')
    print()
for i in range(n-1, 0, -1):
    # spaces
    for j in range(i, n+1):
        print("", end=' ')
    # zeros
    for k in range(i):
        print("0", end=' ')
    print()
