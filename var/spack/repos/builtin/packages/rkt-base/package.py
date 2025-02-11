# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RktBase(RacketPackage):
    """Stub package for packages which are currently part of core
    racket installation (but which may change in the future)."""

    git = "ssh://git@github.com/racket/racket.git"

    maintainers("elfprince13")

    version("8.3", commit="cab83438422bfea0e4bd74bc3e8305e6517cf25f")  # tag='v8.3'

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("racket@8.3", type=("build", "run"), when="@8.3")

    racket_name = "base"
