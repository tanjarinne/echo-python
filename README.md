<h1 align="center">Echo</h1>

<div align="center">
    <i>Echo is a service that responds with any header or body you send over, as-is.</i>
</div>
<br>

## About

This project is intended to be educational, for-research-only and solving a fictional problem, and is not intended to work on any production environment whatsoever as it can potentially leak private information due to its most basic functionality.

## Requirements

* Python 3

### Configuration

| Configuration | Environmental variable | Purpose | Default |
|-|-|-|-|
| Echo host | `ECHO_HOST` | The host Echo will run on | `0.0.0.0` |
| Echo port | `ECHO_PORT` | The port Echo will listen to | `8018` |

### Running

A Makefile is provided to handle common operations – like running the service.

| Target | Description | Examples |
|-|-|-|
| `make run` | Run the service | <pre>$ make run<br>Listening on 0.0.0.0:8018<br></pre> |

## Authors

Cats & Foxes 2018
