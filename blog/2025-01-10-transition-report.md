# Transition Report

**Date:** 2024-12-19 
**Author:** Hendrik Ebbers (@hendrikEbbers)

This report gives detailed information on the state of the transition for each repository.

For the DCO report we assume that always the "committer" of a commit is the person that has to sign the DCO.

## hiero-sdk-go (https://github.com/hiero-ledger/hiero-sdk-go)

Repository has been transferred to Hiero.

## hedera-sdk-swift (https://github.com/hashgraph/hedera-sdk-swift)

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

### DCO checks

The repository does not have an invalid commit.

## hiero-sdk-tck (https://github.com/hiero-ledger/hiero-sdk-tck)

Repository has been transferred to Hiero.

## hedera-sdk-js (https://github.com/hashgraph/hedera-sdk-js)

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| Python-2.0         | :white_check_mark: |
| Unlicense          | :white_check_mark: |

### DCO checks

The repository does not have an invalid commit.

## hiero-sdk-cpp (https://github.com/hiero-ledger/hiero-sdk-cpp)

Repository has been transferred to Hiero.

## hedera-sdk-java (https://github.com/hashgraph/hedera-sdk-java)

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| Apache-2.0         | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| EPL-1.0            | :white_check_mark: |
| EPL-2.0            | :white_check_mark: |
| MIT                | :white_check_mark: |

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-sdk-java/commit/920f26b1aafc095fa730b71726498ce9a75e702b
- https://github.com/hashgraph/hedera-sdk-java/commit/4dd7bdc6b557ec861093b9b641d8f83a90d0f211
- https://github.com/hashgraph/hedera-sdk-java/commit/cac9ee641a5554e9f4e0b53fed45cb812ab98b65
- https://github.com/hashgraph/hedera-sdk-java/commit/030606bd993dd976b3c3c62e820be469bcdfce8c
- https://github.com/hashgraph/hedera-sdk-java/commit/4c3cef0b1880082d22cbd097cf276b09f563f663
- https://github.com/hashgraph/hedera-sdk-java/commit/655814cb878197a3e6c631078250765438ff2d48
- https://github.com/hashgraph/hedera-sdk-java/commit/bb2c02721af35e6d8277576cddb8e88b914573e9

## hedera-sdk-rust (https://github.com/hashgraph/hedera-sdk-rust)

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

### DCO checks

The repository does not have an invalid commit.

## solo (https://github.com/hashgraph/solo)

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

### DCO checks

The repository does not have an invalid commit.

## hedera-local-node (https://github.com/hashgraph/hedera-local-node)

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

### DCO checks

The repository does not have an invalid commit.

## hedera-json-rpc-relay (https://github.com/hashgraph/hedera-json-rpc-relay)

- license check is still in progress

### DCO checks

The repository does not have an invalid commit.

## hedera-mirror-node (https://github.com/hashgraph/hedera-mirror-node)

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

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-mirror-node/commit/1f33e3674d828cce246311d483ca394acf126202
- https://github.com/hashgraph/hedera-mirror-node/commit/d0966cef937271e00222b46d946b980419f943d3
- https://github.com/hashgraph/hedera-mirror-node/commit/fd8d4145116271899c2f89eafe76961883427cdc
- https://github.com/hashgraph/hedera-mirror-node/commit/97924de1b075fac1625c8220086871107631dcef
- https://github.com/hashgraph/hedera-mirror-node/commit/ce47668da9b94487bee1d4c796af67998fc405f8
- https://github.com/hashgraph/hedera-mirror-node/commit/c478a8f1a8d2eb043e1992ac6cb4d1d2c31960fa
- https://github.com/hashgraph/hedera-mirror-node/commit/39024decf56a230714680303df34168ffa0eefcc
- https://github.com/hashgraph/hedera-mirror-node/commit/c6880dfba04e10c7dba620b2f6f3320e8f4bafc3
- https://github.com/hashgraph/hedera-mirror-node/commit/cd05397d37581d91de16a9ffcffb9d6b39785ec8
- https://github.com/hashgraph/hedera-mirror-node/commit/e869f02e23c0ccc2cf39cc037109fb1c9dadb938
- https://github.com/hashgraph/hedera-mirror-node/commit/a7692778f6d6b48c2eb9c778ac39e5e9b6c84413

