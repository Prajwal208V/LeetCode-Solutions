1-- Write your PostgreSQL query statement below
2SELECT s.student_id, s.student_name, subj.subject_name, -- student and subject info
3COUNT(e.subject_name) AS attended_exams -- count attended exams
4FROM Students s
5CROSS JOIN Subjects subj -- generate all student-subject pairs
6LEFT JOIN Examinations e
7ON s.student_id = e.student_id AND subj.subject_name = e.subject_name -- match exams
8GROUP BY s.student_id, s.student_name, subj.subject_name -- group by all
9ORDER BY s.student_id, subj.subject_name; -- required ordering