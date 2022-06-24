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
* Linux-only during early development phase

### Technology Preview

* Technical Preview Slides [docs/hive-slides.odp](https://github.com/8bitgeek/hive/blob/master/docs/hive-slides.odp?raw=true)
* Technical Specification [docs/techspec.md](docs/techspec.md)

### How do I get set up?

* Summary of set up
  - `git clone https://github.com/8bitgeek/hive.git`
  - `cd hive`
  - `git submodule init`
  - `git submodule update`
* Configuration
  - See [src/setup/README.md](src/setup/README.md)
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

