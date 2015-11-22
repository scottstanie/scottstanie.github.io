-- Average word counts and message lengths
SELECT name,
	AVG(msg_length)::INT as avg_msg_length,
	AVG(word_count)::INT as avg_word_count
FROM fb_messages
GROUP BY 1
ORDER BY 2 DESC

-- Message count by user and time period
WITH grid AS (
SELECT start_time
        , lead(start_time) OVER (ORDER BY start_time) AS end_time
FROM (
	SELECT generate_series(
				min(created_time)::timestamp,
				CURRENT_DATE::timestamp,
				interval '3 months') as start_time
	FROM scratch.fb_messages
	) x
)
SELECT start_time::DATE, name, count(created_time) AS messages
FROM grid g
LEFT JOIN scratch.fb_messages e ON e.created_time >= g.start_time
                   AND e.created_time <  g.end_time
GROUP BY 1,2
ORDER BY 1,3 DESC;


-- Add word counts and message lengths
UPDATE fb_messages f
SET (msg_length, word_count) = (e.msg_length, e.word_count)
FROM (
	SELECT id, name, created_time, length(message) as msg_length,
		array_length(regexp_split_to_array(trim(message), E'\\W+'), 1) as word_count
	FROM fb_messages
	) e
WHERE f.id = e.id


