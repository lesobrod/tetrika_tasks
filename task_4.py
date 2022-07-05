import json


def appearance(intervals):
    # Вычисление времени одновременного присутствия
    lesson = intervals['lesson']
    lessons = range(lesson[0], lesson[1]+1)

    pupil = intervals['pupil']
    tutor = intervals['tutor']
    pupil_ranges = make_ranges(pupil)
    tutor_ranges = make_ranges(tutor)

    intervals_all = []
    check_data = []
    check_data += lesson
    check_data += pupil
    check_data += tutor

    for timestamp in check_data:
        if timestamp in lessons:
            tutor_check = is_in_range(timestamp, tutor_ranges)
            pupil_check = is_in_range(timestamp, pupil_ranges)
            if pupil_check and tutor_check:
                intervals_all.append(timestamp)
    intervals_all.sort()
    time = 0

    for i in range(1, len(intervals_all), 2):
        delta = intervals_all[i] - intervals_all[i-1]
        time += delta
    return time


def is_in_range(timestamp, ranges):
    # Проверка попадания в интервал
    return any([timestamp in timedelta
                for timedelta in ranges])


def make_ranges(intervals):
    # Генерация интервалов
    return [range(intervals[i-1], intervals[i]+1)
            for i in range(1, len(intervals), 2)]


if __name__ == "__main__":
    with open("tests.json", "r") as read_file:
        tests = json.load(read_file)

    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        if test_answer == test['answer']:
            print(f'Test case {i + 1} passed OK')
        else:
            print(f'Test case {i + 1} ERROR, got {test_answer}, expected {test["answer"]}')
