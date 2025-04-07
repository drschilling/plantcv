from subprocess import call
from joblib import Parallel, delayed
import multiprocessing


# Process images using multiprocessing
###########################################
def _process_images_multiproc(job):
    """Process images using multiprocessing.
    Keyword arguments:
    job = workflow command-line components
    """
    call(job)

# Process jobs using Joblib instead of Dask
###########################################
def multiprocess(jobs):
    """Process jobs using joblib for parallel processing.

    Args:
        jobs: list of jobs (each is a list of CLI components)
        client: ignored, for API compatibility
    """
    num_workers = multiprocessing.cpu_count()
    Parallel(n_jobs=num_workers)(
        delayed(_process_images_multiproc)(job) for job in jobs
    )