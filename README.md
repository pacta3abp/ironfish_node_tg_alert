# ironfish_node_tg_alert

to install tg alerts on your node:

git clone https://github.com/pacta3abp/ironfish_node_tg_alert.git

specify the api-key of your telegram bot and chat_id where you want to receive notifications in the synccheck.py file


and create service:


echo "
[Unit]
Description=sync_check
After=multi-user.target
[Service]
User=root
Group=root
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /root/ironfish_node_tg_alert/synccheck.py
RestartSec=3600
[Install]
WantedBy=multi-user.target" >> /etc/systemd/system/synccheck.service  && sudo systemctl daemon-reload && sudo systemctl enable synccheck.service && sudo systemctl start synccheck.service
