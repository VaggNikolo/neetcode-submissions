-- Write your query below
SELECT DISTINCT ON (student_id) * FROM exam_results 
order by student_id, score DESC, exam_id ASC
