from tree import Tree

if __name__ == "__main__":

    test = """
parsec-service v1.0.0 (/home/ubuntu/parsec)
├── anyhow v1.0.56
├── base64 v0.13.0
├── bincode v1.3.3
│   └── serde v1.0.136
│       └── serde_derive v1.0.136 (proc-macro)
│           ├── proc-macro2 v1.0.36
│           │   └── unicode-xid v0.2.2
│           ├── quote v1.0.15
│           │   └── proc-macro2 v1.0.36 (*)
│           └── syn v1.0.88
│               ├── proc-macro2 v1.0.36 (*)
│               ├── quote v1.0.15 (*)
│               └── unicode-xid v0.2.2
├── derivative v2.2.0 (proc-macro)
│   ├── proc-macro2 v1.0.36 (*)
│   ├── quote v1.0.15 (*)
│   └── syn v1.0.88 (*)
├── env_logger v0.8.4
│   ├── atty v0.2.14
│   │   └── libc v0.2.120
│   ├── humantime v2.1.0
│   ├── log v0.4.14
│   │   ├── cfg-if v1.0.0
│   │   └── serde v1.0.136 (*)
│   ├── regex v1.5.5
│   │   ├── aho-corasick v0.7.18
│   │   │   └── memchr v2.4.1
│   │   ├── memchr v2.4.1
│   │   └── regex-syntax v0.6.25
│   └── termcolor v1.1.3
├── libc v0.2.120
├── log v0.4.14 (*)
├── num-traits v0.2.14
│   [build-dependencies]
│   └── autocfg v1.1.0
├── parsec-interface v0.26.0
│   ├── bincode v1.3.3 (*)
│   ├── derivative v2.2.0 (proc-macro) (*)
│   ├── log v0.4.14 (*)
│   ├── num v0.3.1
│   │   ├── num-bigint v0.3.3
│   │   │   ├── num-integer v0.1.44
│   │   │   │   └── num-traits v0.2.14 (*)
│   │   │   │   [build-dependencies]
│   │   │   │   └── autocfg v1.1.0
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   ├── num-complex v0.3.1
│   │   │   └── num-traits v0.2.14 (*)
│   │   ├── num-integer v0.1.44 (*)
│   │   ├── num-iter v0.1.42
│   │   │   ├── num-integer v0.1.44 (*)
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   ├── num-rational v0.3.2
│   │   │   ├── num-bigint v0.3.3 (*)
│   │   │   ├── num-integer v0.1.44 (*)
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   └── num-traits v0.2.14 (*)
│   ├── num-derive v0.3.3 (proc-macro)
│   │   ├── proc-macro2 v1.0.36 (*)
│   │   ├── quote v1.0.15 (*)
│   │   └── syn v1.0.88 (*)
│   ├── num-traits v0.2.14 (*)
│   ├── prost v0.8.0
│   │   ├── bytes v1.1.0
│   │   └── prost-derive v0.8.0 (proc-macro)
│   │       ├── anyhow v1.0.56
│   │       ├── itertools v0.10.3
│   │       │   └── either v1.6.1
│   │       ├── proc-macro2 v1.0.36 (*)
│   │       ├── quote v1.0.15 (*)
│   │       └── syn v1.0.88 (*)
│   ├── psa-crypto v0.9.1
│   │   ├── log v0.4.14 (*)
│   │   ├── psa-crypto-sys v0.9.2
│   │   │   [build-dependencies]
│   │   │   ├── cc v1.0.73
│   │   │   ├── cmake v0.1.45
│   │   │   │   └── cc v1.0.73
│   │   │   └── walkdir v2.3.2
│   │   │       └── same-file v1.0.6
│   │   ├── serde v1.0.136 (*)
│   │   └── zeroize v1.3.0
│   │       └── zeroize_derive v1.3.2 (proc-macro)
│   │           ├── proc-macro2 v1.0.36 (*)
│   │           ├── quote v1.0.15 (*)
│   │           ├── syn v1.0.88 (*)
│   │           └── synstructure v0.12.6
│   │               ├── proc-macro2 v1.0.36 (*)
│   │               ├── quote v1.0.15 (*)
│   │               ├── syn v1.0.88 (*)
│   │               └── unicode-xid v0.2.2
│   ├── secrecy v0.7.0
│   │   ├── serde v1.0.136 (*)
│   │   └── zeroize v1.3.0 (*)
│   ├── serde v1.0.136 (*)
│   ├── uuid v0.8.2
│   └── zeroize v1.3.0 (*)
├── rusqlite v0.26.3
│   ├── bitflags v1.3.2
│   ├── fallible-iterator v0.2.0
│   ├── fallible-streaming-iterator v0.1.9
│   ├── hashlink v0.7.0
│   │   └── hashbrown v0.11.2
│   │       └── ahash v0.7.6
│   │           ├── getrandom v0.2.5
│   │           │   ├── cfg-if v1.0.0
│   │           │   └── libc v0.2.120
│   │           └── once_cell v1.10.0
│   │           [build-dependencies]
│   │           └── version_check v0.9.4
│   ├── libsqlite3-sys v0.23.2
│   │   [build-dependencies]
│   │   ├── cc v1.0.73
│   │   ├── pkg-config v0.3.24
│   │   └── vcpkg v0.2.15
│   ├── memchr v2.4.1
│   └── smallvec v1.8.0
├── sd-notify v0.2.0
├── serde v1.0.136 (*)
├── signal-hook v0.3.13
│   ├── libc v0.2.120
│   └── signal-hook-registry v1.4.0
│       └── libc v0.2.120
├── structopt v0.3.26
│   ├── clap v2.34.0
│   │   ├── ansi_term v0.12.1
│   │   ├── atty v0.2.14 (*)
│   │   ├── bitflags v1.3.2
│   │   ├── strsim v0.8.0
│   │   ├── textwrap v0.11.0
│   │   │   └── unicode-width v0.1.9
│   │   ├── unicode-width v0.1.9
│   │   └── vec_map v0.8.2
│   ├── lazy_static v1.4.0
│   └── structopt-derive v0.4.18 (proc-macro)
│       ├── heck v0.3.3
│       │   └── unicode-segmentation v1.9.0
│       ├── proc-macro-error v1.0.4
│       │   ├── proc-macro-error-attr v1.0.4 (proc-macro)
│       │   │   ├── proc-macro2 v1.0.36 (*)
│       │   │   └── quote v1.0.15 (*)
│       │   │   [build-dependencies]
│       │   │   └── version_check v0.9.4
│       │   ├── proc-macro2 v1.0.36 (*)
│       │   ├── quote v1.0.15 (*)
│       │   └── syn v1.0.88 (*)
│       │   [build-dependencies]
│       │   └── version_check v0.9.4
│       ├── proc-macro2 v1.0.36 (*)
│       ├── quote v1.0.15 (*)
│       └── syn v1.0.88 (*)
├── threadpool v1.8.1
│   └── num_cpus v1.13.1
│       └── libc v0.2.120
├── toml v0.5.8
│   └── serde v1.0.136 (*)
├── users v0.11.0
│   ├── libc v0.2.120
│   └── log v0.4.14 (*)
├── uuid v0.8.2
├── version v3.0.0
└── zeroize v1.3.0 (*)
[dev-dependencies]
├── rand v0.8.5
│   ├── libc v0.2.120
│   ├── rand_chacha v0.3.1
│   │   ├── ppv-lite86 v0.2.16
│   │   └── rand_core v0.6.3
│   │       └── getrandom v0.2.5 (*)
│   └── rand_core v0.6.3 (*)
└── rust-cryptoauthlib v0.4.5
    ├── cryptoauthlib-sys v0.2.2
    │   [build-dependencies]
    │   └── cmake v0.1.45 (*)
    ├── lazy_static v1.4.0
    ├── log v0.4.14 (*)
    ├── rand v0.8.5 (*)
    └── strum_macros v0.21.1 (proc-macro)
        ├── heck v0.3.3 (*)
        ├── proc-macro2 v1.0.36 (*)
        ├── quote v1.0.15 (*)
        └── syn v1.0.88 (*)
"""

    test2 = """
parsec-service v1.0.0 (/home/ubuntu/parsec)
├── anyhow v0.0.56
├── base64 v0.13.0
├── bincode v1.3.3
│   └── serde v1.0.136
│       └── serde_derive v1.0.136 (proc-macro)
│           ├── proc-macro2 v1.0.36
│           │   └── unicode-xid v0.2.2
│           ├── quote v1.0.15
│           │   └── proc-macro2 v1.0.36 (*)
│           └── syn v1.0.88
│               ├── proc-macro2 v1.0.36 (*)
│               ├── quote v1.0.15 (*)
│               └── unicode-xid v0.2.2
├── derivative v2.2.0 (proc-macro)
│   ├── proc-macro2 v1.0.36 (*)
│   ├── quote v1.0.15 (*)
│   └── syn v1.0.88 (*)
├── env_logger v0.8.4
│   ├── atty v0.2.14
│   │   └── libc v0.2.120
│   ├── humantime v2.1.0
│   ├── log v0.4.14
│   │   ├── cfg-if v1.0.0
│   │   └── serde v1.0.136 (*)
│   ├── regex v1.5.5
│   │   ├── aho-corasick v0.7.18
│   │   │   └── memchr v2.4.1
│   │   ├── memchr v2.4.1
│   │   └── regex-syntax v0.6.25
│   └── termcolor v1.1.3
├── libc v0.2.120
├── log v0.4.14 (*)
├── num-traits v0.2.14
│   [build-dependencies]
│   └── autocfg v1.1.0
├── parsec-interface v0.26.0
│   ├── bincode v1.3.3 (*)
│   ├── derivative v2.2.0 (proc-macro) (*)
│   ├── log v0.4.14 (*)
│   ├── num v0.3.1
│   │   ├── num-bigint v0.3.3
│   │   │   ├── num-integer v0.1.44
│   │   │   │   └── num-traits v0.2.14 (*)
│   │   │   │   [build-dependencies]
│   │   │   │   └── autocfg v1.1.0
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   ├── num-complex v0.3.1
│   │   │   └── num-traits v0.2.14 (*)
│   │   ├── num-integer v0.1.44 (*)
│   │   ├── num-iter v0.1.42
│   │   │   ├── num-integer v0.1.44 (*)
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   ├── num-rational v0.3.2
│   │   │   ├── num-bigint v0.3.3 (*)
│   │   │   ├── num-integer v0.1.44 (*)
│   │   │   └── num-traits v0.2.14 (*)
│   │   │   [build-dependencies]
│   │   │   └── autocfg v1.1.0
│   │   └── num-traits v0.2.14 (*)
│   ├── num-derive v0.3.3 (proc-macro)
│   │   ├── proc-macro2 v1.0.36 (*)
│   │   ├── quote v1.0.15 (*)
│   │   └── syn v1.0.88 (*)
│   ├── num-traits v0.2.14 (*)
│   ├── prost v0.8.0
│   │   ├── bytes v1.1.0
│   │   └── prost-derive v0.8.0 (proc-macro)
│   │       ├── anyhow v1.0.56
│   │       ├── itertools v0.10.3
│   │       │   └── either v1.6.1
│   │       ├── proc-macro2 v1.0.36 (*)
│   │       ├── quote v1.0.15 (*)
│   │       └── syn v1.0.88 (*)
│   ├── psa-crypto v0.9.1
│   │   ├── log v0.4.14 (*)
│   │   ├── psa-crypto-sys v0.9.2
│   │   │   [build-dependencies]
│   │   │   ├── cc v1.0.73
│   │   │   ├── cmake v0.1.45
│   │   │   │   └── cc v1.0.73
│   │   │   └── walkdir v2.3.2
│   │   │       └── same-file v1.0.6
│   │   ├── serde v1.0.136 (*)
│   │   └── zeroize v1.3.0
│   │       └── zeroize_derive v1.3.2 (proc-macro)
│   │           ├── proc-macro2 v1.0.36 (*)
│   │           ├── quote v1.0.15 (*)
│   │           ├── syn v1.0.88 (*)
│   │           └── synstructure v0.12.6
│   │               ├── proc-macro2 v1.0.36 (*)
│   │               ├── quote v1.0.15 (*)
│   │               ├── syn v1.0.88 (*)
│   │               └── unicode-xid v0.2.2
│   ├── secrecy v0.7.0
│   │   ├── serde v1.0.136 (*)
│   │   └── zeroize v1.3.0 (*)
│   ├── serde v1.0.136 (*)
│   ├── uuid v0.8.2
│   └── zeroize v1.3.0 (*)
├── rusqlite v0.26.3
│   ├── bitflags v1.3.2
│   ├── fallible-iterator v0.2.0
│   ├── fallible-streaming-iterator v0.1.9
│   ├── hashlink v0.7.0
│   │   └── hashbrown v0.11.2
│   │       └── ahash v0.7.6
│   │           ├── getrandom v0.2.5
│   │           │   ├── cfg-if v1.0.0
│   │           │   └── libc v0.2.120
│   │           └── once_cell v1.10.0
│   │           [build-dependencies]
│   │           └── version_check v0.9.4
│   ├── libsqlite3-sys v0.23.2
│   │   [build-dependencies]
│   │   ├── cc v1.0.73
│   │   ├── pkg-config v0.3.24
│   │   └── vcpkg v0.2.15
│   ├── memchr v2.4.1
│   └── smallvec v1.8.0
├── sd-notify v0.2.0
├── serde v1.0.136 (*)
├── signal-hook v0.3.13
│   ├── libc v0.2.120
│   └── signal-hook-registry v1.4.0
│       └── libc v0.2.120
├── structopt v0.3.26
│   ├── clap v2.34.0
│   │   ├── ansi_term v0.12.1
│   │   ├── atty v0.2.14 (*)
│   │   ├── bitflags v1.3.2
│   │   ├── strsim v0.8.0
│   │   ├── textwrap v0.11.0
│   │   │   └── unicode-width v0.1.9
│   │   ├── unicode-width v0.1.9
│   │   └── vec_map v0.8.2
│   ├── lazy_static v1.4.0
│   └── structopt-derive v0.4.18 (proc-macro)
│       ├── heck v0.3.3
│       │   └── unicode-segmentation v1.9.0
│       ├── proc-macro-error v1.0.4
│       │   ├── proc-macro-error-attr v1.0.4 (proc-macro)
│       │   │   ├── proc-macro2 v1.0.36 (*)
│       │   │   └── quote v1.0.15 (*)
│       │   │   [build-dependencies]
│       │   │   └── version_check v0.9.4
│       │   ├── proc-macro2 v1.0.36 (*)
│       │   ├── quote v1.0.15 (*)
│       │   └── syn v1.0.88 (*)
│       │   [build-dependencies]
│       │   └── version_check v0.9.4
│       ├── proc-macro2 v1.0.36 (*)
│       ├── quote v1.0.15 (*)
│       └── syn v1.0.88 (*)
├── threadpool v1.8.1
│   └── num_cpus v1.13.1
│       └── libc v0.2.120
├── toml v0.5.8
│   └── serde v1.0.136 (*)
├── users v0.11.0
│   ├── libc v0.2.120
│   └── log v0.4.14 (*)
├── uuid v0.8.2
├── version v3.0.0
└── zeroize v1.3.0 (*)
[dev-dependencies]
├── rand v0.8.5
│   ├── libc v0.2.120
│   ├── rand_chacha v0.3.1
│   │   ├── ppv-lite86 v0.2.16
│   │   └── rand_core v0.6.3
│   │       └── getrandom v0.2.5 (*)
│   └── rand_core v0.6.3 (*)
└── rust-cryptoauthlib v0.4.5
    ├── cryptoauthlib-sys v0.2.2
    │   [build-dependencies]
    │   └── cmake v0.1.45 (*)
    ├── lazy_static v1.4.0
    ├── log v0.4.14 (*)
    ├── rand v0.8.5 (*)
    └── strum_macros v0.21.1 (proc-macro)
        ├── heck v0.3.3 (*)
        ├── proc-macro2 v1.0.36 (*)
        ├── quote v1.0.15 (*)
        └── syn v0.0.88 (*)
"""
    tree = Tree(test)
    tree2 = Tree(test2)
    hmap = {}
    tree.bfs_hash_it(hmap)
    print(hmap)
    print()
    newhmap = {}
    tree2.bfs_update(hmap, newhmap)
    #print(str(tree2))
    
    print(newhmap)
    #print(*tree.to_ascii(tree.root, -1))
