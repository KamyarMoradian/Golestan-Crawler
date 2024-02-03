import time
from threading import Thread

import config
from crawler_scripts.get_golestan_courses import get_golestan_courses


def get_one_semester(semester, display):
    get_golestan_courses(semester, display)


def get_past_10_semesters(display):
    semesters = config.PAST_10_SEMESTERS

    threads = []

    for semester in semesters:
        t = Thread(target=get_golestan_courses, args=(semester, display))
        t.start()
        threads.append(t)

    for i in range(len(semesters)):
        threads[i].join()


if __name__ == '__main__':
    tic = time.time()

    # # Uncomment the following line to get the courses of the past 10 semesters
    # get_past_10_semesters(display=False)
    # # Uncomment the following line to get the courses of a specific semester
    get_one_semester(config.SEMESTER, display=True)

    toc = time.time()
    print(toc - tic)
