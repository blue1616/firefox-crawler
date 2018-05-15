#!/bin/sh -l
set -eu

echo 'Starting MITMProxy...'
if [ -f /home/firefox/scripts/mitmproxy-script.py ]; then
  su - firefox -c 'nohup mitmdump -s /home/firefox/scripts/mitmproxy-script.py &'
else
  su - firefox -c 'nohup mitmdump &'
fi

su - firefox -c 'firefox --headless www.google.com'

openssl x509 -in /home/firefox/.mitmproxy/mitmproxy-ca-cert.pem -inform PEM -out /home/firefox/.mitmproxy/mitmproxy-ca-cert.crt
mkdir /usr/share/ca-certificates/extra
cp /home/firefox/.mitmproxy/mitmproxy-ca-cert.crt /usr/share/ca-certificates/extra/
echo 'extra/mitmproxy-ca-cert.crt' >> /etc/ca-certificates.conf 
update-ca-certificates

certfile="/home/firefox/.mitmproxy/mitmproxy-ca-cert.pem"
certname="mitmproxy"

for certDB in $(find /home/firefox/ -name "cert9.db")
do
  prefdir=$(dirname ${certDB});
  echo ${prefdir};
  exec_command='certutil -A -n '${certname}' -t "TCu,Cu,Tu" -i '${certfile}' -d sql:'${prefdir}
  su - firefox -c "${exec_command}"
  cp -f /home/firefox/prefs.js ${prefdir}
  chown firefox:firefox ${prefdir}
done

su - firefox -c 'geckodriver &'

echo 'Start Crawling!!'
if [ -f /home/firefox/scripts/crawling-script.sh ]; then
  su - firefox -c '/home/firefox/scripts/crawling-script.sh'
else
  su - firefox -c 'firefox'
fi
