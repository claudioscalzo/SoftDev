#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

# Prelude
AC_PREREQ([2.69])
AC_INIT([lame_project], [0.1beta], [scalzo@eurecom.fr])
AM_INIT_AUTOMAKE([-Wall 1.14.1 foreign])
# AC_CONFIG_SRCDIR([src/main/main.c])
AC_CONFIG_HEADERS([config.h]) # convention: only one

# Checks for programs
AC_PROG_CC # from autoscan

# Checks for libraries
AC_PROG_RANLIB # from automake suggestion
AM_PROG_AR # from automake suggestion

# Checks for header files
# (try to compile with 2 params: if it fails, set the one-param function)
AC_COMPILE_IFELSE(
    [AC_LANG_PROGRAM([[#include <mistery.h>]], [[mistery_value(1,2);]])],
    [AC_MSG_RESULT([yes])],
    [AC_DEFINE([MISTERY_VALUE_ONEPARAM], [], [One param])]
)

# Checks for typedefs, structures

# Check for compiler characteristics

# Checks for library functions
AC_SEARCH_LIBS([mistery_value], [mistery magic voodoo])

# Checks for system services

# Output files
AC_CONFIG_FILES([makefile src/makefile src/main/makefile src/lib_foo/makefile])
AC_OUTPUT