## hedera-mirror-node-explorer (https://github.com/hashgraph/hedera-mirror-node-explorer)

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

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-mirror-node-explorer/commit/e55caa1507cbb0ce9670021b70d4d42d2ce035c1

## hedera-block-node (https://github.com/hashgraph/hedera-block-node)

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

### DCO checks

The repository does not have an invalid commit.

## hedera-services (https://github.com/hashgraph/hedera-services)

- Need to contact Jendrik for automatic license check+

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-services/commit/26967885ce7b3e071773e062b01e857b971ddae4

## hedera-docs (https://github.com/hashgraph/hedera-docs)

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-docs/commit/83458d307d55c7e3132cac178c598e4e11a79247
- https://github.com/hashgraph/hedera-docs/commit/778842cef5180c7646ea111c8ab1dbc1b376c4af
- https://github.com/hashgraph/hedera-docs/commit/41cf46bc0018b5c029dc29d2f4142dc4d78b8456
- https://github.com/hashgraph/hedera-docs/commit/26aea17c0304c34a830b6fc55fc928118a481eed
- https://github.com/hashgraph/hedera-docs/commit/844415e2a9d05370f712c6a34a73ea07cb8eb856

## did-method (https://github.com/hashgraph/did-method)

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/did-method/commit/88043434cbf950e8e2b94d51b5010f2c284f74df
- https://github.com/hashgraph/did-method/commit/d1adb1f21168793640002d09d2ee9c7fb5cbe6a4
- https://github.com/hashgraph/did-method/commit/8359c77230a34aab82a6e07ce99e1da4d5223517
- https://github.com/hashgraph/did-method/commit/4c2a45f3f353a5fc3ab93c250d1c6d2447dbe319
- https://github.com/hashgraph/did-method/commit/74df3c99186b883cc0a40299135589231493445d
- https://github.com/hashgraph/did-method/commit/d2a06383049c86bd304e6f6d006add41f6fe0ac9
- https://github.com/hashgraph/did-method/commit/1ddd306090c1cde899e19e88d747b9b988809d0a
- https://github.com/hashgraph/did-method/commit/a815f7bc5ba12fe4bb77d155c34c9261ee5789d1
- https://github.com/hashgraph/did-method/commit/770e1945a7bff83820e4205308d639cd8bbea6a3
- https://github.com/hashgraph/did-method/commit/abda6f3400e8cffe66a2c09bbf9c39377134cc3c
- https://github.com/hashgraph/did-method/commit/0648ded39446a9f75695d5f93178ffe5df94b54a
- https://github.com/hashgraph/did-method/commit/11615ca76ffbc3ba6de2b28c5ac3de634998660a
- https://github.com/hashgraph/did-method/commit/6600f7a5c686aa762e9408aac2e554697f468b16
- https://github.com/hashgraph/did-method/commit/c7461e317fcae59e92d02631063cc7675007667b
- https://github.com/hashgraph/did-method/commit/41784b0a34511d8e748a8eb7faa1a27dccfb1884
- https://github.com/hashgraph/did-method/commit/3a31a1ae91fb640dbc7ce851903f39c6d91e942a
- https://github.com/hashgraph/did-method/commit/4cc2a3b54b78ac0264fc39195e6076deb9f4ddf6

## did-sdk-js (https://github.com/hashgraph/did-sdk-js)

### License checks

