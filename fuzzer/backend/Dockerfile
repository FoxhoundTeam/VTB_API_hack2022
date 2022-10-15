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
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app/

# RUN apt-get install dotnet6
# RUN mkdir /app/restler-fuzzer/restler_bin
RUN python3 /app/restler-fuzzer/build-restler.py --dest_dir /app/restler-fuzzer/restler_bin
RUN python3 manage.py makemigrations
RUN python3 manage.py makemigrations fuzzing
RUN python3 manage.py migrate

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]