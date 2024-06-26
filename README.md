# Apache NiFi Python Extensions

[![license](https://img.shields.io/github/license/apache/nifi-python-extensions)](https://github.com/apache/nifi-python-extensions/blob/main/LICENSE)
[![build](https://github.com/apache/nifi-python-extensions/actions/workflows/build.yml/badge.svg)](https://github.com/apache/nifi-python-extensions/actions/workflows/build.yml)
[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

The [Apache NiFi](https://nifi.apache.org) Python Extensions repository contains Processors implemented in [Python](https://www.python.org/)
for deployment in Apache NiFi 2.

## Building

This project uses [Hatch](https://hatch.pypa.io) to build distribution packages.

```
hatch build
```

The build command creates a source distribution in the `dist` directory.

The source distribution contains an `extensions` directory can be copied into Apache NiFi to use the packaged Processors.

## Developing

The Apache NiFi [Python Developer's Guide](https://nifi.apache.org/documentation/nifi-2.0.0-M3/html/python-developer-guide.html)
provides the API and implementation guidelines for Python Processors.

The Hatch format command supports evaluating Python Processors against configured rules.

```
hatch fmt --check
```

## Documentation

The Apache NiFi [Documentation](https://nifi.apache.org/documentation/) includes reference information for project capabilities.

## Contributing

The Apache NiFi [Contributor Guide](https://cwiki.apache.org/confluence/display/NIFI/Contributor+Guide)
describes the process for getting involved in the development of this project.

## Issues

This project uses [Jira](https://issues.apache.org/jira/browse/NIFI) for tracking bugs and features.

## Licensing

This project is released under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
