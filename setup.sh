#/bin/sh

mkdir -p ~/.local/bin 
mkdir -p ~/.local/share/tskr/ 


cp ./main.py ~/.local/bin/tskr 
touch ~/.local/share/tskr/tskr_tasks


# Edit the py file to include current HOME path
sed -i "s+tskr_tasks+$HOME/.local/share/tskr/tskr_tasks+g" ~/.local/bin/tskr

