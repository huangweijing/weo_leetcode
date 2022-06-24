import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda crs: crs[1])
        # print(courses)
        sum_dur = 0
        dur_heap = []
        heapq.heapify(dur_heap)
        course_cnt = 0
        for course in courses:
            sum_dur += course[0]
            heapq.heappush(dur_heap, -course[0])
            course_cnt += 1

            # print(f"course={course}, sum_dur={sum_dur}, dur_head={dur_heap}, course_cnt={course_cnt}")

            while sum_dur > course[1] and len(dur_heap) > 0:
                del_course = -heapq.heappop(dur_heap)
                # print(f"delete del_course={del_course}, course_cnt={course_cnt}")
                sum_dur -= del_course
                course_cnt -= 1

        return course_cnt



r = Solution().scheduleCourse([[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]])
print(r)
