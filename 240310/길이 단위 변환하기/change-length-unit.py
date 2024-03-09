ft_cm = 30.48
mi_cm = 160934

ft_a = 9.2
mi_a = 1.3

ft_cm = round(ft_a * ft_cm, 1)
mi_cm = round(mi_a * mi_cm, 1)

print(f"{ft_a}ft = {ft_cm}cm")
print(f"{mi_a}mi = {mi_cm}cm")