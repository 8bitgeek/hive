# Project 'Hive'
```
______  ______             
___  / / /__(_)__   ______ 
__  /_/ /__  /__ | / /  _ \
_  __  / _  / __ |/ //  __/
/_/ /_/  /_/  _____/ \___/ 

```

* Contemporary Peer-to-Peer Social Engagement
* Secure private communications and transactions
* Robust social engagement, anti-censorship, open source
* Version 0.0 (Work in Process)

### Technology Preview

* Technical Preview Slides [docs/hive-slides.odp](https://github.com/8bitgeek/hive/blob/master/docs/hive-slides.odp?raw=true)
* Technical Specification [docs/techspec.md](docs/techspec.md)

### How do I get set up?

* Dependencies
  - Python 3
    - opendht
      - msgpack-c 1.3+, used for data serialization.
      - GnuTLS 3.3+, used for cryptographic operations.
      - Nettle 2.4+, a GnuTLS dependency for crypto.
      - Argon2, a dependency for key stretching.
      - Readline, an optional dependency for the DHT tools.
      - Cython, an optional dependency for the Python bindings.
    - p2pnetwork
    - ipfs-api
    - blowfish
* Summary of set up
  - `git clone https://github.com/8bitgeek/hive.git`
  - `cd hive`
  - `git submodule init`
  - `git submodule update`
    * OpenDHT
      - `cd src/lib/opendht`
      - `sudo apt install libncurses5-dev libreadline-dev nettle-dev libgnutls28-dev libargon2-0-dev libmsgpack-dev  libssl-dev libfmt-dev libjsoncpp-dev libhttp-parser-dev libasio-dev`
      - `sudo apt-get install cython3 python3-dev python3-setuptools`
      - `mkdir build && cd build`
      - `cmake -DOPENDHT_PYTHON=ON -DCMAKE_INSTALL_PREFIX=/usr ..`
      - `make -j4`
      - `sudo make install`
* Configuration
  - See [src/setup/README.md](src/setup/README.md)
* Database configuration
* How to run tests
  * See [src/test/README.md](src/test/README.md)
* Deployment instructions
  - Linux: `./install.sh`
  - Windows: N/A
  - Android: N/A

### Contribution guidelines

* Writing tests
* Code review
* Other guidelines

### Who do I talk to?

* Repo owner or admin
* Other community or team contact
