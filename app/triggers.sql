-- triggers.sql
-- This file defines a function + trigger to increment member.total_check_ins
-- whenever a new attendance row is inserted.

CREATE OR REPLACE FUNCTION increment_total_check_ins()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE member
  SET total_check_ins = total_check_ins + 1
  WHERE id = NEW.member_id;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Drop existing trigger if exists (safe to re-run)
DROP TRIGGER IF EXISTS attendance_after_insert ON attendance;

CREATE TRIGGER attendance_after_insert
AFTER INSERT ON attendance
FOR EACH ROW
EXECUTE FUNCTION increment_total_check_ins();
