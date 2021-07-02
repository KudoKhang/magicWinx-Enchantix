# MagicWinx-Enchantix

Dùng một tấm vải đưa nó ra phía trước camera và bạn sẽ biến mất! 

<p align="center">
  <img src="https://baomoinhanh.com/wp-content/uploads/2016/01/ao-tang-hinh.jpg" />
   
</p>
<p align="center">
   <i>Magic is real 😳 </i>
</p>

# How it work

Ở đây... là Github và tấc nhiên là chúng ta không được dùng phép thuật rồi. Thay vào đó là kỹ thuật Image Segmentation bằng các hàm trong cv2

1. Đầu tiên chụp lại hình ảnh ban đầu (Lưu ý: giữ cho khung hình tĩnh trong 2s)

   ```python
   _, background = cap.read()
   time.sleep(2)
   _, background = cap.read()
   ```

2. Thực hiện segment vùng vải che (Vải che phải đồng nhất một màu nhé)

3. Ghép vùng vải đó với background được chụp ban đầu và giữ nguyên phần còn lại của cơ thể

# Installations

Để khởi chạy ứng dụng ta cần cài đặt thư viện sau :

```python
pip install numpy
pip install cv2
```

# Usage

Clone ứng dụng về máy và chạy bằng cách mở terminal:

```python
git clone https://github.com/KudoKhang/magicWinx-Enchantix
cd magicWinx-Enchantix
python app.py
```

