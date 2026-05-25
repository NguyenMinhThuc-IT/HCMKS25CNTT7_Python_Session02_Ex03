try:
    # Nhap thong tin
    patient_name = input("Nhập họ tên bệnh nhân: ").strip()
    patient_age = int(input("Nhập tuổi bệnh nhân: "))

    if (
        patient_name == ""
        or patient_age < 0
        or patient_age > 150
    ):
        print("LỖI: Tên không hợp lệ hoặc tuổi ngoài phạm vi (0-150)!")

    else:

        if patient_age < 6:
            priority = (
                "ƯU TIÊN: Bệnh nhi - "
                "Chuyên phòng khám Nhi"
            )

        elif patient_age >= 80:
            priority = (
                "ƯU TIÊN: Người cao tuổi - "
                "Hỗ trợ xe lăn"
            )

        else:
            priority = (
                "KHÁM THƯỜNG: "
                "Lấy số thứ tự tại sảnh"
            )

        print("\n===== PHIẾU KHÁM BỆNH =====")
        print(f"Họ tên : {patient_name}")
        print(f"Tuổi : {patient_age}")
        print(f"Kết quả: {priority}")

except ValueError:
    print("LỖI: Dữ liệu tuổi không hợp lệ!")