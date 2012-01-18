from tests import TestCase


class TestCheckUpdate(TestCase):
    command = "check-update"
    installonlypkgs = "bar"

    def test_no_updates(self):
        """Check a repo with no available updates."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = []

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_only_updates(self):
        """Check a repo with only updates available."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'update': ('0:foo-1-1.nb5.0.noarch', '0:foo-1-2.nb5.0.noarch')}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_only_install(self):
        """Check a repo with only new installs available."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'install': '0:bar-1-2.nb5.0.noarch'}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_only_obsoletes(self):
        """Check a repo with only obsoletes available."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'obsolete': ('0:bar-1-1.nb5.0.noarch', '0:baz-2-1.nb5.0.noarch')}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_install_as_dep(self):
        """Check a repo with an update requiring a new install."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'update': ('0:toto-1-1.nb5.0.noarch', '0:toto-2-1.nb5.0.noarch')},
                    {'installdep': '0:plouf-2-1.nb5.0.noarch'}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_ordering(self):
        """Check the ordering of the summary for a repo with a bit of everything available."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'obsolete': ('0:bar-1-1.nb5.0.noarch', '0:baz-2-1.nb5.0.noarch')},
                    {'update': ('0:toto-1-1.nb5.0.noarch', '0:toto-2-1.nb5.0.noarch')},
                    {'update': ('0:foo-1-1.nb5.0.noarch', '0:foo-1-2.nb5.0.noarch')},
                    {'installdep': '0:plouf-2-1.nb5.0.noarch'}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)

    def test_ordering_bis(self):
        """Check the ordering of the summary for a repo with a bit of everything available, bis."""
        args = self.parser.parse_args([self.command])
        self._run_nbyum_test(args)

        # -- Check the update summary ------------------------------
        expected = [{'install': '0:bar-1-2.nb5.0.noarch'},
                    {'update': ('0:toto-1-1.nb5.0.noarch', '0:toto-2-1.nb5.0.noarch')},
                    {'update': ('0:foo-1-1.nb5.0.noarch', '0:foo-1-2.nb5.0.noarch')},
                    {'installdep': '0:plouf-2-1.nb5.0.noarch'}]

        result = [eval(line) for line in self.new_stdout.getvalue().split("\n") if line]
        self.assertEqual(result, expected)
