SELECT
  q.owner_user_id as q_user_id, q.id, q.answer_count, ans.owner_user_id as ans_user_id
FROM
  `bigquery-public-data.stackoverflow.posts_questions` as q
INNER JOIN
  `bigquery-public-data.stackoverflow.posts_answers` AS ans
ON 
  q.accepted_answer_id = ans.id
LIMIT 2
