def tinh_diem_gpa(diem_so):
    # to do: need to logic exchanging into 4.0 scale 
    return round((diem_so/10)*4,2)

print("GPA point 4.0 of " ,tinh_diem_gpa(8.5), "with linear logic")

