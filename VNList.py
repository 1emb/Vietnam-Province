import json

list = []

list.append("An Giang")
list.append("Bà Rịa -Vũng Tàu")
list.append("Bắc Giang")
list.append("Bắc Kạn")
list.append("Bạc Liêu")
list.append("Bắc Ninh")
list.append("Bến Tre")
list.append("Bình Định")
list.append("Bình Dương")
list.append("Bình Phước")
list.append("Bình Thuận")
list.append("Cà Mau")
list.append("Cần Thơn")
list.append("Cao Bằng")
list.append("Đà Nẵng")
list.append("Đăk Lăk")
list.append("Đăk Nông")
list.append("Điện Biên")
list.append("Đồng Nai")
list.append("Đồng Tháp")
list.append("Gia Lai")
list.append("Hà Giang")
list.append("Hà Nam")
list.append("Hà Nội")
list.append("Hà Tĩnh")
list.append("Hải Dương")
list.append("Hải Phòng")
list.append("Hậu Giang")
list.append("Hòa Bình")
list.append("Hưng Yên")
list.append("Khánh Hòa")
list.append("Kien Giang")
list.append("Kon Tum")
list.append("Lai Châu")
list.append("Lâm Đồng")
list.append("Lạng Sơn")
list.append("Lào Cai")
list.append("Long An")
list.append("Nam Định")
list.append("Nghệ An")
list.append("Ninh Bình")
list.append("Ninh Thuận")
list.append("Phú Thọ")
list.append("Phú Yên")
list.append("Quản Bình")
list.append("Quảng Nam")
list.append("Quảng Ngãi")
list.append("Quảng Ninh")
list.append("Quảng Trị")
list.append("Sóc Trăng")
list.append("Sơn La")
list.append("Tây Ninh")
list.append("Thái Bình")
list.append("Thái Nguyên")
list.append("Thanh Hóa")
list.append("Thừa Thiên Huế")
list.append("Tiền Giang")
list.append("TP. Hồ Chí Minh")
list.append("Trà Vinh")
list.append("Tuyên Quang")
list.append("Vĩnh Long")
list.append("Vĩnh Phúc")
list.append("Yên Bái")

dic = {    
}
for i in range(0, len(list)):
    dic[list[i]] = i+1 
VN = {}
VN["Province"] = {}
for i in range(0, len(list)):
    VN["Province"][list[i]] = {}

def link(provinceName, provinceNeighbor):
    try:
        VN["Province"][provinceName][list.index(provinceNeighbor)] = provinceNeighbor            
    except:
        pass
    
    try:
        VN["Province"][provinceNeighbor][list.index(provinceName)] = provinceName
    except:
        pass
    
a1 = "Điện Biên"
link(a1, "Lai Châu")
link(a1, "Sơn La")

a2 = "Lai Châu"
link(a2, "Sơn La")
link(a2, "Yên Bái")
link(a2, "Lào Cai")

a3 = "Lào Cai"
link(a3, "Yên Bái")
link(a3, "Hà Giang")

a4 = "Hà Giang"
link(a4, "Yên Bái")
link(a4, "Tuyên Quang")
link(a4, "Cao Bằng")

a5 = "Cao Bằng"
link(a5, "Tuyên Quang")
link(a5, "Bắc Kạn")
link(a5, "Lạng Sơn")

a6 = "Yên Bái"
link(a6, "Tuyên Quang")
link(a6, "Sơn La")
link(a6, "Phú Thọ")

a7 = "Tuyên Quang"
link(a7, "Phú Thọ")
link(a7, "Vĩnh Phúc")
link(a7, "Thái Nguyên")
link(a7, "Bắc Kạn")

a8 = "Bắc Kạn"
link(a8, "Thái Nguyên")
link(a8, "Lạng Sơn")

a9 = "Lạng Sơn"
link(a9, "Thái Nguyên")
link(a9, "Bắc Giang")
link(a9, "Quảng Ninh")

a10 = "Sơn La"
link(a10, "Phú Thọ")
link(a10, "Hòa Bình")
link(a10, "Thanh Hóa")

a11 = "Phú Thọ"
link(a11, "Vĩnh Phúc")
link(a11, "Hà Nội")
link(a11,"Hòa Bình")

a12 = "Thái Nguyên"
link(a12, "Hà Nội")
link(a12, "Bắc Giang")

a13 = "Bắc Giang"
link(a13, "Hà Nội")
link(a13, "Bắc Ninh")
link(a13, "Hải Dương")
link(a13, "Quảng Ninh")

a14 = "Quảng Ninh"
link(a14, "Hải Dương")
link(a14, "Hải Phòng")

a15 = "Hòa Bình"
link(a15, "Thanh Hóa")
link(a15, "Ninh Bình")
link(a15, "Hà Nam")
link(a15, "Hà Nội")

a16 = "Hà Nội"
link(a16, "Hà Nam")
link(a16, "Hưng Yên")
link(a16, "Bắc Ninh")

