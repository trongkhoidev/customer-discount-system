def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5: return 4.0
    return round((diem_so/10)*4,2)

print("GPA point 4.0 of " ,tinh_diem_gpa(8.5), "with mixture logic")

