CREATE OR REPLACE PROCEDURE delete_byname(
	name_todelete VARCHAR
)
AS $$
BEGIN
	DELETE FROM phonebook
	WHERE name = name_todelete;
END
$$
LANGUAGE PLPGSQL;