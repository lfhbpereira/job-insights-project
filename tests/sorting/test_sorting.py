from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    jobs = read("data/jobs.csv")

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "19857"

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "383416"

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-05-08"