| License (SPDX)     | state |
| ------------------ | ----- |
| 0BSD               | :white_check_mark: |
| Apache-2.0         | :white_check_mark: |
| BSD-3-Clause       | :white_check_mark: |
| ISC                | :white_check_mark: |
| MIT                | :white_check_mark: |
| Unlicense          | :white_check_mark: |

### DCO checks

The repository does not have an invalid commit.

## did-sdk-java (https://github.com/hashgraph/did-sdk-java)

- license check is still in progress

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/did-sdk-java/commit/f0f3072467d8c8cd7d39fea69eb62dacb25df554
- https://github.com/hashgraph/did-sdk-java/commit/9eeb4bc8771fbbadf9b35ccfae6e5ff0dd5f1b0c
- https://github.com/hashgraph/did-sdk-java/commit/0d9fca678f3773de0d09e95da5f7ae3220e35ada
- https://github.com/hashgraph/did-sdk-java/commit/1c9d57f508365b50870dff92799fcbab7eb397df
- https://github.com/hashgraph/did-sdk-java/commit/98111a9a6af825257a62c1393fef8f644c53a97e
- https://github.com/hashgraph/did-sdk-java/commit/2207da4b37e0e9ffd98b677bd96d41c8cddf4041
- https://github.com/hashgraph/did-sdk-java/commit/e9145a70ecfb3540503773c41d428e14c2626a62
- https://github.com/hashgraph/did-sdk-java/commit/1d5db7d7ff39b25fee967ea13bcaaac676884877
- https://github.com/hashgraph/did-sdk-java/commit/a2f072d250b1f0e6f975039191d4750a22b5ad23
- https://github.com/hashgraph/did-sdk-java/commit/4287c80eed00b0f8fce08b0dcc4e3372732e40ce
- https://github.com/hashgraph/did-sdk-java/commit/9e10e3c6b017840da7ebc8a392dd1b7b7285936d
- https://github.com/hashgraph/did-sdk-java/commit/69b1aff04654e4aa20bc5ee6fd747b3abef2ae6b
- https://github.com/hashgraph/did-sdk-java/commit/2d547b7342f7f4d02d0a9616023b1201bb1c86c3
- https://github.com/hashgraph/did-sdk-java/commit/8c02c9c513ff2fcebada816674e6df39e4cfc0a2
- https://github.com/hashgraph/did-sdk-java/commit/3c8ddd1d95cb13e9e773ef2ea4aacc73952cd192
- https://github.com/hashgraph/did-sdk-java/commit/57788165dc7cd9e57f0a888ca91bd1221db1d021

## hedera-protobufs (https://github.com/hashgraph/hedera-protobufs)

### DCO checks

The repository does not have an invalid commit.

## hedera-improvement-proposal (https://github.com/hashgraph/hedera-improvement-proposal)

- license check is still in progress

### DCO checks

The repository contains the following invalid commits:

- https://github.com/hashgraph/hedera-improvement-proposal/commit/a4b28bfbd22d31e93d7df87ee88993db760029ae
- https://github.com/hashgraph/hedera-improvement-proposal/commit/bcd3afcd512b79011be7a1864194ed0a9fb8b2c2
- https://github.com/hashgraph/hedera-improvement-proposal/commit/9524f2162aa80959c60444437cef13018457d817
- https://github.com/hashgraph/hedera-improvement-proposal/commit/505d54548f90fdc76f170e91364fa2b4efd8c102
- https://github.com/hashgraph/hedera-improvement-proposal/commit/1e3d59df789771993eb02f3d0930fd1d112aef2e
- https://github.com/hashgraph/hedera-improvement-proposal/commit/8a295e6d11b235afd581eb30d5a597df6641912f
- https://github.com/hashgraph/hedera-improvement-proposal/commit/aa549bd7cf52079ebc728a3c6b75cb814bbf1582
- https://github.com/hashgraph/hedera-improvement-proposal/commit/6f0c20464c6f7bd95fd94e49f6d384fb3099d24b
