FROM debian:latest

# Install Firefox
RUN apt-get update && apt-get install -y \
  wget bzip2 \
  libgtk-3-dev \
  libdbus-glib-1-2 \
  libxt6 \
  apt-transport-https \
  ca-certificates \
  gnupg \
  fonts-symbola \
  unzip \
  python3-dev \
  python3-pip \
  python3-setuptools \
  --no-install-recommends && \
  wget -O /tmp/firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=ja" && \
  tar -C /opt -xjf /tmp/firefox.tar.bz2 && \
  rm /tmp/firefox.tar.bz2 && \
  ln -fs /opt/firefox/firefox /usr/bin/firefox && \
  rm -rf /var/lib/apt/lists/*

# Install GeckoDriver
RUN GK_VERSION=$(wget -qO- "https://api.github.com/repos/mozilla/geckodriver/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([0-9.]+)".*/\1/') && \
  echo "Using GeckoDriver version: "$GK_VERSION && \
  wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GK_VERSION/geckodriver-v$GK_VERSION-linux64.tar.gz  && \
  rm -rf /opt/geckodriver && \
  tar -C /opt -zxf /tmp/geckodriver.tar.gz && \
  rm /tmp/geckodriver.tar.gz && \
  chmod 755 /opt/geckodriver && \
  ln -fs /opt/geckodriver /usr/bin/geckodriver

# Make user to run Firefox
RUN groupadd -r firefox && useradd -r -g firefox -G audio,video firefox && \
  usermod -u 1000 firefox && groupmod -g 1000 firefox && \
  mkdir -p /home/firefox/Downloads && \
  mkdir -p /home/firefox/output && \
  mkdir -p /home/firefox/scripts && \
  chsh -s /bin/bash firefox && \
  chown -R firefox:firefox /home/firefox

# Install selenium & mitmproxy
RUN pip3 install selenium
RUN pip3 install mitmproxy

# Setting Locale to Ja_JP.UTF-8
RUN apt-get update && apt-get install -y task-japanese \
  locales \
  locales-all \
  --no-install-recommends && \
  sed -i 's/^#\sja_JP.UTF-8\sUTF-8$/ja_JP.UTF-8 UTF-8/' /etc/locale.gen && \
  update-locale && \
  echo 'export LANG=ja_JP.UTF-8' >> /etc/profile && \
  rm -rf /var/lib/apt/lists/*

# Install noto, Japanese Font
RUN mkdir /tmp/japanesefont/ && \
  wget https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O /tmp/japanesefont/NotoSansCJKjp-hinted.zip && \
  unzip /tmp/japanesefont/NotoSansCJKjp-hinted.zip -d /tmp/japanesefont/ && \
  mkdir -p /usr/share/fonts/noto && \
  mv /tmp/japanesefont/*.otf /usr/share/fonts/noto && \
  chmod 644 -R /usr/share/fonts/noto/ && \
  fc-cache -fv && \
  rm -rf /tmp/japanesefont/

# Firefox user couldn't read Fonts in /usr/share/fonts. I don't know why...
RUN mkdir -p /home/firefox/.fonts && \
  cp -p /usr/share/fonts/noto/* /home/firefox/.fonts/ && \
  chown firefox:firefox /home/firefox/.fonts/

RUN apt-get update && apt-get install -y libnss3-tools \
  --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*

# Run script. Switching user in this.
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

COPY prefs.js /home/firefox/prefs.js

ENTRYPOINT ["docker-entrypoint.sh"]
#CMD ["/bin/bash"]
