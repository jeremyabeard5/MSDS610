SELECT
  COUNT(DISTINCT(q.id)) as num_questions,
  COUNT(DISTINCT(ans.owner_user_id)) as num_answerers,
  EXTRACT(YEAR from q.creation_date) as year,
  (COUNT(DISTINCT(ans.owner_user_id)) / COUNT(DISTINCT(q.id)) * 100) as pct_answers
FROM
  `bigquery-public-data.stackoverflow.posts_questions` as q
LEFT JOIN
  `bigquery-public-data.stackoverflow.posts_answers` AS ans
ON
  q.accepted_answer_id = ans.id
GROUP BY
  year
ORDER BY
  year
