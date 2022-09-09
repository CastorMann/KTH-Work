# Denna lösning ger WA på TC3, ej färdig

guests = set()
n = int(input())
names = []
for _ in range(n): names.append(input().strip())
for i in range(n):
    names[i] += input().strip()
print(len(set(names)))