from unittest import TestCase

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Test")

    def test_student_init__when_correct_name__expect_to_be_initialized(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init__when_courses_is_not_none__expect_to_be_initialized(self):
        student = Student("Test", {"Python": ["note1", "note2"]})
        self.assertEqual("Test", student.name)
        self.assertEqual({"Python": ["note1", "note2"]}, student.courses)

    def test_enroll__when_course_name_is_in_courses__expect_notes_to_be_added(self):
        result = self.student.enroll("Python", ["note1", "note2"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)

    def test_enroll__when_course_name_is_in_courses_and_add_course_notes_is_Y__expect_notes_to_be_added(self):
        result = self.student.enroll("Python", ["note1", "note2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)

    def test_enroll__when_course_name_is_in_courses_and_add_course_notes_is_not_Y__expect_notes_to_be_added(self):
        result = self.student.enroll("Python", ["note1", "note2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python": []}, self.student.courses)

    def test_enroll__when_course_name_is_not_in_courses__expect_notes_to_be_added(self):
        result = self.student.enroll("Python", ["note1", "note2"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": ["note1", "note2"]}, self.student.courses)

    def test_add_notes__when_course_name_is_in_courses__expect_notes_to_be_added(self):
        self.student.enroll("Python", ["note1", "note2"])
        result = self.student.add_notes("Python", "note3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"Python": ["note1", "note2", "note3"]}, self.student.courses)

    def test_add_notes__when_course_name_is_not_in_courses__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", "note3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course__when_course_name_is_in_courses__expect_course_to_be_removed(self):
        self.student.enroll("Python", ["note1", "note2"])
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course__when_course_name_is_not_in_courses__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
