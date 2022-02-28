FROM python:3.8

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD streamlit run app.py