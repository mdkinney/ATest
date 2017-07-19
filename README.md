# EDK II Project

A modern, feature-rich, cross-platform firmware development environment
for the UEFI and PI specifications from www.uefi.org.

Contributions to the EDK II open source project are covered by the 
[TianoCore Contribution Agreement 1.1](Contributions.txt)

The majority of the content in the EDK II is open source project uses
a [BSD license](LICENSE).  The the EDK II open source project components
covered by additional licenses are as follows:
* [AppPkg\Applications\Python\Python-2.7.2\Tools\pybench](AppPkg\Applications\Python\Python-2.7.2\Tools\pybench\LICENSE)
* [AppPkg\Applications\Python\Python-2.7.2](AppPkg\Applications\Python\Python-2.7.2\LICENSE)
* [AppPkg\Applications\Python\Python-2.7.10](AppPkg\Applications\Python\Python-2.7.10\LICENSE)
* [BaseTools\Source\C\BrotliCompress](BaseTools\Source\C\BrotliCompress\LICENSE)
* [MdeModulePkg\Library\BrotliCustomDecompressLib](MdeModulePkg\Library\BrotliCustomDecompressLib\LICENSE)
* [OvmfPkg/Include/IndustryStandard/Xen](OvmfPkg/License.txt)
* [OvmfPkg/XenBusDxe](OvmfPkg/License.txt)
* [OvmfPkg/XenPvBlkDxe](OvmfPkg/License.txt)
* [CryptoPkg\Library\OpensslLib\openssl](CryptoPkg\Library\OpensslLib\openssl\LICENSE)

# Resources
* [EDK II](https://github.com/tianocore/tianocore.github.io/wiki/EDK-II)
* [Mailing Lists](https://github.com/tianocore/tianocore.github.io/wiki/Mailing-Lists)
* [How To Contribute](https://github.com/tianocore/tianocore.github.io/wiki/How-To-Contribute)
* [TianoCore Bugzilla](https://bugzilla.tianocore.org/)

# Change Description / Commit Message / Patch Email

Your change description should use the standard format for a
commit message, and must include your `Signed-off-by` signature
and the `Contributed-under` message.

## Sample Change Description / Commit Message

```
From: Contributor Name <contributor@example.com>
Subject: [PATCH] CodeModule: Brief-single-line-summary

Full-commit-message

Contributed-under: TianoCore Contribution Agreement 1.0
Signed-off-by: Contributor Name <contributor@example.com>
---

An extra message for the patch email which will not be considered part
of the commit message can be added here.

Patch content inline or attached
```

## Notes for sample patch email

* The first line of commit message is taken from the email's subject
  line following `[PATCH]`. The remaining portion of the commit message
  is the email's content until the `---` line.
* git format-patch is one way to create this format

## Definitions for sample patch email

* **`CodeModule`** - a short idenfier for the affected code.  For
  example `MdePkg`, or `MdeModulePkg/UsbBusDxe`.
* **`Brief-single-line-summary`** - a short summary of the change.
  The entire first line should be less than ~70 characters.
* **`Full-commit-message`** - a verbose multiple line comment describing
  the change.  Each line should be less than ~70 characters.
* **`Contributed-under`** - explicitely states that the contribution is
  made under the terms of the contribtion agreement.  This
  agreement is included below in this document.
* **`Signed-off-by`** - the contributor's signature identifying them
  by their real/legal name and their email address.
