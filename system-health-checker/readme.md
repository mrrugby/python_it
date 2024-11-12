# System Health Checker

A Python-based system monitoring tool that provides real-time insights into system performance metrics.

## Features

- Real-time CPU usage monitoring
- Memory utilization tracking
- Disk space analysis
- Network statistics monitoring
- Configurable alert thresholds
- Detailed logging capabilities

## Prerequisites

- Python 3.8+
- pipenv

## Installation

The tool uses `pipenv` for dependency management. To install:

1. Ensure you're in the system-health-checker directory:

```bash
cd system-health-checker
```

2. Install dependencies:

```bash
pipenv install
```

## Usage

1. Activate the virtual environment:

```bash
pipenv shell
```

2. Run the monitoring script:

```bash
python check_health.py
```

## Configuration

Default thresholds are set to:

- CPU: 80%
- Memory: 80%
- Disk: 80%

To modify these thresholds, edit the constants at the top of `check_health.py`:

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
```

## Output

The tool provides:

- Real-time console output of system metrics
- Warning messages when thresholds are exceeded
- Network I/O statistics

## Dependencies

- psutil: For system metrics collection
- Additional dependencies are listed in the Pipfile

## Troubleshooting

If you encounter permission errors:

1. Ensure you have appropriate system permissions
2. Run the script with elevated privileges if necessary
3. Check that all required dependencies are installed

## Contributing

Contributions to improve the tool are welcome. Please ensure to:

1. Follow the existing code style
2. Add comments for new functionality
3. Update documentation as needed
4. Test your changes thoroughly