a17 = "Bắc Ninh"
link(a17, "Hưng Yên")
link(a17, "Hải Dương")

a18 = "Hải Dương"
link(a18, "Hưng Yên")
link(a18, "Thái Bình")
link(a18, "Hải Phòng")

a19 = "Hải Phòng"
link(a19, "Thái Bình")

a20 = "Hà Nam"
link(a20, "Ninh Bình")
link(a20, "Nam Định")
link(a20, "Thái Bình")

a21 = "Thái Bình"
link(a21, "Nam Định")

a22 = "Thanh Hóa"
link(a22, "Ninh Bình")
link(a22, "Nghệ An")

a23 = "Ninh Bình"
link(a23, "Nam Định")

a24 = "Nghệ An"
link(a24, "Hà Tĩnh")

a = "Hà Tĩnh"
link(a, "Quảng Bình")

a = "Quản Bình"
link(a, "Quảng Trị")

a = "Quảng Trị"
link(a, "Thừa Thiên Huế")

a = "Thừa Thiên Huế"
link(a, "Đà Nẵng")
link(a, "Quảng Nam")

a = "Đà Nẵng"
link(a, "Quảng Nam")

a = "Quảng Nam"
link(a, "Quảng Ngãi")
link(a, "Kon Tum")

a = "Kon Tum"
link(a, "Gia Lai")
link(a, "Quảng Ngãi")

a = "Quảng Ngãi"
link(a, "Gia Lai")
link(a, "Bình Định")

a = "Gia Lai"
link(a, "Bình Định")
link(a, "Phú Yên")
link(a, "Đăk Lăk")

a = "Bình Định"
link(a, "Phú Yên")

a = "Phú Yên"
link(a, "Đăk Lăk")
link(a, "Khánh Hòa")

a = "Đăk Lăk"
link(a, "Khánh Hòa")
link(a, "Đăk Nông")
link(a, "Lâm Đồng")

a = "Khánh Hòa"
link(a, "Lâm Đồng")
link(a, "Ninh Thuận")

a = "Đăk Nông"
link(a, "Bình Phước")
link(a, "Lâm Đồng")

a = "Lâm Đồng"
link(a, "Bình Phước")
link(a, "Đồng Nai")
link(a, "Bình Thuận")
link(a, "Ninh Thuận")

a = "Ninh Thuận"
link(a, "Bình Thuận")

a = "Bình Phước"
link(a, "Tây Ninh")
link(a, "Bình Dương")
link(a, "Đồng Nai")

a = "Tây Ninh"
link(a, "TP. Hồ Chí Minh")
link(a, "Bình Dương")
link(a, "Long An")

a = "Bình Dương"
link(a, "TP. Hồ Chí Minh")
link(a, "Đồng Nai")

a = "Đồng Nai"
link(a, "TP. Hồ Chí Minh")
link(a, "Bà Rịa -Vũng Tàu")
link(a, "Bình Thuận")

a = "Bình Thuận"
link(a, "Bà Rịa -Vũng Tàu")

a = "Long An"
link(a, "TP. Hồ Chí Minh")
link(a, "Đồng Tháp")
link(a, "Tiền Giang")

a = "TP. Hồ Chí Minh"
link(a, "Tiền Giang")
link(a, "Bà Rịa -Vũng Tàu")

a = "Long An"
link(a, "TP. Hồ Chí Minh")
link(a, "Đồng Tháp")
link(a, "Tiền Giang")

a = "An Giang"
link(a, "Kien Giang")
link(a, "Đồng Tháp")
link(a, "Cần Thơn")

a = "Đồng Tháp"
link(a, "Cần Thơn")
link(a, "Vĩnh Long")
link(a, "Tiền Giang")

a = "Tiền Giang"
link(a, "Vĩnh Long")
link(a, "Bến Tre")
link(a, "Tiền Giang")

a = "Kien Giang"
link(a, "Cần Thơn")
link(a, "Bạc Liêu")
link(a, "Hậu Giang")
link(a, "Cà Mau")

a = "Cần Thơn"
link(a, "Hậu Giang")
link(a, "Vĩnh Long")

a = "Vĩnh Long"
link(a, "Hậu Giang")
link(a, "Sóc Trăng")
link(a, "Trà Vinh")
link(a, "Bến Tre")

a = "Bến Tre"
link(a, "Trà Vinh")

a = "Hậu Giang"
link(a, "Bạc Liêu")
link(a, "Sóc Trăng")
link(a, "Tiền Giang")

a = "Sóc Trăng"
link(a, "Bạc Liêu")
link(a, "Trà Vinh")

a = "Bạc Liêu"
link(a, "Cà Mau")

f = open("VNProvinceBorderLinking.txt", "w", encoding = "utf-8")
f.write(str(VN))
f.close()

json = json.dumps(VN)
f = open("VNProvinceBorderLinking.json","w")
f.write(json)
f.close()


print(VN)
#print(list.index("Thái Bình"))
#print(list[52])

