CREATE OR REPLACE FUNCTION add_many(
	names VARCHAR [], numbers VARCHAR [], n int
) 
RETURNS TABLE  (wrong_name VARCHAR, wrong_number VARCHAR)
AS $$
BEGIN
	FOR i IN 1..n LOOP
		IF numbers[i] LIKE '+77_________' THEN
			INSERT INTO phonebook
			VALUES(names[i], numbers[i]);
		ELSE 
			wrong_name := names[i];
			wrong_number := numbers[i];
			RETURN NEXT;
		END IF;
	END LOOP;
END
$$
LANGUAGE PLPGSQL;