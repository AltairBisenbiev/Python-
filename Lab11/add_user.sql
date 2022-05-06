CREATE OR REPLACE PROCEDURE add_user(
	new_user_name varchar,
	new_phone_number varchar
) 
AS $$
BEGIN
	IF EXISTS (SELECT * FROM phonebook WHERE name = new_user_name) THEN
    	UPDATE phonebook SET phone_number = new_phone_number WHERE name = new_user_name;
	ELSE
		INSERT INTO phonebook
		VALUES(new_user_name, new_phone_number);
	END IF;
END
$$
LANGUAGE PLPGSQL;