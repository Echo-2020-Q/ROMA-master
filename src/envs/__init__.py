from functools import partial
#from smac.env import MultiAgentEnv, StarCraft2Env
from .multiagentenv import MultiAgentEnv
from .starcraft2 import StarCraft2Env

import sys
import os
from pathlib import Path

try:
    from .gfootball import GoogleFootballEnv
except Exception:
    GoogleFootballEnv = None

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

REGISTRY = {}
REGISTRY["sc2"] = partial(env_fn, env=StarCraft2Env)
if GoogleFootballEnv is not None:
    REGISTRY["gf"] = partial(env_fn, env=GoogleFootballEnv)

if sys.platform == "linux":
    project_root = Path(__file__).resolve().parents[2]
    os.environ.setdefault("SC2PATH", str(project_root / "3rdparty" / "StarCraftII"))
