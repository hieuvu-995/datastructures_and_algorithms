Data Structures and Algorithms in Python

                                    I. Cấu trúc dữ liệu
Cách lưu trữ, tổ chức dữ liệu có hệ thống để dữ liệu được sử dụng hiệu quả
2 nền tảng tạo nên cấu trúc dữ liệu:
-Interface: biểu diễn 1 tập hợp các phép tính mà cấu trúc dữ liệu hỗ trợ. 1 Interface cung cấp danh sách các phép tính, các loại tham số và kiểu dữ liệu trả về.
-Implementation: biểu diễn nội bộ của 1 cấu trúc dữ liệu. Cung cấp định nghĩa phần giải thuật được sử dụng trong các phép tính của dữ liệu. 

* Đặc điểm của cấu trúc dữ liệu:
+) Chính xác: Triển khai Interface 1 cách chính xác
+) Độ phức tạp về thời gian: Runtime là nhỏ nhất có thể
+) Độ phức tạp về bộ nhớ: Bộ nhớ sử dụng phải nhỏ nahast có thể

* Tại sao cấu trúc dữ liệu là cần thiết:
+) Tìm kiếm dữ liệu: Giả sử tìm kiếm 1 item từ 1 triệu item. Khi số lượng item gia tăng -> việc tìm kiếm trở nên chậm và tốn kém hơn
+) Tốc độ của vi xử lý: Mặc dù vi xử lý có tốc độ rất nhanh nhưng khi số lượng bản ghi lên đến hàng tỉ bản gì -> Tốc độ xử lý không còn nhanh nữa.
+) Đa yêu cầu: hàng nghìn người truy cập cùng thực hiện 1 phép tìm kiếm -> hàng tỉ phép tính được thực hiện trên server
=> Cấu trúc dữ liệu là 1 giải pháp thiết yếu.

* Độ phức tạp thời gian thực thi cấu trúc dữ liệu và giải thuật
+ Trường hợp xấu nhất: là tình hướng mà phép tính của cấu trúc dữ liệu tốn thời gian tối đa để thực hiện. Vd: Sx 1, 2, 3 theo thứ tự tăng dần -> thời gian thực hiển ngắn nhất. Sx 1, 2, 3 theo thứ tự giảm dần -> thời gian thực hiện dài nhất (worst case)
+ Trường hợp trung bình: thời gian thực thi trung bình của 1 phép tính
+ Trường hợp tốt nhất: thời gian thực thi ngắn nhất.

* Thuật ngữ cơ bản:
+ Dữ liệu: Là các giá trị hoặc tập hợp các giá trị
+ Phần tử dữ liệu: 1 đơn vị đơn lẻ của dữ liệu
+ Các phần tử nhóm: phần tử dữ liệu được chia thành các phần tử con
+ Phần tử cơ bản: phần tử không thể bị chia nhỏ
+ Thuộc tính và thực thể: thực thể là cái chưa 1 vài thuộc tính nào đó và các thuộc tính này có thể gắn giá trị
+ Tập hợp thực thể: tập hợp các thực thể có thuộc tính tương tự
+ Trường: đơn vị thông tin cơ bản biểu diễn 1 thuộc tính
+ Bản ghi: tập hợp các giá trị trường của 1 thực thể
+ File: tập hợp các bản ghi của các thực thể

-----

                                    II. Giải thuật
Giải thuật(thuật toán) là 1 tập hợp hữu hạn các chỉ thị được thực thi theo 1 thứ tự nào đó để đạt được kết quả mong muốn. Giải thuật có thể được triển khai trong nhiều ngôn ngữ lập trình khác nhau.
+ Giải thuật tìm kiếm: Tìm kiếm 1 phần tử trong dữ liệu. 
+ Giải thuật sắp xếp: Sắp xếp các phần tử theo 1 thứ tự nào đó.
+ Giải thuật chèn: chèn phần tử vào 1 cấu trúc dữ liệu.
+ Giải thuật cập nhập: Update phần tử đã tồn tại.
+ Giải thuật xóa: Xóa 1 phần tử đang tồn tại.

- Đặc điểm giải thuật
+ Tính xác định: nên rõ ràng và không mơ hồ
+ Dữ liệu đầu vào xác định: nên có 0 hoặc nhiều hơn dữ liệu đầu vào
+ Kết quả đầu ra: nên có 1 or nhiều hơn
+ Tính dừng: các giải thuật phải kết thúc sau 1 số hữu hạn các bước
+ Tính hiệu quả
+ Tính phổ biến
+ Độc lập: 1 giải thuật nên có chỉ thị độc lập vs bất kỳ phần code lập trình nào

- Phân tích giải thuật
Phân tích hiệu quả dựa trên 2 góc độ:
trước và sau khi triển khai.
+) Phân tích lý thuyết: chỉ dựa trên lý thuyết. Hiệu quả được đánh giá bằng giả sử các yếu tố khác là hằng số và không ảnh hưởng tới triển khai giải thuật.
+) Phân tích tiệm cận: tiến hành sau khi triển khai trên 1 ngôn ngữ nào đó. Sau khi chạy và kiểm tra đo lường các thông số liên quan thì hiệu quả của giải thuật dựa trên thông số như thời gian chạy, thời gian thực thi, bộ nhớ cần dùng.

* Độ phức tạp của giải thuật
Là 1 hàm ước lượng số phép tình mà giải thuật cần thực hiện có kích thước n
+ Nhân tố thời gian
+ Nhân tố bộ nhớ

* Độ phức tạp bộ nhớ: lượng bộ nhớ mà giải thuật cần dùng trong vòng đời của giải thuật. Lượng bố nhớ mà 1 giải thuật cần sử dụng là tổng 2 thành phần:
+ thành phần cố định: lượng bộ nhớ lưu giữ dự liệu và các biến
+ thành phần biến đổi: lượng bộ nhớ của các biến, có kích cỡ phụ thuộc vào kích cỡ của vấn đề

* Độ phức tạp của thời gian: lượng thời gian cần thiết từ khi bắt đầu -> kết thúc. Biểu diễn bời hàm T(n).
T(n) = c *n, trong đó: n là số bước, c: thời gian thực hiện 1 bước.
