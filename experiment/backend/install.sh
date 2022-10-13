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
sudo apt-get install -y dotnet6

# если не срабатывает установка .NET через  apt
# wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
# sudo dpkg -i packages-microsoft-prod.deb
# rm packages-microsoft-prod.deb

# сборка фаззера
mkdir experiment/backend/restler-fuzzer/restler_bin
python3 experiment/backend/restler-fuzzer/build-restler.py --dest_dir experiment/backend/restler-fuzzer/restler_bin