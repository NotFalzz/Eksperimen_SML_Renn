# Wajib pakai Python 3.12.7
FROM python:3.12.7-slim

# Set folder kerja di dalam container
WORKDIR /app

# Copy file requirements dulu biar caching efisien
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ekspos port Jupyter
EXPOSE 8888

# Perintah default saat container nyala: Jalankan Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
