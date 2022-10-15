# pull the official base image
FROM mcr.microsoft.com/dotnet/sdk:6.0

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip
COPY ./fuzzer/backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./fuzzer/backend/ /app/

# RUN apt-get install dotnet6
# RUN mkdir /app/restler-fuzzer/restler_bin
RUN python3 /app/restler-fuzzer/build-restler.py --dest_dir /app/restler-fuzzer/restler_bin

EXPOSE 8016

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]