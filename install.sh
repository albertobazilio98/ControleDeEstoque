echo "Updating APT..."
sudo apt update -qq
echo "Installing MySQL-Server..."
sudo apt install mysql-server -qq
echo "Setting Security Configurations..."
sudo mysql_secure_installation

echo "Installing Python 3..."
sudo apt-get install python3.6 -qq
echo "Installing PIP..."
sudo apt-get install python3-pip -qq
echo "Installing Tkinter..."
sudo apt-get install python3-tk -qq
echo "Installing TKInterTable..."
sudo pip3 install tkintertable -qq
echo "Installing MySQL-Connector..."
sudo pip3 install mysql-connector -qq

sudo mysql -u root -p < db.sql
sudo mysql -u root -p 
