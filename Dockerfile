FROM python
RUN apt-get install g++
WORKDIR /var
COPY . .
CMD ["python", "main.py"]
