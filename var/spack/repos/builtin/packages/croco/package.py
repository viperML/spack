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
#     spack install example
#
# You can edit this file again by typing:
#
#     spack edit example
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Croco(Package):
    """Coastal and Regional Ocean COmmunity model. CROCO is a modeling platform to study the regional, 
coastal and nearshore ocean (ocean dynamics, sedimentary dynamics, biogeochemistry) on time scales 
ranging from event to multi-decadal, and spatial scales ranging from kilometric to metric resolutions."""

    homepage = "https://www.croco-ocean.org"
    url = "https://gitlab.inria.fr/croco-ocean/croco/-/archive/v2.0.0/croco-v2.0.0.tar.gz"

    maintainers("viperML")

    license("MIT AND CECILL-C", checked_by="viperML")

    version("2.0.0", sha256="c66fa41dd0fa723d3055f046f1463f40f4a0ae567e1d4d387bc85493d572e1b7")

    depends_on("fortran", type="build")
    depends_on("netcdf-fortran")

    phases = ["configure", "build", "install"]

    def configure(self, spec, prefix):
        import os
        import re
        os.chdir("OCEAN")

        with open("jobcomp", "r") as f:
            data = f.read()

        data = re.sub(r'SOURCE=(.*)', f"SOURCE=\"$(realpath .)\"", data)
        data = re.sub(r'RUNDIR=(.*)', f"RUNDIR=\"{prefix}/opt/croco\"", data)

        with open("jobcomp", "w") as f:
            f.write(data)

    def build(self, spec, prefix):
        import subprocess

        subprocess.run(["./jobcomp"])


    def install(self, spec, prefix):
        pass
