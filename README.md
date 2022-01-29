# pylogix app

A very simple example of a mobile app using kivy and buildozer
I've only used buildozer on Linux, these instructions work for Ubuntu 20.04 (I use Kubuntu)

## Dependencies
- buildozer
- cython
- kivy
- pylogix

install python dependencies via pip:
```console
pip3 install -r requirements.txt
```

Install linux packages
```console
sudo apt install -y git zip unzip openjdk-13-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

## Building for Android
The first build will take some time as buildozer will likely need to download additional packages.  Your project will be in the bin directory
```console
buildozer -v android debug
```

Assuming that it successfully compiled, you can send it to your android phone.  You have to have USB debugging enabled on your phone first
```console
buildozer android deploy run
```

There are a couple of things to edit in the buildozer.spec file.
  *package.name will be the name of your app.  You can name it whatever you want
  *version is your app version number, you should change ths with each new apk compiled
  *orientation will change whether your app is portraite or landscape
