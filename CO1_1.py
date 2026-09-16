current_year=2026
final_year=int(input("Enter final year: "))
for year in range(current_year,final_year + 1):
    if year % 4==0:
        print(year)
