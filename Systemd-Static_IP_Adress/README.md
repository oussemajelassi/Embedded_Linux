### Systemd Static IP Adress

When our image will not use systemd and not sysvinit the file /etc/network/interface will be useless to set a static ip adress.
Instead we should add the file above to **/etc/systemd/network** to get the job done. 
