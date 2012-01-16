from tests import TestCase


class TestCheckUpdate(TestCase):
    command = "check-update"

    def test_no_updates(self):
        """Check a repo with no available updates."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        expected = []

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_only_updates(self):
        """Check a repo with only updates available."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        expected = [{'update': ('0:foo-1-1.nb5.0.noarch', '0:foo-1-2.nb5.0.noarch')}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)