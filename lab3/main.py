def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5: return 4.0
    if diem_so >= 7.0: return 3.0
    return 2.0

print("GPA point 4.0 of " ,tinh_diem_gpa(8.5), "with condition logic")

