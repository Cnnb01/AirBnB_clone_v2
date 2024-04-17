#!/usr/bin/python3
"""Test cases for console.py"""

import unittest
import io
import sys
from console import HBNBCommand
from unittest.mock import patch
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    @classmethod
    def setUpClass(cls):
        """Set up for tests"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down after tests"""
        del cls.console

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        self.console.onecmd("create State")
        state_id = mock_stdout.getvalue().strip()
        state = storage.all()["State." + state_id]
        self.assertTrue(state)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        self.console.onecmd("create State")
        state_id = mock_stdout.getvalue().strip()
        self.console.onecmd("show State {}".format(state_id))
        self.assertIn(state_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        self.console.onecmd("create State")
        state_id = mock_stdout.getvalue().strip()
        self.console.onecmd("destroy State {}".format(state_id))
        self.assertNotIn(state_id, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        self.console.onecmd("create State")
        self.console.onecmd("create City")
        self.console.onecmd("create Place")
        self.console.onecmd("all")
        output = mock_stdout.getvalue()
        self.assertIn("State", output)
        self.assertIn("City", output)
        self.assertIn("Place", output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_count(self, mock_stdout):
        """Test count command"""
        self.console.onecmd("create State")
        self.console.onecmd("create State")
        self.console.onecmd("create State")
        self.console.onecmd("create City")
        self.console.onecmd("create Place")
        self.console.onecmd("create Place")
        self.console.onecmd("create Place")
        self.console.onecmd("count State")
        self.assertEqual(mock_stdout.getvalue().strip(), "3")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update(self, mock_stdout):
        """Test update command"""
        self.console.onecmd("create State")
        state_id = mock_stdout.getvalue().strip()
        self.console.onecmd("update State {} name \"California\"".format(state_id))
        state = storage.all()["State." + state_id]
        self.assertEqual(state.name, "California")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        with patch('sys.stdin', io.StringIO('EOF\n')):
            self.console.onecmd("EOF")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_quit(self, mock_stdout):
        """Test help quit command"""
        self.console.onecmd("help quit")
        self.assertIn("Exits the program", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_EOF(self, mock_stdout):
        """Test help EOF command"""
        self.console.onecmd("help EOF")
        self.assertIn("Exits the program", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_emptyline(self, mock_stdout):
        """Test emptyline method"""
        self.console.onecmd("\n")
        self.assertEqual("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_create(self, mock_stdout):
        """Test help create command"""
        self.console.onecmd("help create")
        self.assertIn("Creates a class of any type", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_show(self, mock_stdout):
        """Test help show command"""
        self.console.onecmd("help show")
        self.assertIn("Shows an individual instance", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_destroy(self, mock_stdout):
        """Test help destroy command"""
        self.console.onecmd("help destroy")
        self.assertIn("Destroys an individual instance", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_all(self, mock_stdout):
        """Test help all command"""
        self.console.onecmd("help all")
        self.assertIn("Shows all objects", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_count(self, mock_stdout):
        """Test help count command"""
        self.console.onecmd("help count")
        self.assertIn("Count current number", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_update(self, mock_stdout):
        """Test help update command"""
        self.console.onecmd("help update")
        self.assertIn("Updates an object", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_emptyline(self, mock_stdout):
        """Test emptyline method"""
        self.console.onecmd("\n")
        self.assertEqual("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_precmd(self, mock_stdout):
        """Test precmd method"""
        self.assertEqual(self.console.precmd("City.show()"), "show City")
        self.assertEqual(self.console.precmd("Place.all()"), "all Place")
        self.assertEqual(self.console.precmd("State.update(\"id\", \"name\", \"value\")"), "update State id name value")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_postcmd(self, mock_stdout):
        """Test postcmd method"""
        self.console.postcmd(False, "")
        self.assertIn("(hbnb) ", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_precmd_invalid_command(self, mock_stdout):
        """Test precmd method with invalid command"""
        self.assertEqual(self.console.precmd("InvalidCommand"), "InvalidCommand")



if __name__ == '__main__':
    unittest.main()