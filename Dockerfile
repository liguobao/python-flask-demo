FROM python:3.7
# RUN pip3 install pillow -i https://mirrors.aliyun.com/pypi/simple/
# RUN apt update && apt install -y libsm6 libxext6
# RUN apt-get -y install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
# RUN apt-get clean && apt-get autoremove
# RUN pip3 install pillow -i https://mirrors.aliyun.com/pypi/simple/
# RUN pip3 install tesserocr -i https://mirrors.aliyun.com/pypi/simple/




# set working directory
RUN mkdir -p /app
WORKDIR /app

# add requirements
COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# add entrypoint.sh
# COPY ./entrypoint.sh /app/entrypoint.sh

# add app
COPY . /app

# run server
# CMD ["./entrypoint.sh"]
EXPOSE 8000
ENV LC_ALL=C
ENTRYPOINT ["gunicorn", "-b", ":8000","-t","80", "-w", "4", "--access-logfile", "-","manage:app"]