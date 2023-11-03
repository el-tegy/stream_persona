# type: ignore[attr-defined]
"""stream_persona is a comprehensive data engineering solution designed to seamlessly capture, process, store, and analyze data streams. Leveraging state-of-the-art technologies such as Apache Kafka, Apache Airflow, Apache Spark, and Apache Cassandra, this architecture ensures efficient data flow and processing capabilities."""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
