import streamlit as st
import requests

# Định nghĩa địa chỉ API của FastAPI
API_URL = "http://127.0.0.1:8001"

# Danh sách lưu trữ lịch sử cuộc trò chuyện
chat_history = []

# Tiêu đề của ứng dụng
st.title('Travel Bot')

# Khung nhập dữ liệu từ người dùng
user_input = st.text_area('Nhập câu hỏi của bạn về du lịch:', '')

# Nút gửi để gửi yêu cầu đến API
if st.button('Gửi'):
    # Gửi yêu cầu POST đến API FastAPI
    try:
        response = requests.post(f"{API_URL}/travel-rag", json={"text": user_input})
        if response.status_code == 200:
            try:
                data = response.text  # Lấy dữ liệu như là một chuỗi
                # Thêm tin nhắn vào lịch sử cuộc trò chuyện
                chat_history.append(f"You: {user_input}")
                chat_history.append(f"Bot: {data}")
                # Hiển thị lịch sử cuộc trò chuyện trên giao diện
                for message in chat_history[-5:]:  # Chỉ hiển thị 5 tin nhắn gần nhất
                    st.text(message)
            except ValueError:
                st.error("Dữ liệu trả về từ API không hợp lệ")
        else:
            st.error(f"Lỗi khi gửi yêu cầu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Lỗi kết nối đến API: {str(e)}")
