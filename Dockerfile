FROM robd003/python3.10
ENV PYTHONUNDUFFERED 1
WORKDIR /Develops_Test_Task
COPY requirements.txt ./
RUN pip3 install django-cors-headers
RUN pip3 install -r requirements.txt
COPY . /Develops_Test_Task/