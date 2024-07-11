# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install c-deps
#
# You can edit this file again by typing:
#
#     spack edit c-deps
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class CDeps(CMakePackage):
    """Simple package with some dependencies."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gitlab.inria.fr/fayatsll/c-deps"
    url = "https://gitlab.inria.fr/fayatsll/c-deps/-/archive/v0.1.1/c-deps-v0.1.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions and checksums here.
    version("0.1.1", sha256="0dce1315b1fb586f14932894e136d2f1ddb99735bcfe24e4d25983428d181bd2")

    # FIXME: Add dependencies if required.
    depends_on("pkg-config")
    depends_on("sqlite")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
