CREATE OR REPLACE FUNCTION show_table ("name1" varchar)
  RETURNS TABLE(name VARCHAR, number VARCHAR) AS
$$
BEGIN
 RETURN QUERY

 SELECT phonebook.name, phone_number
 FROM phonebook
 WHERE phonebook.name = "name1";

END; $$

LANGUAGE plpgsql;