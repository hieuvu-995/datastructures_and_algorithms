# numbers = [3, 45, 2, 46, 5, 25, 65, 8, 57, 67]
# lenth = len(numbers)

# # Lặp từ phần tử đầu đến kế cuối,
# # Vì khi đến phần tử cuối là đã sắp xếp thànhcông
# for i in range(0, lenth - 1):
#     for j in range(i + 1, lenth):
#         if (numbers[i] > numbers[j]):
#             # Hoán đổi vị trí
#             tmp = numbers[i]
#             numbers[i] = numbers[j]
#             numbers[j] = tmp

# print(numbers)

while True:
    n = int(input("Enter number: "))
    if n < 0:
        print("Invalid number entered")
    else:
        break

for i in range(n):
    space = " "*(n-i-1)
    dots = "*"*(2*i + 1)
    print(space, dots)
