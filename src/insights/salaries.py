from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = max(
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdecimal()
    )

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = min(
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdecimal()
    )

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("Some key is missing")

    if (
        not str(job["min_salary"]).isdecimal()
        or not str(job["max_salary"]).isdecimal()
        or type(salary) not in [int, str]
    ):
        raise ValueError("Some value is not numeric")

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Min Salary is greater than Max Salary")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        finally:
            continue

    return jobs_by_salary_range
