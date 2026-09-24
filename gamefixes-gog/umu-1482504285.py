"""Game fix for Batman: Arkham Asylum GOTY Edition (GOG)"""

from protonfixes import util


def main() -> None:
    """Install required DirectX components and PhysX."""
    util.protontricks('d3dx9')
    util.protontricks('d3dcompiler_43')
    util.protontricks('d3dx9_43')
    util.protontricks('physx')
