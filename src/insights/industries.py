from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    unique_industries = {job["industry"] for job in jobs}
    unique_industries.discard("")
    return list(unique_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry = [job for job in jobs if job["industry"] == industry]
    return industry
