# Firefox-crawler

## Description
Docker Image for crawling Web Sites with Firefox & mitmproxy
It can use Firefox by GUI or headless mode.

## Requirement
Docker & docker-compose

Linux Desktop Environment (necessary only for GUI mode)

## Usage
Execute below and run firefox and mitmproxy.
When you want to Firefox as GUI, you need to allow authentication by X Window System from localhost.
Execute 'xhost +' or 'xhost local:'(I recommend to execute 'xhost -' or 'xhost -local:' when finished).
You have to edit docker-compose.yml and uncomment some lines.

```sh
docker-compose build
docker-compose up
```

If you want to use custom mitmproxy scripts, you make scripts/mitmproxy-script.py (example script is to save all html documents).
If you controle firefox via selenium, make scripts/crawling-script.sh and run python script from it (example script is to access Google site).
docker-entrypoint.sh will exec these scripts if there are files with the same name.

## Author
