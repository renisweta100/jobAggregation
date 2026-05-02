from .job_api import job_api

def filter_job_funct(search):
    url= ""
    data = job_api()

    jobs = []

    for job in data:
        if search.lower() in [tag.lower() for tag in job.get("tags",[])]:

            jobs.append({"title": job.get("position"),"company":job.get("company")})

    return jobs