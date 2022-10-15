#/bin/bash

#клонирование
eval `ssh-agent`
ssh-add ~/github
git clone git@github.com:Ornstein89/VTB_API_hack2022.git
cd VTB_API_hack2022
git submodule init
git submodule update

# попытка установить .NET через  apt
sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt-get install python3-dev -y
sudo apt-get install python3-venv -y
sudo apt-get install redis -y
sudo apt-get install redis-server -y
sudo apt-get install nginx -y
sudo apt-get install dotnet6 -y


# если не срабатывает установка .NET через  apt
# wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
# sudo dpkg -i packages-microsoft-prod.deb
# rm packages-microsoft-prod.deb

# сборка фаззера
mkdir experiment/backend/restler-fuzzer/restler_bin
python3 experiment/backend/restler-fuzzer/build-restler.py --dest_dir experiment/backend/restler-fuzzer/restler_bin

# удалить собранный фаззер для пересборки
rm -r experiment/backend/restler-fuzzer/restler_bin

restler-fuzzer/restler_bin/restler/Restler compile --api_spec openapi8012.json

# В случае успеха - наличие файлов, а также сообщение "Task Compile succeeded" в стандартном выводе, а также файлы словаря, грамматики и settings

restler-fuzzer/restler_bin/restler/Restler fuzz-lean --grammar_file Compile/grammar.py --dictionary_file Compile/dict.json --settings Compile/engine_settings.json --no_ssl

# для WSL

sudo update-alternatives --config iptables

