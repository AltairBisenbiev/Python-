CREATE OR REPLACE FUNCTION show_pag (
    lim int, offs int
)
RETURNS TABLE (names varchar, numbers varchar) AS
$$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook LIMIT lim OFFSET offs;
END;
$$
LANGUAGE PLPGSQL;