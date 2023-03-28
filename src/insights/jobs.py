from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        data = csv.DictReader(file)
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_job_types = {job["job_type"] for job in jobs}
    return list(unique_job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_type = [job for job in jobs if job["job_type"] == job_type]
    return job_type
