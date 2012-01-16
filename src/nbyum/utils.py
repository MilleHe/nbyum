import argparse


def get_parser():
    """Get the argument parser for the main nbyum command line tool."""
    # -- Root level arguments (-h/--help is added by default) ----------------
    parser = argparse.ArgumentParser(description="Just like yum, " \
                                                 "but with a usable output")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Print some useful debug information")

    subparsers = parser.add_subparsers(title="subcommands")

    # -- Subcommand: check-update --------------------------------------------
    parser_checkupdate = subparsers.add_parser("check-update",
                                               help="Check for updates to " \
                                                    "installed packages")
    parser_checkupdate.add_argument("packages", nargs="*", metavar="PACKAGE",
                                    help="The package(s) for which to check " \
                                         "if an update is available. An " \
                                         "arbitrary number can be specified." \
                                         " If none is, updates for the whole" \
                                         " system are checked.")
    parser_checkupdate.set_defaults(func="check_update")

    # -- Subcommand: update ---------------------------------------------------
    parser_update = subparsers.add_parser("update",
                                          help="Update packages or the " \
                                               "whole system")
    parser_update.add_argument("packages", nargs="*", metavar="PACKAGE",
                               help="The package(s) to update. An arbitrary " \
                                    "number can be specified. If none is, " \
                                    "the whole system is updated.")
    parser_update.set_defaults(func="update")

    return parser

def get_envra(pkg):
    """Get the Epoch:Name-Version-Release.Arch representation of a package."""
    return "%s:%s-%s-%s.%s" % (pkg.epoch, pkg.name, pkg.version,
                               pkg.release, pkg.arch)
