# Transition Report

**Date:** 2024-12-19 
**Author:** Hendrik Ebbers (@hendrikEbbers)

This report gives detailed information on the state of the transition for each repository.

## hiero-sdk-go

Repository has been transferred to Hiero.

## hedera-sdk-swift

- The lib https://github.com/krzyzanowskim/CryptoSwift.git has an unknown license


### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| Unknown            | :red_circle: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |


## hiero-sdk-tck

Repository has been transferred to Hiero.

## hedera-sdk-js

- Execution of license checks is still in progress

## hiero-sdk-cpp

Repository has been transferred to Hiero.

## hedera-sdk-java

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| Apache-2.0         | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| EPL-1.0            | :white_check_mark: |
| EPL-2.0            | :white_check_mark: |
| MIT                | :white_check_mark: |

## hedera-sdk-rust

- Unknown license in dependency: https://github.com/briansmith/ring/blob/main/LICENSE
- Example for project under "Unicode 3.0" license: https://github.com/unicode-org/icu4x?tab=readme-ov-file

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-1-Clause       | ? |
| Unknown            | ? |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| MPL-2.0            | :white_check_mark: |
| Unicode-3.0        | ? |

## solo

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| BlueOak-1.0.0      | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| Python-2.0         | :white_check_mark: |
| Unlicense          | :white_check_mark: |

## hedera-local-node

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| BlueOak-1.0.0      | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| Python-2.0         | :white_check_mark: |
| Unlicense          | :white_check_mark: |

## hedera-json-rpc-relay

- license check is still in progress

## hedera-mirror-node

- The LGPL-2.1-only license is not needed at runtime and can be refactored
- Hibernate is licensed LGPL-2.1-or-later
- We depend on "Maven:org.tukaani:xz:1.9" that should be updated to 1.10 to be under BSD0. For the given verdsion no license is defined
- Problem at license check: invalid: send@0.19.1 /tmp/tmp.cO0My85xIU/hedera-mirror-node/hedera-mirror-rest/node_modules/swagger-stats/node_modules/send

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| BlueOak-1.0.0      | :white_check_mark: |
| CC0-1.0            | :red_circle: |
| CDDL-1.0           | :white_check_mark: |
| CDDL-1.1           | :white_check_mark: |
| EPL-1.0            | :white_check_mark: |
| EPL-2.0            | :white_check_mark: |
| ISC                | :white_check_mark: |
| LGPL-2.1-only      | :red_circle: |
| LGPL-2.1-or-later  | :red_circle: |
| Public Domain      | :white_check_mark: |
| MIT                | :white_check_mark: |
| MIT-0              | ? |
| MPL-2.0            | :white_check_mark: |
| Python-2.0         | :white_check_mark: |

## hedera-mirror-node-explorer

- The LGPL-3.0-only license is because of https://github.com/web3/web3.js?tab=readme-ov-file

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| CC-BY-4.0          | :white_check_mark: |
| ISC                | :white_check_mark: |
| LGPL-3.0-only      | :red_circle: |
| MIT                | :white_check_mark: |
| MPL-2.0            | :white_check_mark: |
| Unlicense          | :white_check_mark: |
| Zlib               | :white_check_mark: |

## hedera-block-node

- The "GPL-2.0-only WITH Classpath-exception-2.0" license is because of "Maven:com.google.errorprone:javac-shaded:9-dev-r4023-3"
- The "LGPL-2.1-only" license is because of "Maven:com.github.spotbugs:spotbugs-annotations:4.7.3" that is not needed at runtime

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| Apache-2.0         | :white_check_mark: |
| BSD-2-Clause       | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| CDDL-1.0           | :white_check_mark: |
| EPL-1.0            | :white_check_mark: |
| EPL-2.0            | :white_check_mark: |
| GPL-2.0-only WITH Classpath-exception-2.0 | ? |
| LGPL-2.1-only      | :red_circle: |
| MIT                | :white_check_mark: |
| MPL-2.0            | :white_check_mark: |

## hedera-services

- Need to contact Jendrik for automatic license check+

## hedera-docs

## did-method

## did-sdk-js

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| Unlicense          | :white_check_mark: |


## did-sdk-java

- license check is still in progress

## hedera-protobufs



## hedera-improvement-proposal

- license check is still in progress
